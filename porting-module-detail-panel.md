# Porting — Detail Panel Master-Detail (list + panel kanan bertab)

Status: **KOREKSI POLA** (1 Sep 2026) — pola modul bisnis = DataTable + halaman detail full-width (quotations), BUKAN split panel kiri-kanan (clients)
Sumber pola: legacy `modules/quotations/` (modul bisnis) — `manage_table.php` + `quotation.php`
Target: halaman module (contoh: Sample) — DataTable item, klik → detail full-width

## KOREKSI (baca modul quotations sebagai ground truth)

Pola yang BENAR untuk modul bisnis (quotations, inspections, billings, licences):
- **List**: `manage_table.php` = DataTable penuh full-width (`render_datatable`) + tombol `toggle_small_view` (toggle tampilan, bukan split panel)
- **Detail**: klik baris → halaman terpisah (`view_quotation/$id` → `quotation.php`) full-width (`col-md-12`): header info (col-md-6 + col-md-6) + tabel item (`_add_edit_items`) + total (`bottom-transaction`)
- TIDAK ADA tabs di detail quotation — detail full-width dengan kolom informasi

Pola clients (list kiri + panel kanan bertab via `tabs.php`) = pola untuk **entity dengan banyak tab relasi** (contacts/invoices/projects), bukan pola default modul.

## Implementasi di Spine (sesuai koreksi)

- `/sample`: DataTable item (ID, Nama, Dibuat) — TANPA form create di atasnya
- Klik baris → detail full-width (bukan panel kanan) — meniru `quotation.php`
- Helper `MasterDetail` (list kiri + panel kanan) → JANGAN dipakai untuk modul; cadangan untuk entity bertab banyak bila dibutuhkan

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

## Pemetaan ke Spine (sesuai koreksi pola)

### Backend — SELESAI (kontrak tetap valid)
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
- Kontrak `detail_tabs` tetap berguna untuk **halaman detail full-width** (padanan section `_add_edit_items` / kolom info quotation.php) — tab opsional, bukan keharusan.

### Frontend (nextjs-spine)
- `/sample`: **DataTable** item (ID, Nama, Dibuat) — tanpa form create di atas (padanan manage_table.php) — SELESAI
- Klik baris → detail **full-width** (bukan panel kanan) — mengikuti quotation.php — BELUM
- `lib/master-detail.tsx` (list kiri + panel kanan bertab): **cadangan**, hanya untuk entity bertab banyak bila dibutuhkan — JANGAN dipakai modul bisnis

## Catatan keputusan
- Pola modul bisnis = **DataTable + detail full-width** (quotations sebagai ground truth).
- `badge` (per-item) di-skip dulu — tambah saat ada kebutuhan nyata (YAGNI).
- Visibilitas tab per-role/setting: tunda — butuh konsep role dulu.

## File terkait
- Sample module manifest: `<path-to-modules>/boilerplates/Sample/manifest.php`
- Halaman Sample saat ini: `app/sample/page.tsx` (DataTable — detail full-width menyusul)
- Referensi legacy: `<path-to-app>/modules/quotations/views/admin/quotations/manage_table.php` + `quotation.php`
