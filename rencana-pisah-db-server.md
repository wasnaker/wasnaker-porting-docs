# Rencana: Pisah DB Server dari aaPanel (LXC 107)

Tanggal: 2026-09-05 (05:00 WIB — ditunda, user capek)
Status: **rencana — belum dieksekusi**

## Alasan (keputusan user)
Single-source konfigurasi antara staging & production — tidak ada perbedaan
config, mudah debug. DB server dipisah seperti Varnish (112) & Redis (113).

## Arsitektur target
- Browser → Varnish (LXC 112 .20) → nginx (LXC 107 .17) → Next.js :3000 + Octane :8000
- MySQL/MariaDB → LXC baru (mis. 114) — local network saja (bind 192.168.18.x)
- Redis (LXC 113 .22) sudah terpisah ✓

## Kondisi staging sekarang (verified 2026-09-05)
- MySQL di aaPanel (LXC 107): CPU 0.9%, RSS 194MB, buffer pool 1GB,
  max_connections 500, RAM 8GB (6.3GB free) — ringan, tidak urgent
- DB: wasnaker 2.0MB (37 tabel), spine 0.6MB (19), ci_app 66.2MB (207)

## Langkah
1. Buat LXC baru (114?) + install MySQL 8 (sama versi dgn aaPanel biar config identik)
2. Konfigurasi identik: innodb_buffer_pool_size=1G, max_connections=500,
   character set utf8mb4, timezone
3. Dump semua DB dari aaPanel: `mysqldump --single-transaction` → import ke LXC baru
   (wasnaker, spine, ci_app)
4. Buat user DB khusus app (bukan root): `wasnaker` / password dari .env staging
5. Update `/www/wwwroot/wasnaker.lan/wasnaker-core/.env`:
   DB_HOST=192.168.18.<db-lxc>, DB_PORT=3306, DB_DATABASE, DB_USERNAME, DB_PASSWORD
6. `php artisan config:cache` + `sudo systemctl reload octane-wasnaker`
7. Verifikasi: login API, tinker query, halaman /agencies, /users
8. Firewall: MySQL bind ke IP LXC 107 saja (bukan 0.0.0.0)

## Rollback
- Simpan .env.bak (sudah ada pola `.env.bak-pre-*`)
- Balikin DB_HOST ke 127.0.0.1 + reload octane = kembali ke aaPanel MySQL

## Catatan untuk production (clone dari staging)
- IP Redis/DB di .env WAJIB diganti (jangan ikut ter-clone)
- Production: DB LXC sama arsitekturnya → single source config (alasan user)
