# Resume Sesi — 2 Sep 2026

Ringkasan semua pekerjaan yang diselesaikan. Berlaku untuk repo:
`laravelspine/spine` (package), `laravelspine/boilerplates` (modul Sample),
`laravelspine/sampletasks` (modul SampleTasks), `laravelspine/nextjs-spine` (frontend),
`wasnaker-porting-docs` (docs).

---

## 1. Backend — Generic Entity Lifecycle Hooks (pengganti 100+ hook legacy)

**Masalah**: legacy punya 100+ hook per entity (`after_contract_added`,
`after_estimate_updated`, dst — 59 jenis entity). Tidak scalable.

**Solusi**: 6 event generic + trait, entityType sebagai parameter.

- `Spine\Events\EntityCreating` — sebelum create; `entityType`, `attributes`, `prevent()`
- `Spine\Events\EntityCreated` — setelah create
- `Spine\Events\EntityUpdating` — sebelum update; `changes` (diff old→new), `prevent()`
- `Spine\Events\EntityUpdated` — setelah update; `changes`
- `Spine\Events\EntityDeleting` / `EntityDeleted`
- `Spine\Traits\HasLifecycleHooks` — dipakai model → auto-dispatch event via Eloquent model events

**Listener** (modul):
```php
Event::listen(EntityUpdated::class, fn ($e) => /* filter $e->entityType */);
```

**Status-change pattern** (padanan `estimate_accepted`, `task_status_changed`):
`EntityUpdated` + `changes['status']` — tidak perlu event terpisah untuk 90% kasus.

Catatan pitfall: `Collection::where('done')` = where key, bukan nilai → pakai
`filter(fn)`.

## 2. Modul SampleTasks (child module dari Sample)

- Entity `SampleTask`: `belongsTo SampleItem`, ulid, status (pending/in_progress/done)
- Konstanta status di model (`STATUSES` + `STATUS_LABELS`) — source of truth
- `LogTaskActivity` listener: created/updated/deleted + `task.status_changed`
- Manifest: menu `/sample-tasks`, widget, detail_tabs (overview + activity)
- `extend_detail_tabs` → tambah tab "Tasks" ke detail Sample (lintas modul)
- Activity log: `activityLogs()` query polymorphic subject

## 3. Hook lintas modul

- **`extend_detail_tabs`** (manifest): modul lain menambah tab ke detail modul
  target. Di-merge di `ModuleController::extensions()`. Padanan
  `add_customer_profile_tab` legacy.
- **`SyncSampleStatusFromTasks`** (di modul Sample): listen event SampleTask →
  semua child done → parent SampleItem ikut done. Guard `class_exists` supaya
  Sample tetap jalan tanpa SampleTasks ter-install.

## 4. ulid + status (bukan uuid)

- `HasUlids` bawaan Laravel + **override `uniqueIds()` → `['ulid']`** (default
  HasUlids mengisi PRIMARY KEY — bug yang ditemukan)
- Migration tambah kolom `ulid` (26 char, unique) + `status` (default draft)
- Backfill semua record lama

## 5. Scaffold: module:make-spine + entity:make-spine

- `SpineScaffoldCommand` (base): replacements + copyTree, stubs di
  `src/Console/stubs/` (9 template)
- `module:make-spine Blog` — modul lengkap (manifest + routes + hooks + ulid + status)
  - `--entity=SampleItem` — override entity (kasus Sample → SampleItem)
  - Entity default = `Str::singular(nama modul)`
- `entity:make-spine Branch --module=Customers --parent=Customer` — entity
  tambahan di modul existing:
  - `--parent=` (Pola B child): FK `parent_id` + belongsTo + filter `?parent_id`
  - Tanpa `--parent` (Pola A referensi): entity mandiri
  - **APPEND** routes (sibling level, bukan nested) + provider listener — idempoten
  - Manifest TIDAK disentuh (frontend contract di-review manual)
- Pola relasi: A = FK di entity utama (manual), B = FK di entity baru (scaffold)

## 6. Frontend — SmallTable helper + semantic class names

`lib/small-table.tsx` — helper generik list + panel detail bertab (dipakai SEMUA modul):

- Semantic classes: `small-table`, `small-table-list`, `small-table-list-row`,
  `small-table-list-row--selected`, `small-table-detail`, `small-table-detail-header`,
  `small-table-toolbar`, `small-table-tabs`, `small-table-search`, `small-table-pagination`
- Mode kecil (padanan `toggle_small_view`): tabel 5/12 + panel 7/12, kolom
  non-primary hidden
- Hash `#id` di URL — hanya saat KLIK baris (bukan saat load)
- Toolbar: Mark as {STATUS} dropdown, Edit, PDF, Toggle small view
- Search (client-side) via `getSearchText` — sample: name+description; tasks: title+parent name
- Pagination: `usePaginationLimit()` baca setting `tables_pagination_limit` (default 10)

## 7. Frontend — TabContent (render tab generik)

`lib/master-detail.tsx`:

- **Array → tabel** (tasks, activity) dengan status pill badge
- **Objek tunggal → vertical dl** (overview: label kiri, value kanan)
- `hideKeys` (sembunyikan ulid/title) + `customValue` (parent title)
- `inlineData` → overview render dari data list yang SUDAH ada di client
  (tanpa fetch, tanpa "Memuat..." saat pindah record — padanan legacy smooth)
- **SWR cache** per URL (`tabCache` Map, refreshKey busts cache) + **skeleton**
  shimmer (pengganti teks "Memuat...") — berlaku semua tab ajax

## 8. Review fixes (berlaku kedua module)

- ulid tidak ditampilkan di UI (sistem-only)
- Header panel: **STATUS | #ID | TITLE**
- Parent ditampilkan sebagai **title** (bukan id/key)
- Title entity tidak diulang di overview (sudah di header) — kecuali parent title
- `update()` validasi menerima `sample_item_id` (fix: edit parent dari UI dibuang backend)

## 9. Deploy & konvensi teknis

- Build: stop service → `npm run build` → start (hindari race .next)
- Cache nginx: `proxy_cache off` di vhost spine.lan (cache HTML lama bikin verifikasi salah)
- Commit message WAJIB bahasa Inggris; jangan commit hostname .lan / path internal
- Sync modul boilerplates → konsumen: `sudo cp` + `chown www:www`
- Install modul: zip → multipart upload API `/api/v1/modules/install`

## Status akhir

- Semua ter-push ke GitHub (4 repo) + live di spine.lan
- PHPUnit belum dipasang (keputusan sesi) — verifikasi via skrip ad-hoc
- Next steps: porting modul legacy (inspections, licences, quotations...), evaluasi
  scaffold dengan modul nyata multi-entity (Equipments, Customers)
