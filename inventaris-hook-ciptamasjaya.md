# Inventaris Hooks — app.ciptamasjaya.co.id (Perfex kustom)

Dokumen ini memetakan sistem hook aplikasi legacy **app.ciptamasjaya.co.id**
(PerfexCRM yang dikustomisasi untuk bisnis inspeksi/licensi — ada hook
`inspection_*`, `licence_*`, `schedule_*`, `jobreport_*`, `office_*`,
`billing_*`) ke backend Spine (Laravel API-only).

Referensi awal: gist JamesSimpson
(https://gist.github.com/JamesSimpson/4eae4ba2d6d7072eca9f0fae58b8887c) — hanya
mencakup controllers admin standar Perfex. **Ground truth diambil langsung dari
aplikasi**: 526 hook unik (`do_action`) dari `application/` + `modules/`.

## Lokasi file hook di aplikasi

| File | Peran |
|------|-------|
| `application/config/hooks.php` | Deklarasi bootstrap hooks + fungsi `hooks()` |
| `application/hooks/App_Autoloader.php` | Autoload class App_*/modul |
| `application/hooks/EnhanceSecurity.php` | Blokir bot/UA/referrer buruk |
| `application/hooks/InitModules.php` | Load modul aktif + csrf_exclude_uris |
| `application/hooks/InitHook.php` | Init library + jalankan `modules_loaded`, `admin_init` |
| `application/helpers/core_hooks_helper.php` | Helper sistem action/filter |
| `application/third_party/action_hooks.php` | Package `bainternet/php-hooks` (add_action/do_action/add_filter/apply_filters) |
| `application/controllers|models|libraries|core` + `modules/*` | Titik `do_action(...)` tersebar (526 unik) |

## Klasifikasi (526 unik)

| Kategori | Jumlah | Nasib |
|----------|--------|-------|
| **BACKEND — generik (Spine)** | ±50 | Event Spine (port sekarang) |
| **BACKEND — domain (modul)** | ±200 | Event per-modul saat modul di-port (Sales, Jobreport, Licence, Inspection, Schedule, ...) |
| **FRONTEND / VIEW** | ±210 | SKIP — API-only (html_viewed, tabs, menu, widget, forms, settings views, upload-anchored view hooks) |
| **INFRA / bootstrap** | ±35 | NATIVE — ServiceProvider + Middleware + Composer autoload (keputusan `analisis-hook-perfex.md` Bagian A) |
| **UNKNOWN (review manual)** | ±30 | Mayoritas domain event → masuk kategori modul |

## Hook generik → target Spine (port Batch 1)

Keputusan `analisis-hook-perfex.md`: `do_action` → Laravel Events; `apply_filters`
→ Pipeline/event-mutation; bootstrap → native.

### Sudah dibuat (event class + dispatch nyata, 30 Agu 2026)

| Hook Perfex | Event Spine | Dispatch di |
|-------------|-------------|-------------|
| settings save (option_updated dkk) | `Spine\Events\SettingUpdated` | `SettingService::set()` (create + update) |
| `sms_trigger_triggered` / SMS provider events | `Spine\Events\SmsSent` | `SmsService::send()` |
| `module_installed` | `Spine\Events\ModuleInstalled` | `ModuleController::install()` |
| `module_uninstalled` | `Spine\Events\ModuleUninstalled` | `ModuleController::uninstall()` |
| `module_activated` | `Spine\Events\ModuleActivated` | `ModuleController::enable()` |
| `module_deactivated` | `Spine\Events\ModuleDeactivated` | `ModuleController::disable()` |

### Dipetakan ke native Laravel (tidak perlu kode)

| Hook Perfex | Native Laravel |
|-------------|----------------|
| `after_staff_login`, `before_staff_login`, `after_contact_login`, `before_client_login` | `Illuminate\Auth\Events\Login` |
| `after_user_logout`, `before_staff_logout`, `after_client_logout`, `before_contact_logout` | `Illuminate\Auth\Events\Logout` |
| `before_user_reset_password`, `after_user_reset_password`, `forgot_password_email_sent`, `set_password_email_sent` | `PasswordReset` + `PasswordBroker` events |
| `email_template_sent`, `failed_to_send_email_template`, `smtp_test_email_success/failed` | `Illuminate\Mail\Events\MessageSent` + `MessageSending` |
| `modules_loaded`, `admin_init` | `ServiceProvider::boot()` |
| `before_cron_run`, `after_cron_run` | Scheduler events / `Schedule` (saat scheduler dibuat) |
| `before_upload_*` (13 varian) | Validasi `FileService` (saat upload endpoint dibangun) |

### Ditunda ke modul (contoh, bukan daftar penuh)

`lead_*`, `invoice_*`, `estimate_*`, `proposal_*`, `quotation_*`,
`contract_*`, `credit_note_*`, `ticket_*`, `project_*`, `task_*`,
`expense_*`, `payment_*`, `staff_member_*` (CRUD staff → app konsumen),
`jobreport_*`, `inspection_*`, `licence_*`, `schedule_*`, `office_*`,
`billing_*`, `newsfeed_*`, `discussion_*`, `sms_*` (bukan trigger),
`email_*` (domain).

Aturan: event domain dibuat di `modules/<N>/Providers/EventServiceProvider.php`
saat modul di-port — JANGAN masuk package Spine (hard rule: tidak ada kode
modul di core).

## Verifikasi port (30 Agu 2026)

- `php -l` 9 file OK; 6 event terautoload di konsumen spine.lan.
- `SettingUpdated`: dispatch terbukti create + update (tinker, Event::listen).
- `SmsSent`: dispatch terbukti (driver log).
- Module events: ter-wire (lint OK), runtime butuh auth + modul nyata.
- Commit package: `laravelspine/laravelspine` `3f54298`.
