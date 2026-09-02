# Resume Sesi 2026-09-02 — Frontend Wasnaker (rombak abis → NextAdmin)

> On-boarding sesi berikutnya: baca file ini + `roadmap-sesi-berikutnya-frontend-wasnaker.md`.
> CATATAN: sesi lanjutan MENYENTUH Spine (backend) — lihat §9; "Backend Spine TIDAK disentuh" sudah tidak berlaku.

## 1. Keputusan sesi

- Frontend produksi wasnaker = **NextAdmin free** (clone resmi `NextAdminHQ/nextjs-admin-dashboard`),
  bukan scaffold lama (nextjs-spine pattern sebagai referensi pola, bukan copy).
- Lokasi TETAP: `/www/wwwroot/wasnaker.lan/wasnaker-frontend/` (di dalam monorepo wasnaker.lan) —
  service systemd & vhost tidak berubah. Usulan roadmap `/www/wwwroot/wasnaker-frontend/` DIBATALKAN.
- Scaffold lama (4 commit, halaman home doang) DIWIPEH total (git history lama hilang — sengaja).

## 2. Temuan infrastruktur (penting!)

- `wasnaker.lan` → vhost `/www/server/panel/vhost/nginx/wasnaker.lan.conf` (root-only, baca via sudo):
  - `location /api/`, `/up`, `/_ignition/`, `*.php` → PHP-FPM → **wasnaker-core** (Laravel backend)
  - `location /` → `proxy_pass http://127.0.0.1:3000` (Next.js frontend)
- `wasnaker-web.service` (systemd): Next.js **standalone** `.next/standalone/server.js`, User=www, port 3000.
- **Proxy cache global**: `/www/server/nginx/conf/proxy.conf` set `proxy_cache cache_one` untuk SEMUA
  proxy_pass → HTML lama ke-cache (gejala: title "Create Next App" lama, asset hash lama 404,
  padahal :3000 sudah baru). FIX: `proxy_cache off;` di vhost wasnaker.lan.conf (pola sama dengan
  spine.lan.conf:57) + purge `/www/server/nginx/proxy_cache_dir/` + reload. JANGAN verifikasi lewat
  domain kalau cache ini aktif tanpa purge.
- `/wasnaker-frontend/` di URL = 404 wajar (bukan route app; app diserve di ROOT wasnaker.lan).

## 3. Yang dikerjakan

1. `sudo systemctl stop wasnaker-web.service` → wipe isi dir frontend (chown dulu: `sudo chown -R aapanel:aapanel`)
2. `git clone https://github.com/NextAdminHQ/nextjs-admin-dashboard.git .` (v2.0.0)
3. `next.config.ts`: `{ output: "standalone" }` (hapus allowedDevOrigins IP)
4. `npm install` (526 pkg) + `npm run build` → PASS, semua route static
5. `cp -r .next/static .next/standalone/.next/static` + `cp -r public .next/standalone/public`
   (Next 16 standalone TIDAK auto-copy static/public — wajib manual)
6. `sudo chown -R www:www .` → start service → verifikasi:
   - `127.0.0.1:3000/` & `wasnaker.lan/` → 200, title "NextAdmin - Next.js Dashboard Kit"
   - rute `/tables/basic-tables`, `/ui-elements/buttons`, `/charts/bar-charts`, `/form-elements` → 200
7. nginx: tambah `proxy_cache off;` + purge cache + reload (lihat §2)
8. Git: commit `chore: enable standalone output and sync lockfile`
   (identity repo-local: `laravelspine <laravelspine@users.noreply.github.com>`)

## 4. Catatan kode

- Lint: `npm run lint` → 7 error + 9 warning, SEMUA pre-existing di kode upstream NextAdmin
  (`src/hooks/use-media-query.ts` setState-in-effect, `src/types/tanstack-table.d.ts` unused vars).
  Tidak disentuh.
- Deps NextAdmin sudah punya: `@tanstack/react-query`, `@tanstack/react-table`, `react-aria-components`,
  `tailwind-merge`, dll. Jangan tambah dep baru kalau sudah ada.
- `nextadmin.lan` (clone lokal /www/wwwroot/nextadmin) = reference native, JANGAN diubah.

## 5. Pola nextjs-spine yang sudah dibaca (referensi Langkah 2)

- `lib/api.ts` — fetch wrapper tipis: Bearer dari `localStorage("spine_token")`, `ApiResult<T>{ok,status,data,error}`, `API_URL` env
- `lib/use-pagination-limit.ts` — GET `/api/v1/settings/tables_pagination_limit` (default 10, 404=default)
- `lib/module-extensions.ts` — `useModuleExtensions()` → `/api/v1/modules/extensions` → `{menu,widgets,detail_tabs}`, refetch saat token berubah
- `lib/small-table.tsx` — SmallTable: tabel kiri `lg:w-5/12` + panel detail `lg:w-7/12`, kolom non-primary hidden
  saat mode kecil, hash `#id` di-set di PAGE (klik baris, bukan saat load), header `STATUS|#ID|TITLE` via `renderHeader`,
  toolbar, search client-side `getSearchText`, pagination `perPage` setting, semantic classes `small-table-*`
- `lib/master-detail.tsx` — TabContent: array→tabel+badge status, objek→vertical dl; `hideKeys`/`customValue`/`inlineData`
  (overview tanpa fetch); cache SWR manual `Map` + `refreshKey` di cache key; `TabSkeleton` shimmer
- `lib/ui.tsx` — `cx()` + Button/Input/Card/Badge/PageHeader, semua pakai design tokens spine
- `app/sample/page.tsx` — pola wiring halaman modul (load list → select hash → toolbar → refreshKey)

## 6. Arsitektur wasnaker-core (konteks dari user)

- `wasnaker-core` = Laravel TIPIS (thin consumer), bukan monolit. Isinya nanti makin
  sedikit karena Spine jadi dependency eksternal.
- SAAT INI composer.json core: `require spine/laravel-spine: @dev` via **path repository**
  → `/www/wwwroot/laravelspine/public_html` (vendor/spine/laravel-spine = symlink), dan
  `wasnaker/sales-module: @dev` via path `../wasnaker-sales-module` (symlink).
- RENCANA: ganti path repo → `require` dari **https://github.com/laravelspine/laravelspine**
  (VCS repo). `/www/wwwroot/laravelspine` = working dir package (isi: modules/, public_html/,
  git-credential-laravelspine helper).
- `Modules/` di wasnaker-core kosong (module aktif di-flag via modules_statuses.json).

## 7. Langkah 2 — SELESAI (sesi ini)

Adapter Spine di NextAdmin sudah dibangun + diverifikasi E2E (playwright):

**File baru (7):**
- `src/services/spine/api.ts` — fetch wrapper (Bearer `spine_token`, `ApiResult{ok,status,data,error}`, API_URL env, default same-origin; catch jaringan)
- `src/services/spine/use-pagination-limit.ts` — baca setting, gate token (PENTING: tanpa gate → 401 pre-login ke-cache → pageSize stuck)
- `src/services/spine/module-extensions.ts` — `useModuleExtensions()` + types `DetailTab/ModuleExtensions`, token di query key
- `src/components/spine/status-badge.tsx` — map status → Badge color (done/active→success, in_progress/pending→warning, cancelled→error, fallback gray)
- `src/components/spine/tab-content.tsx` — TabContent (React Query cache per URL + refreshKey di key; skeleton; inlineData; hideKeys/customValue; array→tabel+badge, objek→dl)
- `src/components/spine/small-table.tsx` — SmallTable TanStack Table (mode kecil 5/12+7/12 via kolom primary, search client-side, pagination controlled + sync pageSize, semantic classes `small-table-*`)
- `src/app/(with-layouts)/sample/page.tsx` — demo: login inline (demo@spine.test) → list → toolbar (Mark as done/Edit/PDF/Toggle) → dialog edit

**TAMBAHAN sesi (setelah E2E):**
- `src/components/spine/login-card.tsx` — LoginCard dipakai sample + settings (extract, hindari duplikasi)
- `src/app/(with-layouts)/settings/page.tsx` — halaman Settings schema-driven (port nextjs-spine):
  GET schema → nav tab kiri + form kanan; POST bulk → nilai; PUT per key → simpan.
  Input UNCONTROLLED + remount via key (tanpa state-sync effect). Checkbox baca state dari
  DOM saat save (RAC checkbox tak ikut FormData saat unchecked). Field action baca from_key
  dari FormData form. Native select (ponytail: ganti Select RAC kalau butuh a11y penuh).

**Pitfall settings:** PUT per field ~0.6s (server sync) → 5 field ≈ 3.5s sequential. Bukan bug —
  tunggu cukup lama di E2E. `qc.invalidateQueries(["spine","settings-bulk"])` setelah simpan.

**GELOMBANG KEDUA (setelah sesi lanjutan): auth global + home + menu**
- `src/services/spine/auth-context.tsx` — AuthProvider/useAuth: token state (initializer dari
  localStorage, BUKAN effect — hindari set-state-in-effect), validasi /auth/me saat mount
  (setState hanya di async path), signIn/logout. Di-mount di `src/app/providers.tsx`.
- `src/app/login/page.tsx` — halaman login BARE (root layout, tanpa shell); sudah login → redirect "/".
- `src/app/(with-layouts)/(dashboard)/(home)/page.tsx` — halaman depan Spine-aware:
  belum login → CTA /login; login → sambutan (nama dari /auth/me) + kartu modul (menu extensions)
  + Settings. Home lama (mock e-commerce NextAdmin) DIGANTI.
- `src/components/common/sidebar/index.tsx` — section MODULES dinamis saat login (menu extensions,
  NavItem per modul + Settings). data.tsx tidak diubah (menu demo NextAdmin tetap utk dev).
- `src/components/common/header/user-profile.tsx` — user asli (nama/email /auth/me), logout wired,
  belum login → tombol "Masuk" → /login. Avatar fallback initial.
- sample/settings page: LoginCard inline DIGANTI redirect effect → `/login` saat !token.
  LoginCard kini cuma dipakai /login; onSuccess meneruskan token (setToken dipindah ke signIn).
- LoginCard tidak set token sendiri lagi (AuthProvider.signIn yang set + validasi).

**Catatan:** 404 `/sample-tasks` di console = Next prefetch Link sidebar; halaman frontend
  sample-tasks belum ada (hilang saat Langkah 3). E2E pakai waitUntil domcontentloaded
  (networkidle kadang hang di root /login).

**Delta keputusan vs nextjs-spine:** React Query ganti Map SWR; TanStack Table ganti tabel manual; tokens NextAdmin (`text-text-*`, `bg-card-*`, `border-border-*`); API_URL same-origin (produksi) / `http://spine.lan` di `.env.local` (dev, gitignored).

**Pitfall NextAdmin:** Button pakai `isDisabled` (React Aria), bukan `disabled`; props `title` nggak diterima. Query api yang butuh auth WAJIB di-gate `enabled: Boolean(token)` — kalau tidak, error 401 ke-cache permanen.

**Verifikasi:** `node /tmp/hermes-verify-sample.js` (playwright, NODE_PATH ke node_modules proyek): login→rows 25 (settings)→search→klik baris→hash #id→3 tab→konten tab, errors=0. Script tetap di /tmp (hermes-verify-*).

## 9. Dashboard widgets DnD — kontrak SPINE (backend) SELESAI

Ground truth legacy: `app.ciptamasjaya.co.id/application/views/admin/dashboard/{dashboard,dashboard_js}.php`
+ `widgets/{calendar,user_data}.php` — pola: jQuery UI sortable connectWith antar 8 area statis
(top-12/middle-left-6/middle-right-6/left-8/right-4/bottom-left-4/bottom-middle-4/bottom-right-4),
handle `.widget-dragger`, widget root `#widget-{id}` + `data-name`, save STATE PENUH per drop
(area kosong = sentinel `'empty'`), visibility checkbox per widget + reset.

KEPUTUSAN: kontrak hidup di SPINE (backend), frontend tinggal adopsi. Opsi A disetujui
(satu baris JSON per user, bukan tabel normal). DIKERJAKAN & TER-PUSH:
- Repo `laravelspine/laravelspine` commit `350530c` (main):
  - migration `user_dashboard_states` (user_id unique, layout json, visibility json)
  - `src/Models/UserDashboardState.php` (casts array)
  - `ModuleService::widgets()` — agregat widget dari manifest modul aktif (dipakai
    extensions() + validasi state) — extensions() di-refactor ke method ini
  - `DashboardController` — GET/PUT order/PUT visibility/POST reset
  - routes: `GET /api/v1/dashboard`, `PUT /api/v1/dashboard/order`,
    `PUT /api/v1/dashboard/visibility`, `POST /api/v1/dashboard/reset`
- KONTRAK: layout `{area: [widgetId,...] | 'empty'}` (server normalisasi 'empty'→[]);
  id widget DIVALIDASI ke registry extensions (siluman → 422); visibility `{widgetId: bool}`;
  GET null = belum diatur (frontend pakai default manifest).
- Migrasi dijalankan di spine.lan (php 8.4: `/www/server/php/84/bin/php artisan migrate`);
  tes E2E curl PASS (save/422/reset/extensions regression OK).

BELUM dikerjakan (NextAdmin side, sesi depan): render widget dari `extensions.widgets`
per area + DnD (@dnd-kit/react sudah di deps) + konsumsi state endpoint di atas.

**SEMANTIK MERGE (dari `application/helpers/widgets_helper.php` — ground truth):**
- id widget legacy = nama file view (`create_widget_id()`), container default per widget
  dari registrasi; state user `dashboard_widgets_order` + `dashboard_widgets_visibility`
  disimpan per user (meta).
- Render per area: (a) state ada → render id sesuai urutan state utk area itu
  (skip yg sudah tidak terdaftar); (b) FALLBACK → widget TERDAFTAR yang tidak
  ditempatkan di area state manapun dirender di container DEFAULT-nya (urut
  registrasi/manifest) — widget baru otomatis muncul di area default sampai dipindah;
  (c) belum ada state → semua di container default.
- Visibility: `{id, visible}` — visible=0 → disembunyikan (legacy: class `hide` server-side).
- Container kosong permanen hanya terjadi kalau semua widget-nya "applied" di area lain.
- Merge INI harus diimplementasikan FRONTEND (Spine GET /dashboard hanya state mentah;
  katalog + area default dari /modules/extensions).

## 10. Langkah berikutnya (Langkah 3 roadmap — KOREKSI PRIORITAS)

**Kerangka dashboard widget (infrastruktur) DULUAN, modul bisnis belakangan** —
widget Quotations tidak bisa berfungsi tanpa kerangka widgetnya; modul = layer
paling atas. Roadmap §4 sekarang: kerangka widget (registry React + grid area
frontend `top-12/left-8/right-4` + merge render + DnD @dnd-kit + dropzone/
preview-area pola legacy + visibility). Backend dashboard Spine sudah final —
area layout bebas, frontend define grid; area default per widget dari manifest
(`extensions.widgets`). Uji kerangka pakai widget Sample yang sudah terdaftar.
Modul pertama (setelah kerangka): Quotations — scaffold + ground truth legacy
seperti tercantum di roadmap §5.

## 11. KERANGKA DASHBOARD WIDGET — SELESAI (commit `702fe1a` frontend)

Perluasan sesi ini (commit `7ae8cbe`): grid = 8 area base legacy + area
EFEKTIF dinamis = base + default-area widget katalog modul + area di layout
user (append di bawah). Lebar kolom dari suffix id (`areaSpan`): -12/-8/-6/
-4/-3/-2 → col-span (3/4/6 kolom = akhiran -4/-3/-2). Self-check 22 assert,
E2E 14/14. KEPUTUSAN: posisi area custom append bawah dulu; sisip blok
tengah (middle-x3) ditunda sampai modul produksi butuh.

Infrastruktur widget live di `/www/wwwroot/wasnaker.lan/wasnaker-frontend`
(dashboard halaman home), verifikasi E2E Playwright 14/14 PASS (render
default per area → DnD antar-area → PUT state penuh → persist reload →
visibility hide/unhide → preview area → reset → 0 console error).
File & detail pola: lihat roadmap §4 (sudah di-annotasi path per item).

Catatan penting (agar tidak terulang):
- react-query optimistic update (onMutate/onSuccess/rollback) HARUS pakai
  key exact `["spine","dashboard",token]` — prefix tanpa token TIDAK kena.
- @dnd-kit/react v0.5 = API BARU: `DragDropProvider` + `useSortable` dari
  `@dnd-kit/react/sortable` (bukan DndContext/useSortable lama). Docs pola:
  item `useSortable({id,index,group,type:'item',accept:'item'})`, kolom
  `useDroppable` priority Low. Plugin OptimisticSorting menggeser DOM &
  update `source.index/group` saat drag-over; update state React cukup di
  onDragEnd (cancel = plugin revert DOM sendiri). Drop ke kolom KOSONG =
  target non-sortable `type:'column'` → append akhir (plugin skip).
  `@dnd-kit/helpers` (helper `move`) TIDAK terpasang → manual.
- Widget hidden TETAP dirender (`hidden` attr) supaya posisinya di layout
  tidak hilang (paritas legacy class hide). Konsekuensi: tombol eye di kartu
  hidden tak terjangkau → panel "Widgets" (checkbox) wajib ada.
- Self-check merge: `npx tsc src/components/dashboard/dashboard-merge.ts
  --outDir /tmp/x --module esnext ...` lalu `node /tmp/x/dashboard-merge.js`
  (guard `argv[1].endsWith("dashboard-merge.js")` — endsWith tanpa ".js"
  GAGAL karena suffix file .js).
- E2E idempotent: mulai dengan klik Reset dashboard (state user demo bisa
  menyisakan layout/visibility dari run sebelumnya).

Deploy ulang selalu: stop service → build → copy static/public ke standalone → chown www:www → start.
