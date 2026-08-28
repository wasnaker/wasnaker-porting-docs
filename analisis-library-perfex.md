# Analisis Library PerfexCRM — Penerapan untuk Backend Laravel API-Only

Dokumen ini menganalisis `application/libraries/` PerfexCRM (21 library utama + subdirektori:
`merge_fields/`, `pdf/`, `mails/`, `sms/`, `gateways/`, `gdpr/`, `import/`, `assets/`, `Session/`)
dan bagaimana cara menerapkannya di project backend **Laravel API-only** (`wasnaker.lan`).

> Prinsip sama seperti analisis helper: **API-only & modular**. Library berkaitan view/HTML/
> session-frontend → skip; logika teknis/bisnis → adopsi sebagai service/provider Laravel.

---

## Kategori Keputusan

| Kode | Makna |
|------|-------|
| ✅ **ADOP** | Logika berguna untuk backend API → pindah (service/provider Laravel) |
| ⚠️ **ADAPT** | Ada gunanya tapi perlu dimodifikasi/konversi untuk konteks API/token |
| ❌ **SKIP** | View/HTML/session-frontend/theme → tidak relevan API-only |
| 🔄 **NATIVE** | Sudah tersedia native di Laravel / package populer → tidak perlu adopsi ulang |

---

## 1. Library Inti (`application/libraries/*.php`)

### `App.php` — aplikasi inti & upgrade database ✅ ADAPT
`is_db_upgrade_required`, `upgrade_database`, `get_update_info`, `get_option`,
`get_available_languages`, `get_available_reminders_keys`.

→ Laravel pakai **Migrations** sudah native. `get_option` → `SettingService` (dari analisis
helper). Logika "app versioning/upgrade" → kontrol versi Laravel via migrations + `php artisan
migrate`. **Skrip upgrade khas Perfex → skip; migrasi DB diposisikan di module masing-masing.**

**STATUS: 🔄 ONGOING** — `get_option` sudah via `SettingService` (Batch 2), migrations native Laravel.

---

### `App_mailer.php` — Wrapper PHPMailer ⚠️ ADAPT
`from`, `to`, `reply_to`, `attach`, `send`, queue.

→ **Ganti native Laravel Mailable / Mail** (+ queue mail). Wrapper PHPMailer baku →
**skip**. Semua templating email → `database/notification` di modul.

**STATUS: ❌ BELUM** — belum implementasi Mailable/Notification di core.

---

### `App_Email.php` — antrean email + retry ✅ ADAPT
`send`, `send_queue`, `retry_queue`, `clean_up_old_queue`, `delete_queued_email`.

→ **Adopsi konsep** antrean email + retry + cleanup → Laravel **Queued Mailable** +
**Mail queue** + scheduled cleanup (`Failed Jobs`, retry via artisan). Implementasi native.

**STATUS: ❌ BELUM** — belum setup Mail queue + failed jobs.

---

### `App_Form_validation.php` — wrapper CI validation 🔄 NATIVE
`run`, `errors_array`.

→ **Ganti native Laravel Validation / FormRequest**. Konsep errors → `$validator->errors()`.

**STATUS: ✅ NATIVE** — Laravel FormRequest/Validation sudah pakai.

---

### `App_Migration.php` & `App_module_migration.php` & `App_module_installer.php` — migration modul ✅ ADOPT untuk modular
Mengelola migrate per modul + install modul dari upload.

→ **Laravel Migration native** per module; `php artisan module:migrate` (jika pakai
`nwidart/laravel-modules`). Instal/uninstall modul → pemetaan ke **service module discovery**.

**STATUS: ⚠️ PARCIAL** — `nwidart/laravel-modules` terinstall, module migration native.

---

### `App_modules.php` — register/aktifkan/nonaktifkan modul ✅ ADOPT (konsep)
`activate`, `deactivate`, `uninstall`, `is_active`, `is_installed`, `upgrade_database`.

→ **Adopsi ide** modul aktif/nonaktif di Laravel modular:
`nwidart/laravel-modules` (status + service provider per modul) atau mekanisme register
modul core sendiri. Logika modul mana yang dimuat oleh aplikasi → **config module**.

**STATUS: ✅ SELESAI** — `nwidart/laravel-modules` terdaftar di `LaravelModulesServiceProvider`; modul discovery aktif. Implementasi:
- `bootstrap/providers.php` — register `LaravelModulesServiceProvider`
- `app/Services/ModuleService.php` — wrapper service: `all`, `enabled`, `find`, `isEnabled`, `isDisabled`, `enable`, `disable`, `getPath`
- `app/Http/Controllers/ModuleController.php` — API endpoint: `GET /api/modules`, `GET /api/modules/enabled`, `GET /api/modules/{name}`, `GET /api/modules/{name}/status`, `POST /api/modules/{name}/enable`, `POST /api/modules/{name}/disable`
- `routes/api.php` — route registration
- **Apidocs**: ✅ ADA (Scribe generate + push ke repo `apidocs-wasnaker`, commit `40877c7`)

---

### `App_bulk_pdf_export.php` — export banyak PDF sekaligus ❌ ADAPT
Export PDF, zip, save dir.

→ **Ganti native**: `laravel-dompdf`/`laravel-snappy` untuk PDF + `ZipArchive`/`laravel-zip`.
Bagian "queue + background export" → **Job + Storage** (sesuai prinsip proses berat).

**STATUS: ❌ BELUM** — PDF library belum di-install.

---

### `App_items_table.php` & `App_items_table_template.php` — render tabel item (invoice/estimate) ❌ SKIP
`items`, `html_headings`, `pdf_headings` → render HTML/PDF view.

→ Untuk API-only: **skip** bagian render. Hanya pertahankan logika **data item + urutan/
kolom** di service modul; representasi HTML dipegang frontend/PDF di client.

**STATUS: ❌ SKIP** — render view tidak relevan API-only.

---

### `App_number_to_word.php` — angka → terbilang (IDN/India) ✅ ADOPT
`convert`, `convert_indian`, `convert_number_indian`.

→ **Adopsi** sebagai service/helper `NumberToWord` (dipakai API untuk menampilkan
terbilang di dokumen/invoice). Ini logika murni, tidak bergantung view.

**STATUS: ✅ SELESAI (Baru saja)**
- `app/Services/NumberToWord.php` — convert (ID), convertIndian (lakh/crore)
- `app/Http/Controllers/NumberToWordController.php` — API `POST /number-to-word/convert`, `/convert-indian`
- **Commit:** `7290167` | **Push:** `lrvl-wasnaker_core` + `apidocs-wasnaker`
- **Apidocs:** ✅ ADA (generate + push ke `apidocs-wasnaker`)
- **HTTP test:** convert 1234567 → "sejuta dua ratus tiga puluh empat ribu lima ratus enam puluh tujuh rupiah"

---

### `App_object_cache.php` — object cache in-memory 🔄 NATIVE
`get`, `add`, `flush`, `incr`, `decr`, `stats`.

→ **Ganti native Laravel Cache / Runtime cache.** Gunakan Redis/Laravel Cache Bag.

**STATUS: ✅ NATIVE** — Laravel Cache (Redis) sudah terpakai.

---

### `App_menu.php` & `App_tabs.py` — menu/sidebar/tab view ❌ SKIP
Cocok untuk frontend admin → tidak relevan API-only.

**STATUS: ❌ SKIP** — frontend concern.

---

### `App_tags.php` — handle tag & relasi ✅ ADAPT
`get`, `create`, `save`, `relation`, `all`, `flat`.

→ **Ganti package `spatie/laravel-tags`** (native Laravel). Bila ingin custom, adopsi
logika tag + relation di module/`TagService`.

**STATUS: 🔄 DEFERRED** — pakai Spatie Tags saat butuh, bukan core.

---

### `App_pusher.py` — realtime via Pusher 🔄 NATIVE
→ Laravel **Broadcasting** (pusher/ably/reverb). `Reverb` sudah ada di plan stack.

**STATUS: 🔄 PLANNED** — Reverb untuk realtime.

---

### `Endroid_qrcode.py` — QR code ✅ ADOPT (jika perlu)
→ **Package `endroid/qr-code`** (sudah dipakai Perfex) atau `simplesoftwareio/simple-qrcode`.
Dipakai untuk 2FA/signature/scan bila ada.

**STATUS: ❌ BELUM** — package belum di-install.

---

### `Stripe_core.php` & `Stripe_subscriptions.php` — integrasi Stripe ✅ ADOPT (jika dipakai)
`create_customer`, `get_customer`, `create_session`, webhooks.

→ **Adopsi** sebagai **module Payment Gateway** dengan package `laravel/cashier-stripe` atau
sdk Stripe + service. Webhook → endpoint API + event listener.

**STATUS: ❌ BELUM** — payment gateway module pending.

---

## 2. Subdirektori Library

### `merge_fields/` — template placeholder (staff/client/invoice/project dst) ⚠️ ADAPT
Menyediakan variabel per modul untuk template email/PDF.

→ Untuk API-only, `merge field` baku diganti **Laravel Mailable + Blade** (Blade punya
variable & loops). **Skip** sistem merge-field Perfex; mapping user/data → data model di
Mailable.

**STATUS: ✅ SELESAI** — MailService + MailController + GenericMailNotification sudah diimplementasikan untuk core mail API. Implementasi:
- `app/Services/MailService.php` — wrapper `send`, `notify`, `notifyMany`
- `app/Http/Controllers/MailController.php` — API `POST /api/mail/send`, `/notify`, `/notify-many`
- `app/Notifications/GenericMailNotification.php` — Notification channel mail
- **Apidocs**: ✅ ADA (Scribe generate + push ke repo `apidocs-wasnaker`, commit `f1e12af`)

---

### `pdf/` — generator PDF per modul (`Invoice_pdf`, `Estimate_pdf`, `Proposal_pdf`, dst) ✅ ADAPT
→ **Ganti `laravel-dompdf` / `laravel-snappy`**. Ini pola penting untuk API: **generate PDF
lewat Job** (nilai invoicePOS/logo/kolom). Representasi PDF bisa dibuat dari **HTML template
Blade** yang dibutuhkan frontend, atau PDF di-generate server saat permintaan download.

**STATUS: ❌ BELUM** — DomPDF/Snappy belum di-install.

---

### `mails/` — templated class email per skenario (60+ file) 🔄 NATIVE (konsep)
→ Setiap `*_mail.php` di Perfex = **Laravel Mailable** + **Notification class** di modul.
Ini pemetaan 1:1 konsep. Contoh: `Invoice_send_to_customer.php` →
`Modules\Sales\Mail\InvoiceSentToCustomer`.

**STATUS: ✅ SELESAI** — MailService + MailController + GenericMailNotification sudah diimplementasikan untuk core mail API. Implementasi:
- `app/Services/MailService.php` — wrapper `send`, `notify`, `notifyMany`
- `app/Http/Controllers/MailController.php` — API `POST /api/mail/send`, `/notify`, `/notify-many`
- `app/Notifications/GenericMailNotification.php` — Notification channel mail
- **Apidocs**: ✅ ADA (Scribe generate + push ke repo `apidocs-wasnaker`, commit `f1e12af`)

---

### `sms/` — provider SMS (`Sms_twilio`, `Sms_clickatell`, `Sms_msg91`) ✅ ADOPT (optional)
→ Adopsi sebagai **abstract SMS provider** + notifikasi channel SMS (
`laravel/notifications` + driver Twilio). Provider pluggable.

**STATUS: ❌ BELUM** — SMS channel belum.

---

### `gateways/` — payment gateway (`Stripe`, `Paypal`, `Mollie`, `Instamojo`, dst) ✅ ADOPT
→ Adopsi pola **abstraksi gateway** → interface `PaymentGateway` + feature `PaymentService`,
bukan satu per satu. Setiap gateway diaktifkan konfiguratif.

**STATUS: ❌ BELUM** — Payment abstraction pending.

---

### `gdpr/` — service permission/export/delete per modul (GDPR) ✅ ADOPT
→ Adopsi sebagai **module GDPR / data-privacy service**: consents, data export (JSON),
data erasure (anonymize/delete) — cocok untuk API & compliance.

**STATUS: ❌ BELUM** — GDPR service pending.

---

### `import/` — import CSV/Excel data (`Import_customers`, `Import_items`, `Import_leads`) ⚠️ ADAPT
→ **Import/export** di Laravel via package **`maatwebsite/excel`** (Laravel Excel) +
**Job + queue**. Konsep skema kolom & validasi dipertahankan sebagai config/import DTO.

**STATUS: ❌ BELUM** — Laravel Excel belum di-install.

---

### `assets/` — load CSS/JS/view ❌ SKIP
Frontend asset → tidak relevan API-only.

**STATUS: ❌ SKIP** — frontend concern.

---

### `Session/` — driver session CI 🔄 NATIVE
→ **Skip**. Laravel pakai Session sendiri; API memakai **Sanctum token**, bukan session.

**STATUS: ✅ NATIVE** — Sanctum token-based auth.

---

## 3. Rekomendasi Penerapan di Project Laravel API-Only

| Library Perfex | Implementasi Laravel | Lokasi |
|----------------|----------------------|--------|
| `App_mailer` / `App_Email` | Mailable + Mail queue | Core notify |
| `App_number_to_word` | `NumberToWord` service | Core `Support` |
| `App_object_cache` | Laravel Cache / Redis | Core |
| `App_modules` | Module discovery / `nwidart` | Core module-loader | ✅ ADA | ✅ ADA |
| `App_tags` | `spatie/laravel-tags` | Core |
| `App_pusher` | Laravel Broadcasting/Reverb | Core |
| `Endroid_qrcode` | `endroid/qr-code` | Core (jika perlu) |
| `merge_fields/` | Blade + Mailable data | Per module |
| `pdf/` | DomPDF/Snappy via Job | Per module |
| `mails/` | Mailable/Notification per modul | Per module |
| `gateways/` + `Stripe_*` | `PaymentGateway` interface + Cashier/SDK | Core Payment + per module |
| `sms/` | Notification SMS channel | Core (optional) |
| `gdpr/` | GDPR/Privacy service | Core |
| `import/` | Laravel Excel + Job | Per module |
| `App_menu`/`App_tabs`/`assets` | — | **Skip** (frontend) |
| `App_items_table` | data item di service, render di client | Per module |

### Struktur Target

```text
app/
├── Support/
│   └── NumberToWord.php            # dari App_number_to_word
├── Services/
│   ├── SettingService.php          # dari App->get_option
│   ├── TagService.py               # dari App_tags (atau spatie)
│   ├── PaymentService.py           # abstraksi gateway
│   └── ReceivePaymentService.py
└── Providers/
    ├── ModuleServiceProvider.py    # load modul aktif (dari App_modules)
    └── ...

modules/
├── Sales/
│   ├── Mail/                       # dari mails/ (Mailable)
│   ├── Pdf/                        # dari pdf/ (DomPDF via Job)
│   └── Services/InvoiceService.py
└── ...
```

---

## 4. Kesimpulan

- Library yang **berupa logika teknis murni** → **diadopsi** sebagai service/provider
  Laravel (`NumberToWord`, cache, QR).
- Library yang **berupa view/HTML/frontend** (`assets`, `menu`, `tabs`, `items_table`,
  `merge_fields`-rendering) → **skip** (API-only; frontend dipegang client).
- Library **integrasi eksternal** (mail, SMS, payment gateway, import) → **adopsi konsep
  abstraksinya** sebagai provider/interface Laravel, pakai package native.
- Template email (`mails/`) → **Mailable/Notification** per modul.
- PDF → **Job + DomPDF/Snappy** per modul (proses berat, tidak di request sync).
- Modul active/inactive (`App_modules`) → **modular Laravel** (nwidart atau kustom).

---

## 5. Ringkasan Status Implementasi (UPDATE)

| Library | Kategori | Status | Lokasi Implementasi | Commit/Batch | Apidocs |
|---------|----------|--------|---------------------|--------------|---------|
| `App.php` | ADAPT | 🔄 ONGOING | `SettingService`, native migrations | - | ❌ N/A |
| `App_mailer.py` | ADAPT | ❌ BELUM | Mailable/Notification | - | ❌ Belum |
| `App_Email.py` | ADAPT | ❌ BELUM | Queued Mailable + Mail queue | - | ❌ Belum |
| `App_Form_validation.py` | NATIVE | ✅ NATIVE | Laravel FormRequest | - | ❌ N/A |
| `App_Migration` / `App_module_installer` | ADOPT | ⚠️ PARCIAL | `nwidart/laravel-modules` | - | ❌ N/A |
| `App_modules.py` | ADOPT | ✅ SELESAI | `nwidart` + ModuleService/Controller API | `app/Services/ModuleService.php`, `app/Http/Controllers/ModuleController.php` | ✅ ADA |
| `App_bulk_pdf_export.py` | ADAPT | ❌ BELUM | DomPDF/Snappy + Job + Zip | - | ❌ Belum |
| `App_items_table` / `App_items_table_template` | SKIP | ❌ SKIP | - | - | ❌ N/A |
| `App_number_to_word.py` | ADOPT | ✅ SELESAI | `NumberToWord`, `NumberToWordController` | `7290167` | ✅ ADA |
| `App_object_cache.py` | NATIVE | ✅ NATIVE | Laravel Cache (Redis) | - | ❌ N/A |
| `App_menu.py` / `App_tabs.py` | SKIP | ❌ SKIP | - | - | ❌ N/A |
| `App_tags.py` | ADAPT | 🔄 DEFERRED | `spatie/laravel-tags` | - | ❌ N/A |
| `App_pusher.py` | NATIVE | 🔄 PLANNED | Laravel Broadcasting/Reverb | - | ❌ N/A |
| `Endroid_qrcode.py` | ADOPT | ❌ BELUM | `endroid/qr-code` | - | ❌ Belum |
| `Stripe_core.py` / `Stripe_subscriptions.py` | ADOPT | ❌ BELUM | `PaymentGateway` + Cashier | - | ❌ Belum |
| `merge_fields/` | ADAPT | ❌ BELUM | Mailable + Blade data | - | ❌ Belum |
| `pdf/` (Invoice_pdf, dll) | ADAPT | ❌ BELUM | DomPDF/Snappy via Job | - | ❌ Belum |
| `mails/` | NATIVE | ❌ BELUM | Mailable/Notification per modul | - | ❌ Belum |
| `sms/` | ADOPT | ❌ BELUM | Notification SMS channel | - | ❌ Belum |
| `gateways/` | ADOPT | ❌ BELUM | `PaymentGateway` interface | - | ❌ Belum |
| `gdpr/` | ADOPT | ❌ BELUM | GDPR/Privacy service | - | ❌ Belum |
| `import/` | ADAPT | ❌ BELUM | Laravel Excel + Job | - | ❌ Belum |
| `assets/` | SKIP | ❌ SKIP | - | - | ❌ N/A |
| `Session/` | NATIVE | ✅ NATIVE | Sanctum token | - | ❌ N/A |

**Legenda Apidocs:**
- ✅ **ADA** = Scribe generate + push ke repo `apidocs-wasnaker` (terdokumentasi di apidocs.wasnaker.lan)
- ❌ **Belum** = Belum ada controller endpoint, atau belum di-generate
- ❌ **N/A** = Tidak relevan (helper murni / view-only / skip / native tanpa endpoint)

---

*Dokumen dibuat berdasarkan inspeksi `application/libraries/` PerfexCRM, 27 Agustus 2026.*
*Diupdate: 28 Agustus 2026 — status NumberToWord ✅ SELESAI + kolom Apidocs ditambahkan.*