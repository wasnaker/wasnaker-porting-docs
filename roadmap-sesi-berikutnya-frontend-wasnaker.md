# Roadmap Sesi Berikutnya — Frontend Wasnaker (NextAdmin)

> Dokumen ini = panduan on-boarding sesi baru. Dibaca PERTAMA sebelum kerja:
> 1. `resume-sesi-2026-09-02.md` — semua yang sudah dikerjakan di Spine
> 2. `porting-frontend.md` — checklist porting + catatan keputusan
> 3. File ini — rencana konkret langkah berikutnya

## 1. Konteks singkat

- **Spine selesai**: backend (package `laravelspine/spine`) + 2 modul contoh
  (Sample di `boilerplates`, SampleTasks) + frontend contoh (`nextjs-spine`)
  — semua ter-push GitHub + live di `spine.lan`.
- **Keputusan**: frontend PRODUKSI wasnaker pakai **NextAdmin free** (bukan
  nextjs-spine). Backend Spine frontend-agnostic — TIDAK disentuh.
- `tailadmin.lan` (TailAdmin 2.3.0) & `nextadmin.lan` (NextAdmin 2.0.0) =
  native reference, JANGAN diubah.

## 2. Langkah 1 — Setup frontend baru

1. Clone NextAdmin free dari repo resmi (`https://nextadmin.co/` — cek README
   di `/www/wwwroot/nextadmin/` untuk URL repo) → lokasi baru
   (usulan: `/www/wwwroot/wasnaker-frontend/` — konfirmasi nama).
2. `npm install` + `npm run build` (pola deploy: stop→build→start, hindari race .next).
3. Buat systemd service (pola `tailadmin.service` port 3003 → port baru, mis. 3004).
4. Buat vhost di aaPanel (domain wasnaker) → proxy ke port service.
5. Verifikasi: halaman dashboard NextAdmin tampil.

## 3. Langkah 2 — Adapter Spine (pola dari nextjs-spine)

Backend kontrak tetap:
- `/api/v1/modules/extensions` → menu/widgets/detail_tabs
- `/api/v1/{module}/{id}` + `?parent_id` + `/activity-logs`
- Setting `tables_pagination_limit`

Yang DIBANGUN ulang di NextAdmin (implementasi ulang, bukan copy kode):
1. `lib/api.ts` — wrapper fetch (Bearer token, JSON, error) — lihat
   `/www/wwwroot/nextjs-spine/lib/api.ts` sebagai referensi POLA.
2. `lib/use-pagination-limit.ts` — baca setting pagination.
3. **SmallTable** → pakai **TanStack Table** NextAdmin + panel detail bertab:
   - mode kecil (tabel 5/12 + panel 7/12, kolom non-primary hidden)
   - hash `#id` saat klik baris (bukan saat load)
   - header `STATUS|#ID|TITLE`
   - toolbar: Mark as {STATUS}, Edit, PDF, Toggle
   - search client-side (title + parent name)
   - semantic class names (sesuai struktur NextAdmin)
4. **TabContent** → konten tab generik:
   - array → tabel + badge status; objek → vertical dl
   - `hideKeys` / `customValue` (parent title, ulid hidden)
   - `inlineData` untuk tab overview (tanpa fetch — smooth pindah record)
   - SWR cache per URL + skeleton shimmer (bukan teks "Memuat...")
5. Konsumsi `detail_tabs` + `extend_detail_tabs` dari extensions.

## 4. Langkah 3 — Modul pertama produksi

- Pilih modul legacy pertama untuk di-port (usulan: **Quotations** — paling
  kompleks di legacy, ground truth ada di `/www/wwwroot/app.ciptamasjaya.co.id/`
  + daftar hook di `wasnaker-porting-docs/inventaris-hook-ciptamasjaya.md`).
- Buat modul backend pakai scaffold: `module:make-spine Quotations --entity=Quotation`
  + `entity:make-spine QuotationItem --module=Quotations --parent=Quotation`.
- Halaman frontend NextAdmin konsumsi modul tsb (pola halaman sample/tasks di
  nextjs-spine).

## 5. Konvensi yang TIDAK BOLEH dilanggar

- Commit message bahasa Inggris; jangan commit hostname `.lan` / path internal
  (`/www/wwwroot`) / kata 'perfex' — pakai placeholder (`http://localhost`, `<path-to-app>`).
- Bangun theme system (design tokens) DULU sebelum visual; NextAdmin sudah punya
  semantic tokens — gunakan itu, jangan hardcode warna per halaman.
- Modul FPM/chown: folder yang ditulis PHP-FPM (Modules/, uploads) → chown www:www.
- Verifikasi: skrip ad-hoc tempfile `hermes-verify-*` (build + start + readiness + E2E).
- Sebelum porting pola legacy: BACA ULANG kode legacy sebagai ground truth.

## 6. Catatan teknis sesi ini (hemat waktu)

- Build Next.js: stop service → `npm run build` → start (hindari race .next).
- Cache nginx: pastikan `proxy_cache off` di vhost dev (cache HTML bikin verifikasi salah).
- Credential helper git inline ada di `boilerplates` repo — salin ke repo baru
  (`git config credential.helper ...`) kalau push gagal.
- Scaffold tersedia: `module:make-spine` (`--entity=`), `entity:make-spine`
  (`--module=`, `--parent=`) — sudah ter-install di konsumen spine.lan.
- Hook pattern: EntityCreated/Updated/Deleted + `changes` diff + `prevent()`;
  `extend_detail_tabs` untuk tab lintas modul; parent-status sync contoh di
  `SyncSampleStatusFromTasks`.
