# Dokumentasi Teknis: Varnish Cache Server

## 1. Ringkasan

Dokumen ini menjelaskan implementasi **Varnish Cache Server** di lingkungan Proxmox VE
untuk mempercepat delivery konten web (HTTP) dengan memposisikan Varnish sebagai
reverse-proxy/cache di depan web server nginx yang di-host pada aapanel (LXC 107).

Implementasi dirancang **non-disruptif** — yaitu tidak mengubah konfigurasi web server
origin, tidak memindahkan port, dan tidak menyebabkan downtime bagi pengguna yang sedang
menggunakan layanan.

---

## 2. Arsitektur

### 2.1 Diagram Aliran Permintaan

```
                    ┌─────────────────────────────────────────────┐
                    │              Jaringan Lokal (LAN)           │
                    │                                              │
  Klien/Laptop ────►│  Varnish (LXC 112)                          │
  (Browser)         │  192.168.18.20:80                           │
                    │  reverse-proxy + cache                      │
                    │         │                                   │
                    │         ▼ (backend)                         │
                    │  nginx origin (LXC 107 / aapanel)           │
                    │  192.168.18.17:80                           │
                    │         │                                   │
                    │         ▼                                    │
                    │  PHP-FPM (Laravel) / Node (Next.js)          │
                    └─────────────────────────────────────────────┘
```

### 2.2 Komponen

| Komponen             | Nilai                          |
|----------------------|--------------------------------|
| LXC Varnish (VMID)   | `112`                          |
| Hostname             | `varnish`                      |
| OS                   | Ubuntu 26.04 LTS (standard)    |
| IP Address           | `192.168.18.20`                |
| DNS                  | `varnish.lan`                  |
| Varnish Version      | `7.7.3`                        |
| Port Listen (Varnish)| `80`                           |
| Backend (origin)     | `192.168.18.17:80` (nginx aapanel) |
| Storage Container    | `HDD01SAS2TB`                  |
| Spesifikasi          | 2 core, 2048 MB RAM, 512 MB swap |

---

## 3. Langkah Implementasi

### 3.1 Membuat LXC Container

Template yang digunakan tersedia pada storage `HDD01SAS2TB`:

```
HDD01SAS2TB:vztmpl/ubuntu-26.04-standard_26.04-1_amd64.tar.zst
```

Perintah pembuatan (dijalankan pada node Proxmox):

```bash
pct create 112 HDD01SAS2TB:vztmpl/ubuntu-26.04-standard_26.04-1_amd64.tar.zst \
  --hostname varnish \
  --storage HDD01SAS2TB \
  --net0 name=eth0,bridge=vmbr0,firewall=1,gw=192.168.18.1,ip=192.168.18.20/24,type=veth \
  --cores 2 \
  --memory 2048 \
  --swap 512 \
  --ostype ubuntu \
  --features nesting=1
```

Menjalankan container:

```bash
pct start 112
```

Verifikasi jaringan:

```bash
pct exec 112 -- ip addr show eth0
pct exec 112 -- ping -c 2 192.168.18.17
```

### 3.2 Instalasi Varnish

```bash
pct exec 112 -- bash -c 'apt-get update -qq && apt-get install -y -qq varnish'
pct exec 112 -- varnishd -V
```

Output menunjukkan versi yang terpasang, contoh: `varnishd (varnish-7.7.3 ...)`.

### 3.3 Mengubah Port Bind Varnish ke 80

Secara default Varnish listen pada port `6081`. Ubah pada systemd unit:

```bash
pct exec 112 -- bash -c \
  'sed -i "s/-a :6081/-a :80/" /lib/systemd/system/varnish.service && \
   systemctl daemon-reload && \
   systemctl enable varnish && \
   systemctl restart varnish'
```

Verifikasi port:

```bash
pct exec 112 -- ss -tlnp | grep ":80"
```

---

## 4. Konfigurasi VCL

Berikut isi `/etc/varnish/default.vcl` yang diterapkan.

```vcl
vcl 4.1;

backend default {
    .host = "192.168.18.17";
    .port = "80";
}

sub vcl_recv {
    # Hanya layani metode GET/HEAD
    if (req.method != "GET" && req.method != "HEAD") {
        return (pass);
    }

    # Bypass endpoint dinamis Laravel API
    if (req.url ~ "^\/(api|up|_ignition)(\/|$)") {
        return (pass);
    }

    # Bypass bila ada cookie auth / set-cookie
    if (req.http.Cookie) {
        return (pass);
    }

    return (hash);
}

sub vcl_backend_response {
    # Jangan cache bila backend kirim Set-Cookie
    if (beresp.http.Set-Cookie) {
        set beresp.uncacheable = true;
        return (deliver);
    }

    # Cache aset statis lebih lama
    if (bereq.url ~ "\.(css|js|gif|jpg|jpeg|png|webp|svg|ico|woff2|woff|eot|ttf|otf)(\?.*)?$") {
        set beresp.ttl = 24h;
        unset beresp.http.Set-Cookie;
        return (deliver);
    }

    # HTML: cache singkat untuk konten publik
    if (beresp.status == 200 || beresp.status == 301 || beresp.status == 302 || beresp.status == 404) {
        set beresp.ttl = 30s;
        return (deliver);
    }

    # Lainnya: tidak cache
    set beresp.uncacheable = true;
    return (deliver);
}

sub vcl_deliver {
    if (obj.hits > 0) {
        set resp.http.X-Cache = "HIT";
    } else {
        set resp.http.X-Cache = "MISS";
    }
}
```

### 4.1 Validasi VCL

Compile check tanpa menjalankan Varnish:

```bash
pct exec 112 -- varnishd -C -f /etc/varnish/default.vcl
```

Jika tidak ada error, gunakan `varnishreload` untuk reload tanpa downtime:

```bash
pct exec 112 -- /usr/share/varnish/varnishreload
```

---

## 5. Kebijakan Cache (Policy)

| Jenis Konten                | Perlakuan                          |
|-----------------------------|------------------------------------|
| GET/HEAD                    | Boleh masuk pipeline cache         |
| POST / PUT / DELETE         | `return (pass)` — selalu diteruskan |
| `/api/*`, `/up`, `/_ignition` | `return (pass)` — bypass (dinamis) |
| Request dengan `Cookie`     | `return (pass)` — bypass           |
| Aset statis (`css/js/img/font`) | Cache 24 jam                    |
| HTML publik (status 2xx/404) | Cache 30 detik                    |
| Response dengan `Set-Cookie` | Tidak di-cache                     |

---

## 6. Verifikasi & Pengujian

### 6.1 Uji dari LXC Varnish

```bash
pct exec 112 -- curl -s -I -H "Host: apidocs.wasnaker.lan" http://127.0.0.1/
pct exec 112 -- curl -s -I -H "Host: wasnaker.lan" http://127.0.0.1/
```

### 6.2 Uji dari Laptop/Klien

```bash
# Akses via Varnish IP dengan Host header
curl -I -H "Host: apidocs.wasnaker.lan" http://192.168.18.20
curl -I -H "Host: wasnaker.lan" http://192.168.18.20
```

### 6.3 Indikator Cache

Perhatikan header pada response:

```
X-Varnish: 32775
Via: 1.1 varnish (Varnish/7.7)
X-Cache: HIT      <-- berasal dari cache
X-Cache: MISS     <-- pertama kali / belum ter-cache
Age: 0
```

- `X-Cache: HIT` → objek dilayani dari cache Varnish.
- `X-Cache: MISS` → objek diambil dari backend (origin) dan disimpan ke cache.
- `Via: 1.1 varnish (Varnish/7.7)` → konfirmasi permintaan melewati Varnish.

---

## 7. Verifikasi Non-Disruptif

Penting: implementasi tidak mengubah web server origin.

```bash
# Backend tetap normal (dari aapanel LXC 107)
pct exec 107 -- curl -s -o /dev/null -w "%{http_code}\n" -H "Host: wasnaker.lan" http://127.0.0.1/
pct exec 107 -- curl -s -o /dev/null -w "%{http_code}\n" -H "Host: apidocs.wasnaker.lan" http://127.0.0.1/
```

Keduanya harus mengembalikan `200`. Konfigurasi vhost dan port nginx di aapanel
tidak diubah sama sekali.

---

## 8. DNS

### 8.1 Entri DNS di MikroTik

Entri DNS statik ditambahkan pada router MikroTik (`192.168.18.12`):

```
/ip dns static
add name=varnish.lan address=192.168.18.20 type=A comment=varnish-LXC112
```

Daftar entri yang sudah ada (untuk referensi):

| Nama                  | Type | Address        |
|-----------------------|------|----------------|
| `varnish.lan`         | A    | `192.168.18.20` |
| `wasnaker.lan`        | A    | `192.168.18.17` |
| `wasnaker-old.lan`    | A    | `192.168.18.17` |
| `apidocs.wasnaker.lan`| A    | `192.168.18.17` |
| `kayudolken.lan`      | A    | `192.168.18.17` |

> **Catatan runout:** Untuk mengarahkan traffic melalui Varnish, ubah entri DNS
> subdomain terkait (mis. `wasnaker.lan`, `apidocs.wasnaker.lan`) agar mengarah ke
> `192.168.18.20` (Varnish). Backend nginx di `192.168.18.17:80` tetap menjadi origin.

---

## 9. Operasional & Pemecahan Masalah

### 9.1 Menjalankan ulang (restart) Varnish

```bash
pct exec 112 -- systemctl restart varnish
```

### 9.2 Reload VCL tanpa downtime

```bash
pct exec 112 -- /usr/share/varnish/varnishreload
```

### 9.3 Melihat statistik cache

```bash
pct exec 112 -- varnishstat
```

### 9.4 Melihat log real-time

```bash
pct exec 112 -- varnishlog -g request
```

### 9.5 Menghapus cache (purge)

Dengan Varnish CLI:

```bash
pct exec 112 -- varnishadm ban 'req.url ~ /'
```

> Ban ini menghapus semua objek dari cache.

### 9.6 Akses SSH ke LXC Varnish

```bash
ssh -i ~/.ssh/id_rsa_mkt01 root@192.168.18.20
```

---

## 10. Referensi Hostname / Backend Origin

| Item                  | Nilai                          |
|-----------------------|--------------------------------|
| Origin hostname       | `aapanel` (LXC 107)            |
| Origin IP             | `192.168.18.17`                |
| Origin port           | `80` (nginx)                   |
| Layanan origin        | PHP-FPM (Laravel), Node (Next.js) |

---

*Dokumen ini dibuat berdasarkan implementasi 27 Agustus 2026.*
