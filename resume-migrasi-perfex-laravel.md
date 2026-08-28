# Resume — Migrasi PerfexCRM ke Backend Laravel API-Only

## 1. Tujuan

- Migrasi arsitektur PerfexCRM menuju sistem yang lebih modular.
- Business logic PerfexCRM akan **diekstraksi ke backend Laravel baru**.
- Laravel menjadi core backend dan menyediakan API sebagai pintu utama aplikasi.
- PerfexCRM lama dipertahankan sementara sebagai legacy/reference system selama masa transisi.
- Target akhir adalah satu backend/business logic yang dapat digunakan oleh berbagai client.

## 2. Strategi Migrasi

- Business logic tidak lagi bergantung pada controller dan view PerfexCRM.
- Logic bisnis dipindahkan secara bertahap ke Laravel.
- Sistem lama dan sistem baru dapat berjalan paralel selama masa transisi.
- Migrasi dilakukan per modul agar risiko perubahan dapat dikendalikan.
- Database dan data existing PerfexCRM harus dipertahankan kompatibilitasnya selama proses migrasi.
- Setelah modul berhasil dipindahkan dan diuji, frontend/client baru menggunakan API Laravel.

## 3. Arsitektur Target

```text
                    ┌─────────────────┐
                    │   Web Frontend  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Laravel API   │
                    │    Backend      │
                    └────────┬────────┘
                             │
             ┌───────────────┼────────────────┐
             │               │                │
        Authentication   Business Logic    Authorization
        Sanctum/Fortify   Services/Jobs     Permission
             │               │                │
             └───────────────┼────────────────┘
                             │
                    ┌────────▼────────┐
                    │    Database     │
                    └─────────────────┘
                             │
                    ┌────────▼────────┐
                    │ Redis / Queue   │
                    │    Workers      │
                    └─────────────────┘
```

## 4. Laravel Stack

### Core

- **Laravel Framework**
  - Core backend.
  - REST API.
  - Routing.
  - Dependency Injection.
  - Eloquent ORM.
  - Validation.
  - Configuration dan environment management.

### Authentication

- **Laravel Sanctum**
  - API authentication.
  - Token-based authentication.
  - Cocok untuk SPA, mobile application, internal API dan service client.

- **Laravel Fortify**
  - Login.
  - Registration.
  - Password reset.
  - Email verification.
  - Two-factor authentication bila diperlukan.

### Authorization

- **Spatie Laravel Permission**
  - Role management.
  - Permission management.
  - Capability management.
  - User-role relationship.
  - Role-permission relationship.

- **Laravel Policies & Gates**
  - Authorization pada level resource dan action.
  - Memastikan user hanya dapat mengakses resource yang memang diperbolehkan.

### Background Processing

- **Laravel Queue**
  - Menjalankan proses berat secara asynchronous.
  - Menghindari proses panjang berada langsung di HTTP request.
  - Mengurangi risiko PHP `max_execution_time` timeout.

- **Laravel Jobs**
  - Generate dokumen.
  - Import/export.
  - Processing data.
  - Integrasi API eksternal.
  - Pekerjaan berat lainnya.

- **Laravel Horizon**
  - Monitoring queue.
  - Monitoring worker.
  - Management job berbasis Redis.

### Scheduling

- **Laravel Scheduler**
  - Scheduled task.
  - Maintenance task.
  - Sinkronisasi berkala.
  - Processing otomatis.

### Event & Notification

- **Laravel Events & Listeners**
  - Memisahkan business event dari proses yang mengikutinya.
  - Mengurangi coupling antar modul.

- **Laravel Notifications**
  - Email notification.
  - Database notification.
  - Channel notification lainnya.

### API

- **Laravel API Resources**
  - Standardisasi response JSON.
  - Memisahkan representasi API dari model database.

- **Laravel Form Requests**
  - Validasi request.
  - Authorization request.
  - Menjaga controller tetap tipis.

- **Laravel HTTP Client**
  - Komunikasi dengan external API/service.

### Data & Infrastructure

- **Laravel Eloquent ORM**
  - Database abstraction.
  - Model dan relationship.
  - Query database.

- **Redis**
  - Queue backend.
  - Cache.
  - Shared state bila diperlukan.

- **Laravel Cache**
  - Caching data yang sering digunakan.
  - Mengurangi beban database.

- **Laravel Storage**
  - Abstraksi penyimpanan file.
  - Dapat diarahkan ke local storage maupun object storage.

- **Laravel Logging**
  - Application logging.
  - Error dan operational logging.

- **Laravel Reverb**
  - Real-time/WebSocket.
  - Digunakan bila diperlukan untuk dashboard realtime, notification realtime, status job, dan kebutuhan sejenis.

## 5. Prinsip Business Logic

- Controller tidak menjadi tempat utama business logic.
- Controller bertugas menerima request dan meneruskan proses ke layer aplikasi/business.
- Business logic ditempatkan pada service/domain layer yang dapat digunakan kembali.
- Business logic tidak boleh bergantung pada tampilan frontend.
- Business logic tidak boleh bergantung pada controller tertentu.
- API menjadi interface untuk mengakses business logic.
- Web, mobile, AI agent, automation, dan integrasi pihak ketiga dapat menggunakan backend yang sama.

### 5.1 Penempatan Service — Level Module (keputusan arsitektur)

> **Keputusan:** Service bisnis per modul (mis. `InvoiceService`, `EstimateService`,
> `ProjectService`) **berada di level module**, bukan di core `app/`.

Alasan:
- Sesuai konsep awal: modul yang dihilangkan dari core PerfexCRM menjadi **module tersendiri**.
- Module menjadi unit mandiri yang membungkus service + model + routes + migrations + dll.
- Service modul tidak bergantung pada core; komunikasi antar modul lewat interface/events,
  bukan dependency langsung.
- Core hanya menyimpan **cross-cutting service** (lintas modul) yang benar-benar reusabel.

Pembagian dua level:

- **Level Core (`app/`)** — hanya service lintas-modul & reusabel:
  `SettingService`, `ActivityLogService`, `NotificationService`, `FileService`,
  `RelationService`, `MetaDataService`, helper `Str/Number/Time`, trait `HasMetaData`.
- **Level Module (`modules/*`)** — service bisnis milik masing-masing modul:
  `InvoiceService`, `EstimateService`, `ProjectService`, `ContactService`, dst.

### 5.2 Struktur Module (berdasar konsep awal + analisis helper)

```text
modules/
├── Sales/
│   ├── Invoice/
│   │   ├── src/
│   │   │   ├── Services/
│   │   │   │   └── InvoiceService.php      # business logic (dari invoices_helper)
│   │   │   ├── Models/
│   │   │   │   └── Invoice.php
│   │   │   ├── Http/
│   │   │   │   ├── Controllers/
│   │   │   │   └── Requests/
│   │   │   └── Events/                      # komunikasi antar modul
│   │   ├── Routes/
│   │   │   └── api.php
│   │   └── Database/
│   │       └── migrations/
│   ├── Estimate/                 # EstimateService (dari estimates_helper)
│   └── ...
├── Project/                      # ProjectService (dari projects_helper)
│   └── ...
├── Support/                      # TicketService (dari tickets_helper)
├── HR/                           # StaffService / RoleService
├── Content/                      # KnowledgeBase / Announcement / EmailTemplate
└── ...
```

Aturan:
- Tiap modul = satu unit mandiri (service + model + routes + migrations + events + jobs).
- Service modul TIDAK menempel di core `app/` — menempel di module miliknya.
- Komunikasi antar modul melalui **Events/Listeners** dan **interface**, bukan dependency langsung.
- Implementasi di Laravel dapat memakai: package `nwidart/laravel-modules`, struktur folder
  manual (`modules/*`), atau struktur package php iteratif — disepakati saat setup project.

## 6. Masalah PHP Traditional yang Ingin Dihindari

- PHP HTTP request memiliki batas waktu eksekusi.
- `max_execution_time` dapat menyebabkan proses panjang mengalami timeout.
- Proses berat tidak sebaiknya dijalankan langsung dalam request API.
- Solusi:
  - API menerima request.
  - API membuat Job.
  - Job dimasukkan ke Queue.
  - Worker menjalankan proses di background.
  - Client mendapatkan status/progress melalui API.
- Dengan pola ini, proses berat tidak bergantung pada lifetime HTTP request.

## 7. Pemisahan Jenis Proses

Sistem akan membedakan:

- **Synchronous API Request**
  - Operasi cepat.
  - Harus segera memberikan response.

- **Background Job**
  - Operasi berat.
  - Diproses oleh worker.

- **Scheduled Task**
  - Operasi yang berjalan berdasarkan jadwal.

- **Long-running Worker**
  - Worker yang terus berjalan untuk memproses queue.

## 8. Client yang Dapat Menggunakan Backend

Backend Laravel dirancang agar dapat digunakan oleh:

- Web application.
- Mobile application.
- Internal application.
- Third-party integration.
- AI agent.
- Automation service.
- Service/API lain.

## 9. Target Arsitektur Akhir

```text
                    ┌──────────────────────┐
                    │    Client Layer      │
                    │                      │
                    │ Web │ Mobile │ AI    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Laravel API       │
                    │                      │
                    │ Auth                 │
                    │ Authorization        │
                    │ API Resources        │
                    │ Validation            │
                    └──────────┬───────────┘
                               │
                               ▼
                     ┌──────────────────────┐
                     │    Core Layer        │
                     │  (cross-cutting)     │
                     │                      │
                     │ SettingService       │
                     │ ActivityLogService   │
                     │ Auth / Authorization │
                     └──────────┬───────────┘
                                │
                     ┌──────────▼───────────┐
                     │  Module Layer        │
                     │  (business logic)    │
                     │                      │
                     │  ┌──────────────┐    │
                     │  │InvoiceModule │    │
                     │  │ InvoiceSvc   │    │
                     │  │ Model/Routes │    │
                     │  └──────────────┘    │
                     │  ┌──────────────┐    │
                     │  │ProjectModule │    │
                     │  │ ProjectSvc   │    │
                     │  └──────────────┘    │
                     │  ...                 │
                     └──────────┬───────────┘
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
            Database          Redis        External APIs
                 │              │
                 │              ▼
                 │          Queue/Worker
                 │
                 ▼
         Existing / New Data
```

> Business/service layer kini dipisah menjadi:
> - **Core Layer** — layanan lintas modul (auth, settings, activity log, files, meta).
> - **Module Layer** — masing-masing modul membungkus service bisnis, model, routes, jobs-nya sendiri.

## 10. Prinsip Utama Proyek

> **PerfexCRM menjadi sumber business logic legacy, sedangkan Laravel menjadi target backend baru yang modular, API-first, dan tidak bergantung pada frontend.**

- Migrasi dilakukan bertahap.
- Business logic dipisahkan dari presentation layer.
- API menjadi interface utama.
- Authentication dan authorization terpusat.
- Proses berat menggunakan Queue/Worker.
- Sistem dirancang agar dapat digunakan oleh banyak jenis client.
- Komponen Laravel digunakan sesuai kebutuhan; tidak semuanya harus diaktifkan sejak tahap pertama.

## 11. Tahap Berikutnya

Tahapan teknis berikutnya dapat diarahkan pada:

1. Audit struktur PerfexCRM existing. *(done — lihat `identifikasi-core-perfex.md`)*
2. Identifikasi seluruh business logic dan dependency.
3. Mapping module PerfexCRM ke Laravel. *(kelompok modul — lihat `identifikasi-core-perfex.md`)*
4. Menentukan database strategy.
5. Membuat Laravel API foundation.
6. Implementasi authentication dan authorization.
7. Membuat architecture untuk service/domain layer. *(keputusan: service di level module)*
8. Memindahkan modul Perfex satu per satu.
9. Membuat API contract.
10. Membuat frontend/client baru.
11. Menjalankan old dan new system secara paralel.
12. Melakukan cut-over secara bertahap.
13. Menghapus dependency PerfexCRM setelah seluruh business logic berhasil dimigrasikan.

> **Referensi dokumen analisis:**
> - `identifikasi-core-perfex.md` — modul core yang jadi module (Kelompok 1–6).
> - `analisis-helper-perfex.md` — keputusan adopsi 45 helper PerfexCRM
>   (ADOP / ADAPT / SKIP / NATIVE) untuk backend API-only.

---

## 12. Keputusan: API Versioning — semua endpoint di `/api/v1` (tanpa kecuali)

**Status: ✅ DITERAPKAN (29 Agustus 2026, commit `9e99863` core / `45a21aa` apidocs)**

Keputusan: **seluruh** endpoint API — termasuk `health` dan `broadcasting/auth` —
di-versi-kan di bawah prefix `/api/v1`. Tidak ada pengecualian. Alasan:

- Modul Sales sudah terlanjur memakai `/api/v1/sales` → tanpa versioning terjadi
  inkonsistensi prefix.
- Fase development, belum ada klien eksternal → sekarang waktu termurah untuk
  menetapkan kontrak stabil. Breaking change berikutnya → `v2`, path lama tetap
  hidup (tidak langsung dihapus) setelah ada klien di luar kendali kita.

### Yang dimodifikasi (persis)

| File | Perubahan |
|------|-----------|
| `routes/api.php` | Seluruh isi dibungkus `Route::prefix('v1')->group(...)` |
| `bootstrap/app.php` | `withBroadcasting` prefix `api` → `api/v1` (auth channel) |
| `app/Http/Controllers/BroadcastController.php` | Docblock path auth diperbarui |
| `~/.hermes/skills/legacy-php-porting` | Konvensi path di skill disesuaikan |
| `~/ws-e2e.js` | Script tes realtime: base URL + path disesuaikan ke `/api/v1` |

### Perpindahan path (semua `api/*` → `api/v1/*`)

| Grup | Contoh path lama → baru |
|------|------------------------|
| Infra | `GET /api/health` → `/api/v1/health` (public, tanpa token) |
| Auth | `GET /api/login` (named `login`) → `/api/v1/login` |
| User | `GET /api/user` → `/api/v1/user` |
| Settings | `GET/PUT/DELETE /api/settings/{key}`, `POST /api/settings/bulk` → `/api/v1/...` |
| Activity Logs | `GET /api/activity-logs...` → `/api/v1/activity-logs...` |
| Custom Meta | `/api/meta/{type}/{id}/...` → `/api/v1/meta/...` |
| Relations | `/api/relations/...` → `/api/v1/relations/...` |
| NumberToWord | `/api/number-to-word/...` → `/api/v1/number-to-word/...` |
| Modules | `/api/modules...` → `/api/v1/modules...` |
| Files | `/api/files...` → `/api/v1/files...` |
| Mail | `/api/mail/...` → `/api/v1/mail/...` |
| Payment | `/api/payment/...` → `/api/v1/payment/...` |
| GDPR | `/api/gdpr/...` → `/api/v1/gdpr/...` |
| PDF | `/api/pdf/...` → `/api/v1/pdf/...` |
| SMS | `/api/sms/...` → `/api/v1/sms/...` |
| QR Code | `/api/qr-code/...` → `/api/v1/qr-code/...` |
| Excel | `/api/excel/...` → `/api/v1/excel/...` |
| Tags | `/api/tags...` → `/api/v1/tags...` |
| Broadcasting | `GET /api/broadcast/config`, `POST /api/broadcast/test`, `POST /api/broadcasting/auth` → `/api/v1/...` |
| Sales (module) | sudah `/api/v1/sales` — tidak berubah |

Total: 62 route terdaftar di `/api/v1`, 0 route tersisa di `/api` tanpa versi.

### Perilaku path lama

- Path lama `/api/*` → **404** (tanpa alias/redirect — sengaja, fase dev).
- `routes/web.php` catch-all SPA sudah mengecualikan `api(?:/|$)` → aman.
- Klien wajib update prefix: frontend Next.js (dicatat, dikerjakan saat frontend
  dibuka lagi), script tes (`~/ws-e2e.js` sudah diperbarui).

### Verifikasi

- `php artisan route:list` — 62 route `api/v1`, 0 sisa.
- HTTP: `/api/v1/health` 200 tanpa token; `/api/v1/activity-logs` 200+token / 401
  tanpa token; `/api/v1/broadcasting/auth` 200+token; path lama 404.
- Realtime E2E WebSocket: auth → subscribe `private-user.1` → event
  `notification.sent` diterima (via `/api/v1/broadcast/*`).

### Struktur menu apidocs: top-level `api/v1` + subgroup (v2-ready)

Keputusan lanjutan: menu dokumentasi mengikuti versi API — top-level `api/v1`,
di dalamnya subgroup per domain. Saat `api/v2` tiba, tinggal muncul grup top-level
kedua; subgroup per domain bisa dipakai ulang.

Implementasi (commit `c384f15` core / `83b9a59` apidocs / `92e8280` sales-module):

- Semua controller core: `@group api/v1` + `@subgroup <domain>` (Activity Logs,
  Broadcasting, Custom Meta, Excel, Files, GDPR, Mail, Modules, Payment, Pdf,
  QrCode, Relations, Settings, Sms, System, Tags, Utilities).
- `ApiController`: route login (closure) diubah jadi method `login()` agar bisa
  diberi annotation (`@subgroup System`).
- `config/scribe.php`: `groups.order => ['api/v1']` + exclude `*/broadcasting/auth`
  (controller framework internal, dipanggil otomatis laravel-echo — tidak perlu
  masuk menu).
- Sales module (repo `wasnaker-sales-module`): `@group api/v1` + `@subgroup Sales`.
  **Pitfall ditemukan:** docblock `@group`/`@subgroup` HARUS di SEBELUM deklarasi
  `class X extends Controller` — docblock yang ditaruh setelah `{` melekat ke
  member pertama (bukan class), sehingga class-level tidak terbaca dan endpoint
  nyasar ke grup `Endpoints`. Solusi sementara awal (annotation per-method)
  membuat Scribe merender heading subgroup BERULANG per endpoint (System x3,
  Sales x5) — dihindari. Commit `77c9b6b` core / `607e051` sales-module.
- Hasil: openapi hanya 1 tag (`api/v1`), 0 endpoint di grup `Endpoints`, 35 path;
  sidebar HTML: `api/v1` → subgroup → endpoint.

### Sidebar collapsible (tambahan setelah menu api/v1)

Tema Scribe v4 tidak punya klik-untuk-collapse pada heading grup (hanya scrollspy —
grup aktif selalu terbuka). Dengan satu grup top-level, sidebar terkesan permanen
terbuka. Solusi: `scripts/post-scribe-inject.sh` (repo core) meng-inject JS kecil ke
`index.html` hasil generate (idempoten):
- klik heading grup level-1 → expand/collapse subheader
- klik heading subgroup level-2 → expand/collapse endpoint-nya (accordion penuh)
- ikon caret ▸/▾ tersinkron dua arah (klik + scrollspy) via MutationObserver
- state tersimpan di localStorage (bertahan saat reload)
- **WAJIB dijalankan SETELAH setiap `php artisan scribe:generate --force`**
- Teruji fungsional via jsdom: 15/15 PASS (commit `a0b7ec3` core / `2af5470` apidocs)
