# Porting — Detail Panel Master-Detail (list + panel kanan bertab)

Status: **helper induk SELESAI** (1 Sep 2026) — `lib/master-detail.tsx` + kontrak `detail_tabs` di manifest + endpoint per-item
Sumber pola: legacy `application/views/admin/clients/` + `application/libraries/App_tabs.php`
Target: halaman module (contoh: Sample) — list item di kiri, klik → panel kanan dengan tabs

## Pola legacy (referensi)

| File legacy | Peran |
|---|---|
| `views/admin/clients/manage.php` | List item (DataTables), link ke detail |
| `controllers/admin/Clients.php` | `$customer_tabs = get_customer_profile_tabs($id)`; `$tab = $customer_tabs[$group] ?? null` |
| `views/admin/clients/client.php` | Detail: header (nama + aksi) → `load('tabs')` (nav) → `load($tab['view'])` (konten) |
| `views/admin/clients/tabs.php` | Nav tab dari `$customer_tabs`, link `?group=$key`, icon + badge |
| `libraries/App_tabs.php` | `add_customer_profile_tab($slug, $tab)` — modul menambah tab |
| `helpers/clients_helper.php` | `filter_client_visible_tabs()` — visibility dari settings + badge per item |

## Kontrak tab detail (dari App_tabs::add)

```php
$tab = [
    'slug'     => 'profile',              // required, unique
    'name'     => 'Profile',              // required
    'icon'     => 'fa fa-user',           // icon class
    'view'     => 'admin/clients/groups/profile',  // view file = konten tab
    'position' => 10,                     // urutan nav
    'badge'    => ['value' => 5, 'type' => 'info', 'color' => '#hex'],  // opsional, per-item
];
```

Modul menambah tab: `app_tabs->add_customer_profile_tab($slug, $tab)` → `$this->add($slug, $tab, 'customer_profile')`.
Contoh tab bawaan client: profile, contacts, invoices, estimates, payments, projects, proposals, contracts, expenses, vault, etc.

## Pemetaan ke Spine (rencana)

### Backend — SELESAI
- Kontrak manifest modul `detail_tabs` (opsional) — sudah diimplementasikan:
```php
'detail_tabs' => [
    [
        'slug'     => 'overview',
        'label'    => 'Overview',
        'icon'     => '👁️',
        'api'      => '/api/v1/sample/{id}/overview',   // data konten tab
        'position' => 10,
    ],
],
```
- `extensions()` di ModuleController menyertakan `detail_tabs` per modul (key = lowercase nama modul) — satu request untuk menu + widgets + detail_tabs.

### Frontend (nextjs-spine) — SELESAI (helper induk)
- `lib/master-detail.tsx`: komponen `MasterDetail` generik — list kiri + panel kanan bertab; konten tab di-fetch dari `tab.api` (placeholder `{id}` diganti id item); dipakai semua modul tanpa perulangan.
- Halaman modul tinggal: fetch list + `<MasterDetail items={items} tabs={detail_tabs["<modul>"]} />`.
- Contoh terpasang: `/sample` (tab overview → GET /sample/{id}, tab activity → GET /sample/{id}/activity-logs).

## Catatan keputusan
- `badge` (per-item) di-skip dulu — tambah saat ada kebutuhan nyata (YAGNI).
- Tab konten = data dari `tab.api` (API-driven), bukan komponen React per modul (sama seperti keputusan settings fields generic).
- Visibilitas tab per-role/setting: tunda — sama seperti filter_client_visible_tabs, butuh konsep role dulu.

## File terkait
- Sample module manifest: `<path-to-modules>/boilerplates/Sample/manifest.php`
- Halaman Sample saat ini: `app/sample/page.tsx` (list + form create — belum ada detail panel)
