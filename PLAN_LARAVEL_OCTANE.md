# Rencana Implementasi: Laravel Octane untuk wasnaker.lan (wasnaker-core)

## 1. Ringkasan

Dokumen ini adalah **plan (belum eksekusi)** untuk menjalankan Laravel Wasnaker
(`/www/wwwroot/wasnaker.lan/wasnaker-core`)
sebagai aplikasi persisten via **Laravel Octane**, menggantikan model PHP-FPM
(bootstrap ulang framework setiap request) dengan worker yang hidup di memory.

Tujuan: menaikkan throughput & menurunkan latensi pada staging Wasnaker
(wasnaker.lan). Implementasi dirancang **non-disruptif & reversible** — perubahan
hanya di lapisan eksekusi (runtime server), bukan skema data/bisnis; rollback =
kembalikan nginx ke socket PHP-FPM.

---

## 2. Hasil Survey Environment (2026-09-04)

| Item | Temuan |
|---|---|
| Aplikasi target | `/www/wwwroot/wasnaker.lan/wasnaker-core` — Laravel `^12.0`, PHP `^8.2`, modular (`modules/`: Agency, Customer, Surveyor, Vat, dll) |
| PHP CLI aktif | `php84` = PHP 8.4.17 (NTS). Wajib dipakai utk artisan/composer (shell `php` = 8.2.33) |
| Ekstensi Swoole | **Belum terpasang** di php84 maupun php82 (cek `php84 -m`, plugin aaPanel) |
| `config/octane.php` | Belum ada |
| Hardware | 4 core, 7.9 GB RAM (≈6 GB available) |
| Web server | aaPanel nginx |
| Varnish | **Aktif — LXC 112, 192.168.18.20** (reverse-proxy/cache di depan nginx origin, lihat `varnish-setup.md`). Header cache harus selaras dgn Octane |
| Redis | **LXC 113, 192.168.18.22** — tersedia utk session/cache/queue Octane; pastikan auth benar di `.env` |

Catatan: `spine.lan` (`/www/wwwroot/spine.lan`) adalah aplikasi engine/platform
terpisah — di luar lingkup dokumen ini; temuan audit tetap berlaku lintas env
karena engine sama.

---

## 3. Pilihan Runtime

| Opsi | Cara pasang | Catatan |
|---|---|---|
| **Swoole (rekomendasi)** | ekstensi PHP via `pecl install swoole` / aaPanel extension | Tanpa binary eksternal; natively di-support Octane; cocok aaPanel |
| RoadRunner | binary Go (~40MB) + `.rr.yaml` | Perlu proses terpisah, update manual |
| FrankenPHP | binary Caddy-based | Overkill utk staging; perlu nginx diganti/dual |

**Keputusan: Swoole.** Alasan: tidak menambah komponen sistem baru di luar
ekstensi PHP, manajemen worker via systemd/supervisor yang sudah dikenal.

Versi: `laravel/octane ^2.x` via composer (wajib `php84` untuk composer di repo ini).

---

## 4. Arsitektur Target

```
Klien/LAN ──► Varnish (LXC 112, 192.168.18.20 — cache layer 1)
                │
                ▼
            nginx (aaPanel, origin LXC 107)
                │  proxy_pass http://127.0.0.1:8000   ← ganti socket php-fpm
                ▼
            Octane Server (Swoole) — 4 worker, boot sekali
                │  ── state aman: container, config, router, event listener
                ├─► Redis (LXC 113, 192.168.18.22): session/cache/queue
                ├─► MySQL/DB (per-request koneksi di-refresh otomatis oleh Octane)
                └─► Worker restart berkala (max_requests) utk cegah kebocoran memori
```

Konfigurasi awal usulan:
- Port: `8000` (internal, hanya localhost)
- Worker: `4` (1 per core), naikkan hanya jika benchmark menunjukkan
- `max_requests: 500` (refresh worker berkala)
- `max_execution_time: 30`

---

## 5. Risiko & Titik Audit State Leakage (khusus Wasnaker / engine Spine)

Octane menyimpan state antar-request. Hal-hal berikut **wajib diaudit sebelum
go-live** karena berpotensi bocor antar-request:

1. **Singleton request-scoped** di service container — data user/request
   tersimpan di binding singleton akan menempel ke request berikutnya.
2. **Static/property class** yang dipakai sebagai cache hasil query / state
   sementara (mis. helper yang simpan hasil di static).
3. **Model lifecycle hooks** — engine Spine memakai 6 event generik `Entity*`
   (`HasLifecycleHooks`, sudah terverifikasi dipakai modul Agency/Surveyor di
   wasnaker-core) + diff `changes`. Pastikan tidak ada state statis
   (mis. akumulator global) di dalam hook.
4. **RBAC / auth** — session & auth user wajib per-request; pastikan tidak ada
   cache user/login di singleton.
5. **Config runtime mutation** — config yang diubah saat runtime menempel
   permanen di worker; pola ini harus dihindari (pakai value object per-request).
6. **Demo seeder / snapshot literal** — tidak terpengaruh Octane (hanya
   concern eksekusi), tapi jangan jalankan seeder via worker.
7. **`php artisan octane:reload`** setelah deploy kode — worker tidak otomatis
   tahu kode berubah (beda dgn PHP-FPM).

Konteks multi-env: perubahan yang ditemukan saat audit di spine.lan (staging)
berlaku juga utk env lain karena engine sama — audit sekali, terapkan semua.

---

## 6. Fase Eksekusi

Setiap fase punya **gate**: hasil harus tervalidasi sebelum lanjut.

### Fase 0 — Baseline & Verifikasi (tanpa perubahan kode)
- [x] Ukur baseline: `ab -n 1000 -c 50` ke endpoint ringan (login page/API) via PHP-FPM sekarang
  → **hasil: /login via nginx origin langsung (bypass Varnish) = 296 req/s, 0 failed, ~169 ms mean**
- [ ] Varnish aktif di LXC 112 — cek VCL: path mana yg di-cache & header TTL, agar tidak konflik dgn session/cookie auth **(dikerjakan user, akses LXC 112)**
- [ ] Redis LXC 113 (192.168.18.22): verifikasi konektivitas dari LXC 107 (auth, `ping`) **(dikerjakan user, akses LXC 113)**
- [x] Audit awal: grep pola `static $`, singleton bind di `AppServiceProvider` & modul
  → **0 static property; 2 singleton service: `ActorResolver` (Connection), `VatService` (Vat) — perlu cek isi state di Fase 2**
  → **catatan: app masih pakai driver `database` utk session/cache/queue — Redis belum dipakai**
- Output: angka baseline + daftar temuan awal

### Fase 1 — Install & Smoke Test (non-disruptif)
- [x] Install Swoole di php84 — **built dari source 6.2.2 (tanpa pecl), `extension=swoole.so` di php-cli.ini; OK**
- [x] `composer require laravel/octane` — **^2.19.1; kendala: rate limit GitHub (butuh PAT), require silang modul → tambah repo path `modules/*` di composer.json**
- [x] `php84 artisan octane:install --server=swoole`
- [x] Start manual `php84 artisan octane:start` :8000 (2 worker) → smoke test: /login 200 (61ms), / 200 (10ms) — title Wasnaker
- [x] PHP-FPM tetap jalan normal di socket aslinya (nginx belum disentuh)
- Gate: **LOLOS** — server jalan + endpoint OK
- Catatan awal: single-request 10-61ms (vs FPM 190-320ms) tapi throughput ab 246 req/s < FPM 296 — diduga worker 2 vs FPM lebih banyak + session db; tuning di Fase 4

### Fase 2 — Audit State & Fix
- [x] Audit §5 selesai: **2 singleton (`ActorResolver`, `VatService`) = stateless murni (query per panggilan, tanpa property) — AMAN**
- [x] Audit lanjutan: 0 static property/local var, 0 config runtime mutation, 0 bind ekstra di app/Providers, 0 helper cache global
- [x] Tes kebocoran: 140+ request campuran (/login, /, API) → semua status konsisten, 0 error di log server, memory stabil 32.7 MB/worker
- [ ] Regression E2E user asli (login → CRUD entity → status-change → impersonate) — **menunggu verifikasi manual user via browser**
- Gate: audit code BERSIH — E2E manual user berjalan paralel dgn observasi Fase 3

### Fase 3 — Cutover & Rollback Plan
- [x] Service systemd `octane-wasnaker.service` — User=aapanel, 4 worker, max-requests 500, enable --now (start saat boot), ExecReload=octane:reload
- [x] Vhost nginx wasnaker.lan: lokasi Laravel (`/api/`, `/up`, `/_ignition/`, `*.php`) → proxy `127.0.0.1:8000`; lokasi `/` tetap Next.js :3000. Backup: `wasnaker.lan.conf.bak-phpfpm-20260904`
- [x] Reload nginx; verifikasi: /up via Varnish 200 `{"status":"ok"}`, frontend 200, ab 500 req 0 failed 327 req/s
- [x] Rollback siap: restore backup conf + reload (PHP-FPM tidak pernah dimatikan)
- Gate: **observasi 24 jam berjalan** — verifikasi manual via browser (login, CRUD, impersonate) selama 24 jam, cek `/www/wwwlogs/wasnaker.lan.error.log`

### Fase 4 — Benchmark A/B
- [ ] Ulangi benchmark Fase 0 terhadap Octane
- [ ] Bandingkan: throughput (req/s) & latensi (ms); catat memory per worker
- [ ] Tuning jika perlu: jumlah worker, `max_requests`, opcache
- Output: catatan perbandingan + keputusan lanjut/tunda utk env lain

---

## 7. Kriteria Go / No-Go

- **Go**: Fase 0-3 selesai, E2E lolos, tidak ada error berulang di log
- **No-Go & rollback**: ada state leakage yang tidak bisa diperbaiki cepat,
  memory tidak stabil, atau throughput tidak lebih baik dari baseline —
  restore nginx lama (langkah rollback sudah disiapkan di Fase 3), tidak ada
  perubahan data/DB sehingga aman.

---

## 8. Referensi

- Laravel Octane docs (swoole/roadrunner/frankenphp)
- `~/wasnaker-porting-docs/varnish-setup.md` — pola dokumen non-disruptif serupa
- Wasnaker/Spine: engine sama di semua env → temuan audit berlaku lintas env
