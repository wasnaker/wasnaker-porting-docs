# Analisis Hooks PerfexCRM — Implementasi untuk Backend Laravel API-Only

Dokumen ini menganalisis sistem **hook** di PerfexCRM dan bagaimana implementasinya
di project backend **Laravel API-only** (`wasnaker.lan`).

## Poin Penting: Ada DUA Mekanisme "Hook" di Perfex

Perlu dibedakan karena keduanya sering tertukar:

1. **CodeIgniter Bootstrap Hooks** — `application/hooks/` + `application/config/hooks.php`
   Berjalan saat request dimulai (bootstrapping aplikasi).
2. **Action/Filter Hook System** — `hooks()->add_action()`, `add_filter()`, `do_action()`,
   `apply_filters()`. Sistem ekstensi ala WordPress (berbasis package `bainternet/php-hooks`).
   Dipakai di **155 file** core → ini yang sesungguhnya jadi "extension point" Perfex.

---

## Bagian A — Bootstrap Hooks (`application/hooks/`)

Dideklarasikan di `application/config/hooks.php`:

| Hook | Peran | Implementasi Laravel |
|------|-------|----------------------|
| `EnhanceSecurity::protect()` | Blokir bot/UA/referrer/IP buruk (list eksternal, cache 1 hari) | **Middleware** `BlockBadRequest` + WAF. Laravel punya middleware + throttle. List buruk bisa ditaruh di config/cache (Redis). |
| `App_Autoloader::register()` | Autoload class App_*/module (spl_autoload_register) | **Composer autoload + PSR-4** (native). Tidak perlu diadopsi. |
| `InitModules::handle()` | Load modul aktif + gabung `csrf_exclude_uris` | **Module Service Provider + Bootstrap** (`ModuleServiceProvider::boot`, `routes/api.php`). CSRF exclude → middleware `VerifyCsrfToken` (tetap default untuk API). |
| `InitHook::_app_init()` | Load library awal + jalankan action `modules_loaded`, `admin_init`, dsb | **AppServiceProvider / ModuleServiceProvider** `boot()` + proses registrasi. |

> **Kesimpulan A:** Bootstrap hook adalah mekanisme **startup** khas framework lama.
> Di Laravel digantikan **Service Provider + Middleware + Composer autoload** — native,
> tidak perlu sistem hook tersendiri.

---

## Bagian B — Action/Filter Hook System (yang REAL penting)

### Cara kerja di Perfex
- `hooks()->add_action('nama', callable, priority)` — daftarkan fungsi saat event.
- `hooks()->do_action('nama', args)` — jalankan semua fungsi yang terdaftar.
- `hooks()->add_filter('nama', callable, priority)` — daftarkan fungsi modifikasi data.
- `hooks()->apply_filters('nama', $value, ...args)` — jalankan fungsi, value jadi dimodifikasi.

### Fungsi inti
- **Ekstensibilitas** — modul/tema menambahkan perilaku tanpa mengubah core.
- **Loose coupling** — core memicu event; modul merespons.
- **Kustomisasi** — modifikasi data lewat filter.

---

## Bagian C — Pemetaan ke Laravel API-Only

Laravel **sudah punya sistem hook setara** secara native. Berikut pemetaannya:

### 1. `do_action` (jalankan aksi — tidak kembalikan data) → **Laravel Events**

| Perfex | Laravel |
|--------|---------|
| `hooks()->do_action('invoice_added', $id)` | `event(new InvoiceCreated($invoice))` |
| `hooks()->add_action('invoice_added', 'SomeClass@method', 10)` | *listener* di `EventServiceProvider` / `#[Listener]` |

Contoh pemetaan action Perfex → Event Laravel:

| Action Perfex | Event Laravel |
|---------------|---------------|
| `modules_loaded` | `ModulesLoaded` / `app()->booted()` |
| `admin_init` | `ServiceProvider::boot()` |
| `before_update_database` | `MigrationStarted` / `artisan migrate` hook |
| `database_updated` | `Migrated` |
| `new_ticket_...`, `ticket_..._loaded` | `TicketCreated`, `TicketReplied` |
| `app_init_admin_sidebar_menu_items` | registrasi di module's `boot()` |

### 2. `apply_filters` (modifikasi data) → **Laravel Events (returns) / Pipeline / Macros / Listeners**

Laravel tidak punya *filter* persis seperti WordPress. Opsi terbaik:

| Pola | Deskripsi |
|------|-----------|
| **Event + Listener mengubah objek** | Listener menerima objek & mengubah properti (paling mudah, setara filter) |
| **Middleware / Pipeline (`Illuminate\Pipeline`)** | Rantai transform data, cocok untuk filter bernilai kembalian |
| **Macros** (`Macroable`) | Menambah method dinamis → setara customisasi |
| **Higher Order / Decorators** | Membungkus perilaku asli |

Contoh konversi filter:
```php
// Perfex
$value = hooks()->apply_filters('before_update_invoice_item', $value, $item_id);

// Laravel
$event = new UpdatingInvoiceItem($value, $itemId);
event($event);                       // listeners bisa ubah $event->value
$value = $event->value;
```

### 3. Fitur ekstensi Perfex lain → padanan Laravel

| Fitur Perfex | Padanan Laravel |
|--------------|-----------------|
| Merging menu/tabs/sidebar (`app_menu`, `app_tabs`) | **API: frontend/client** mengelola menu — tidak di backend. Bila perlu: module expose endpoint/`MenuService`. |
| Register merge fields | **Blade + Mailable data** (template) |
| Variabel global `hooks()` | **Event dispatcher `Illuminate\Events\Dispatcher`** (`Event::dispatch`) |
| Hook prioritas (priority) | Laravel listener urutan keberdaftaran; untuk kontrol lebih → Pipeline |

---

## Bagian D — Strategi untuk Project Kita (API-Only & Modular)

### Rekomendasi utama: **pakai Laravel Events + EventServiceProvider per module**

Karena project **modular**, setiap module mendaftarkan **event & listener-nya sendiri**
di `modules/<modul>/Providers/EventServiceProvider.php`.

```text
modules/
├── Sales/
│   ├── Events/
│   │   ├── InvoiceCreated.php
│   │   └── PaymentRecorded.php
│   ├── Listeners/
│   │   ├── SendInvoiceEmail.php
│   │   └── SyncAccountLedger.php
│   └── Providers/
│       └── EventServiceProvider.php   # register events + listeners modul ini
└── Project/
    ├── Events/
    │   └── TaskStatusChanged.php
    └── Listeners/
        └── NotifyProjectMember.php
```

### Aturan implementasi

1. **Tidak perlu sistem hooks kustom** — Laravel Events sudah cukup & idiomatis.
2. Perancangan **event per domain** dilakukan saat memindahkan tiap modul
   (dari daftar `do_action`/`apply_filters` yang ada di code Perfex tiap modul).
3. Event LARANG dipakai untuk control-flow yang kompleks antar modul → gunakan
   **Jobs/Queue** + **interface** bila butuh kepastian urutan.
4. Untuk kebutuhan font-extension point di level API (mis. webhook keluar / plugin),
   cukup siapkan **WebhookOutService** + queue, dan **API hook-out** — bukan hook internal.
5. Bootstrap hooks lama (`EnhanceSecurity`, `InitModules`, `InitHook`) →
   **Middleware + ServiceProvider** (native), tidak perlu adopsi.

### Contoh konkret migrasi hook Perfex → Laravel

| Hook Perfex (contoh di code) | Implementasi Laravel |
|------------------------------|----------------------|
| `hooks()->do_action('invoice_created', $id)` | `event(new InvoiceCreated($invoice))` → listener kirim email |
| `hooks()->apply_filters('invoice_status_changed', ...)` | Event `InvoiceStatusChanged` + listener ubah data |
| `hooks()->do_action('lead_converted_to_customer')` | `LeadConvertedToCustomer` → listener buat customer default |
| `hooks()->add_filter('before_send_ticket_reply', ...)` | Middleware/Pipeline pada service `TicketService::reply()` |

---

## Kesimpulan

- **Bootstrap hooks** (`application/hooks/`) → digantikan **Service Provider + Middleware +
  Composer autoload** Laravel (native). Tidak diadopsi ulang.
- **Action/Filter hooks** (`hooks()->*`) → dipetakan ke **Laravel Events** (`do_action`) dan
  **Pipeline/decorator/event-mutation** (`apply_filters`).
- Tidak perlu membangun ulang sistem hooks khas WordPress di Laravel; gunakan kemudahan
  `Event::dispatch` + per-module `EventServiceProvider`.
- Saat memindahkan tiap modul, **inventarisasi** `do_action`/`apply_filters` dalam code
  Perfex modul tsb → konversi menjadi Event/Listener di module Laravel.

---

*Dokumen dibuat berdasarkan inspeksi `application/hooks/`, `application/config/hooks.php`,
`application/third_party/action_hooks.php`, dan `application/helpers/core_hooks_helper.php`,
27 Agustus 2026.*
---

## Lampiran A — Inventaris Hook app.ciptamasjaya.co.id (ground truth, 31 Agustus 2026)

Inventaris diambil dari **`application/` saja (core Perfex kustom) — hook dari `modules/` TIDAK dibaca** (hook kustom bisnis licence/inspection/schedule milik module, di-port bersama modulnya nanti).

| Kategori | Jumlah | Keputusan porting |
|----------|--------|-------------------|
| BACKEND (event) | 195 | → **Laravel Events** di package Spine (`src/Events/`) atau modul |
| FRONTEND (view/UI) | 160 | → skip (frontend Next.js; API tidak render HTML) |
| INFRA (lifecycle) | 35 | → ServiceProvider / Middleware / native Laravel |
| **Total** | **390** | |

> Sumber: `grep -rhoE "do_action('[^']+'" application/` — 390 hook unik (sebelumnya 526 termasuk module).


### 1. BACKEND hooks → Laravel Events (195)

Ini hook yang **harus tersedia sebagai event di backend** (package Spine untuk yang generik, modul untuk yang domain). Nama event Laravel mengikuti konvensi `Domain\Verb` (mis. `after_add_task` → `TaskCreated`), listener didaftarkan di `EventServiceProvider` modul.

```text
5x after_update_task
4x after_add_task
3x lead_created
3x after_ticket_status_changed
3x after_staff_login
2x task_status_changed
2x project_status_changed
2x lead_status_changed
2x email_template_sent
2x contact_created
2x before_user_reset_password
2x before_staff_login
2x after_user_reset_password
2x after_payment_added
2x after_contact_login
1x ticket_created
1x task_timer_started
1x task_timer_deleted
1x task_follower_added
1x task_deleted
1x task_comment_updated
1x task_comment_deleted
1x task_comment_added
1x task_checklist_item_finished
1x task_checklist_item_created
1x task_assignee_added
1x staff_render_permissions
1x staff_profile_access
1x staff_member_updated
1x staff_member_profile_updated
1x staff_member_deleted
1x staff_member_created
1x smtp_test_email_success
1x smtp_test_email_failed
1x sms_trigger_triggered
1x set_password_email_sent
1x public_ticket_start
1x public_ticket_end
1x proposal_sent
1x proposal_declined
1x proposal_created
1x proposal_converted_to_invoice
1x proposal_converted_to_estimate
1x proposal_accepted
1x project_copied
1x pre_deactivate_module
1x pre_activate_module
1x notification_created
1x note_updated
1x note_deleted
1x note_created
1x non_existent_user_login_attempt
1x new_template_added
1x new_tag_created
1x module_deactivated
1x module_activated
1x lead_marked_as_lost
1x lead_marked_as_junk
1x lead_created_from_email_integration
1x lead_converted_to_customer
1x item_updated
1x item_deleted
1x item_created
1x item_coppied
1x invoice_unmarked_as_cancelled
1x invoice_status_changed
1x invoice_sent
1x invoice_overdue_reminder_sent
1x invoice_marked_as_cancelled
1x invoice_due_reminder_sent
1x invoice_copied
1x inactive_user_login_attempt
1x forgot_password_email_sent
1x failed_to_send_email_template
1x failed_login_attempt
1x expense_converted_to_invoice
1x existing_lead_email_inserted_from_email_integration
1x estimate_sent
1x estimate_requests_created
1x estimate_request_status_changed
1x estimate_request_assigned_changed
1x estimate_declined
1x estimate_converted_to_invoice
1x estimate_accepted
1x edit_logged_in_staff_profile
1x customers_area_knowledge_base_construct
1x customer_vault_entry_deleted
1x customer_updated_company_info
1x customer_subscribed_to_subscription
1x customer_group_deleted
1x credits_applied
1x credit_note_status_changed
1x credit_note_sent
1x credit_note_refund_updated
1x credit_note_refund_deleted
1x credit_note_refund_created
1x created_credit_note_from_invoice
1x contact_updated
1x contact_status_changed
1x contact_email_verified_but_requires_admin_confirmation
1x contact_email_verified
1x contact_deleted
1x client_status_changed
1x before_update_note
1x before_unpin_post
1x before_tickets_email_templates
1x before_ticket_deleted
1x before_template_deleted
1x before_tasks_email_templates
1x before_subscriptions_table
1x before_subscriptions_email_templates
1x before_staff_myprofile
1x before_staff_email_templates
1x before_send_test_smtp_email
1x before_save_completed_checklist_visibility
1x before_render_payment_gateway_settings
1x before_render_invoice_template
1x before_remove_project_file
1x before_proposals_email_templates
1x before_projects_email_templates
1x before_pin_post
1x before_payment_deleted
1x before_notifications_email_templates
1x before_leads_settings
1x before_leads_email_templates
1x before_leads_email_integration_form
1x before_lead_email_activity
1x before_lead_deleted
1x before_invoices_email_templates
1x before_invoice_deleted
1x before_get_payment_gateways
1x before_gdpr_email_templates
1x before_estimates_email_templates
1x before_estimate_request_email_templates
1x before_estimate_request_deleted
1x before_estimate_deleted
1x before_delete_ticket_reply
1x before_delete_staff_member
1x before_delete_post
1x before_delete_note
1x before_delete_department
1x before_delete_contact
1x before_delete_announcement
1x before_customers_email_templates
1x before_credit_notes_email_templates
1x before_credit_note_deleted
1x before_contracts_email_templates
1x before_contract_deleted
1x before_confirmation_identity_fields
1x before_compile_scripts_assets
1x before_client_login
1x before_client_deleted
1x before_check_recurring_tasks
1x app_client_assets_added
1x app_client_assets
1x app_admin_assets_added
1x app_admin_assets
1x announcement_updated
1x announcement_deleted
1x announcement_created
1x after_update_project
1x after_update_credit_note
1x after_ticket_reply_added
1x after_template_updated
1x after_template_deleted
1x after_system_info_files_permissions
1x after_single_knowledge_base_article_customers_area
1x after_render_invoice_template
1x after_proposal_updated
1x after_leads_settings
1x after_lead_email_activity
1x after_kb_groups_customers_area
1x after_invoice_updated
1x after_invoice_added
1x after_expense_updated
1x after_expense_added
1x after_estimate_updated
1x after_estimate_added
1x after_email_templates
1x after_department_added
1x after_customers_area_files
1x after_customer_billing_and_shipping_tab
1x after_customer_admins_tab
1x after_credit_note_deleted
1x after_create_credit_note
1x after_contract_updated
1x after_contract_added
1x after_confirmation_identity_fields
1x after_client_updated
1x after_client_deleted
1x after_client_added
1x after_check_recurring_tasks
1x after_add_project
1x after_add_discussion_comment
1x admin_area_after_project_progress
```

### 2. INFRA hooks → native Laravel (35)

```text
2x after_clients_area_init
1x pre_upgrade_database
1x pre_uninstall_module
1x pre_admin_init
1x pdf_construct
1x pdf_close
1x modules_loaded
1x module_uninstalled
1x module_installed
1x module_
1x model_init
1x deprecated_hook_run
1x deprecated_function_run
1x database_updated
1x clients_init
1x before_update_database
1x before_settings_group_view
1x before_perform_update
1x before_cron_run
1x auto_upgrade_failed_to_extract_zip_file
1x app_init
1x app_base_after_construct_action
1x after_settings_group_view
1x after_settings_e_sign_fields
1x after_pdf_signature_settings_fields
1x after_finance_settings_tabs_content
1x after_finance_settings_last_tab
1x after_cron_settings_last_tab_content
1x after_cron_settings_last_tab
1x after_cron_run
1x after_client_register_logged_in
1x after_client_register
1x admin_init
1x admin_auth_init
1x After_Hooks_Setup
```

### 3. FRONTEND hooks → skip (160)

Hook view/UI (render sidebar, tab, widget, form, logo, dsb.) **tidak di-port** — frontend adalah SPA Next.js yang konsumsi API, bukan HTML server-rendered. Contoh: `forms_table_start`, `before_remove_contact_profile_image`, `web_to_lead_form_start`, `customers_content_container_start`, `header_action`, `after_misc_settings`.


### 4. Catatan

- Klasifikasi berbasis pola nama + review manual 40 hook ambigu (semua terklasifikasi).
- Saat mem-port tiap modul, jalankan ulang inventaris di `modules/<modul>/` — hook domain modul (mis. `licence_html_viewed`) di-port bersama modulnya.
- Aturan konversi tetap mengikuti Bagian C di atas: `do_action` → `event()`, `add_action` → listener, `apply_filters` → event-mutation/Pipeline.
