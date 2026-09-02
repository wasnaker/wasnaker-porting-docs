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
- **KEPUTUSAN ARSITEKTUR (sesi lanjutan 2026-09-02)**: nextjs-spine lama
  (`/www/wwwroot/nextjs-spine`) TERLALU BESAR karena dibangun sebagai app utuh
  sebelum shell ada. Ia pensiun sbg REFERENSI pola; demo spine.lan tetap
  jalan. CATATAN: pola `lib/master-detail.tsx` (list + panel bertab) SUDAH
  tergantikan oleh `SmallTable` NextAdmin (TanStack, mode kecil 5/12 + panel
  7/12, hash #id, tab dari detail_tabs) + `TabContent` — tidak ada gap
  fungsional adaptor tersisa; verifikasi paritas = halaman modul produksi.
  berikutnya (layer portable, bisa dipasang di shell mana pun) = layer yg
  dikerjakan DI NextAdmin: `services/spine/*` (api, auth-context,
  module-extensions, dashboard-state, use-pagination-limit — sudah 0
  dependensi shell) + `components/spine/*` (pakai tailgrids/core) +
  `components/dashboard/*`.
- **KEPUTUSAN: POLA 1 DISETUJUI (2026-09-02) — eksekusi BELUM dijalankan.**
  Package layer portable DI-EKSTRAK DARI NEXTADMIN (`services/spine/*` +
  `components/spine/*` + `components/dashboard/*`), bukan rombak nextjs-spine
  lama. Rencana eksekusi (nama kerja repo: `spine-frontend`, path-repo):
  - Tahap A: repo package + pindah `services/spine` (sudah 0 dependensi shell).
  - Tahap B: pindah komponen visual + primitif yang dipakai (badge/button/
    card/field/input/input-group/table/skeleton dari tailgrids/core + cn) +
    ganti import `@/components/common/header/icons` (shell) dgn ikon lokal.
  - Tahap C: NextAdmin konsumsi via path-repo: `next.config transpilePackages`,
    tailwind content include pkg, import `theme.css`, hapus folder lama.
  - Tahap D: build + E2E 14/14.
  - Tahap E: konsumen kedua = TailAdmin utk spine.lan (nextjs-spine lama
    pensiun setelah itu).
  TEMUAN PENTING (biaya netralisasi): SEMUA lapisan visual pakai token
  semantic CSS shell — tailgrids/core (`bg-badge-*-background`, dll) &
  komponen (`text-text-primary`, `bg-card-background`, `border-card-border`,
  `icon-*`, `primary-*`) yang didefinisikan via `@theme` di `globals.css`
  NextAdmin. Utility custom hanya ter-generate bila token ada di @theme
  konsumen → package WAJIB membawa `theme.css` berisi `@theme` token netral
  (prefix `spine-*`) + `:root` default; konsumen `@import` di css-nya; shell
  bisa override var utk menyamakan identitas visual. Tailwind v4: file css
  package ikut di-scan utk utility. React 19 + @tanstack/react-query +
  @dnd-kit/react + sonner = peerDeps.

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

## 4. Langkah 3 — Kerangka dashboard widget (INFRA, sebelum modul bisnis)

✅ **SELESAI sesi 2026-09-02** (commit `702fe1a` — lokasi:
`/www/wwwroot/wasnaker.lan/wasnaker-frontend`, file di bawah). Backend sudah final
(state per user + katalog widget di Spine, terverifikasi):

- Kontrak: GET/PUT `/api/v1/dashboard/order`, PUT `.../visibility`,
  POST `.../reset`; area layout BEBAS (frontend yang define grid);
  area default per widget dari manifest modul
  (`extensions.widgets`: `{id, area, title, api}`).
- Semantik merge (dari `application/helpers/widgets_helper.php`): layout
  null → semua di area default; layout ada → render saved + FALLBACK widget
  tak-tertempatkan ke area default-nya; visibility hide.

Yang DIBANGUN di NextAdmin (`/www/wwwroot/wasnaker.lan/wasnaker-frontend`):
1. Registry widget React: map widgetId → komponen; katalog "yang ADA" dari
   `extensions.widgets`; widget terdaftar tanpa komponen → kartu placeholder
   (modul boleh daftar manifest duluan). — `src/components/dashboard/widget-registry.tsx`
2. Halaman dashboard (home) jadi host: grid area frontend = 8 area base
   legacy (`top-12` → `middle-left/right-6` → `left-8/right-4` →
   `bottom-×3`), urutan = posisi di dashboard.php. Lebar kolom DITURUNKAN
   dari suffix id (grid 12) → area 3/4/6 kolom tinggal definisikan id
   (akhiran `-4`/`-3`/`-2`). Area efektif = base + area default widget di
   katalog modul + area di layout user (append di bawah — KEPUTUSAN:
   posisi sisip tengah via konvensi blok ditunda sampai modul produksi
   nyata butuh). — `src/app/(with-layouts)/(dashboard)/(home)/page.tsx`
3. Merge render sesuai semantik di atas. — `src/components/dashboard/dashboard-merge.ts`
   (pure, self-check `node dashboard-merge.js` setelah tsc: 12 assert)
4. Hook state (SWR): GET/PUT order, PUT visibility, POST reset. —
   `src/services/spine/dashboard-state.ts` (react-query; key cache HARUS
   `["spine","dashboard",token]` exact agar optimistic update kena)
5. DnD antar-area + reorder (@dnd-kit/react sudah di deps) → PUT state penuh
   per drop; area kosong → `'empty'` (backend terima + normalisasi). —
   `src/components/dashboard/dashboard-grid.tsx` + `dashboard-widget-card.tsx`
   (item: `useSortable({id,index,group:area,type:'item',accept:'item'})`;
   kolom: `useDroppable` CollisionPriority.Low; update state HANYA di
   onDragEnd via cache optimistic — plugin OptimisticSorting update
   `source.index/group` final; drop ke kolom kosong = branch target
   `type==='column'` → append akhir)
6. Dropzone visuals: area valid terlihat saat drag (kotak dashed, pola
   legacy `.placeholder-dashboard-widgets`) + toggle "preview widgetable
   area" (widget disembunyikan, semua area kosong tampil — pola WordPress).
7. Visibility toggle per widget: panel "Widgets" (checkbox, padanan
   screen-options legacy — WAJIB ada karena tombol eye di kartu yang hidden
   tak terjangkau) + tombol eye per kartu (sembunyikan cepat).
8. Uji dengan widget Sample (sudah terdaftar di backend) → bukti kerangka
   hidup; verifikasi ad-hoc `hermes-verify-*` (DnD E2E).

## 5. Langkah 4 — Modul pertama produksi

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
