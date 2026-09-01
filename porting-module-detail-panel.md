# Porting — Detail Panel Master-Detail (list + panel kanan bertab)

Status: **tercatat, belum diimplementasikan** (1 Sep 2026)
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

### Backend
- Perluas kontrak manifest modul dengan `detail_tabs` (opsional):
```php
'detail_tabs' => [
    [
        'slug'     => 'overview',
        'label'    => 'Overview',
        'icon'     => 'eye',
        'api'      => '/api/v1/sample/{id}/overview',   // data konten tab
        'position' => 10,
    ],
    [
        'slug'     => 'activity',
        'label'    => 'Activity',
        'icon'     => 'clock',
        'api'      => '/api/v1/sample/{id}/activity-logs',
        'position' => 20,
    ],
],
```
- Endpoint baru (kalau perlu): `GET /api/v1/{resource}/{id}/tabs` → tab yang berlaku untuk item tsb + badge (padanan get_customer_profile_tabs + filter_client_visible_tabs).

### Frontend (nextjs-spine)
- Halaman module list (kiri) → klik item → panel kanan muncul (URL `?id=N` atau `/module/N`).
- Panel kanan: header item + nav tabs (dari kontrak) + konten tab (fetch `tab.api`).
- Komponen generik di `lib/` (padanan `render_dashboard_widgets` — render apa yang dikirim kontrak).

## Catatan keputusan
- `badge` (per-item) di-skip dulu — tambah saat ada kebutuhan nyata (YAGNI).
- Tab konten = data dari `tab.api` (API-driven), bukan komponen React per modul (sama seperti keputusan settings fields generic).
- Visibilitas tab per-role/setting: tunda — sama seperti filter_client_visible_tabs, butuh konsep role dulu.

## File terkait
- Sample module manifest: `/www/wwwroot/laravelspine/modules/boilerplates/Sample/manifest.php`
- Halaman Sample saat ini: `app/sample/page.tsx` (list + form create — belum ada detail panel)
