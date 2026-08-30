# Diskusi Arsitektur Repo — Core Generik + 25 Modul + Frontend

Status: **DISKUSI** (belum keputusan final)
Tanggal: 30 Agustus 2026
Lokasi: repo `wasnaker-porting-docs` (bukan core — porting/analisis docs terpisah)

---

## Konteks

- Core (`wasnaker-core`) ternyata **90% generik** — layak dipakai app mana pun,
  bukan hanya isnaker. Target arsitektur dari awal (resume-migrasi): "satu
  backend/business logic yang dapat digunakan oleh berbagai client".
- Core berisi infrastruktur lintas-modul: SettingService, ActivityLogService,
  HasMetaData, FileService, RelationService, Mail/Pdf/Sms/QrCode/Excel/Tag/Gdpr/
  NumberToWord/PaymentService, ModuleService (nwidart), API versioning v1,
  Sanctum, Scribe, list API query-builder, Realtime Reverb.
- Yang spesifik isnaker: branding (APP_NAME), Scribe output path, modul Sales,
  remote repo — semua di lapisan luar, mudah diganti.
- Frontend: satu SPA (Next.js) — sudah pernah dibuat, belum di-update.
- Ada **25 modul bisnis** yang perlu di-port dari PerfexCRM (Customers, Leads,
  Proposals, Estimates, Invoices, Credit Notes, Payments, Subscriptions,
  Contracts, Expenses, Invoice Items, Taxes, Currencies, Projects, Tasks, dll —
  lihat `identifikasi-core-perfex.md`).

---

## Topik 1 — Nama Core Generik

Core adalah **API-only + Modular Monolith** (kombinasi #2 dan #8 dari daftar
pola Laravel). Nama yang diusulkan:

**`laravel-modular-api`** (repo: `wasnaker/laravel-modular-api`)

- "modular" = nilai jual utama: pasang-copot modul bisnis via nwidart
- "api" = bentuk headless/API-only
- Alternatif terpendek: `laravel-api-core` (kehilangan sinyal modular)
- Package name (bila jadi composer package): `naker/laravel-modular-api`

Deskripsi (gabungan):
> API-only modular core untuk Laravel — infrastruktur lintas-modul (settings,
> activity log, meta, files, relations, mail, pdf, sms, qr-code, excel, tags,
> gdpr, payment gateway, module manager) + API versioning v1 + Sanctum + Scribe
> docs + list API query-builder + realtime Reverb. Siap dipasangi modul bisnis
> via nwidart/laravel-modules. Core TIDAK pernah berisi kode modul — modul
> hidup terpisah dan di-mount.

---

## Topik 2 — Dilema Jumlah Repo (25 Modul + Core + Frontend)

Pertanyaan: dengan API yang konsisten (satu core) dan frontend satu repo,
apakah tiap modul butuh 2 repo (backend + frontend)? Atau monorepo?

### Analisis: modul = konsep BACKEND, bukan frontend

- Modul nwidart = kode PHP (models, controllers, services, routes, migrations,
  events) di `modules/<Name>/`.
- Frontend SPA TIDAK butuh "repo modul" terpisah — modul frontend cukup
  feature folder di dalam satu repo frontend (mis. `features/sales/`,
  `features/projects/`). **Jadi "2 repo per modul" adalah false dilemma** —
  frontend tetap 1 repo apa pun keputusannya.
- Yang dipertanyakan sebenarnya: backend modul di-monorepo atau per-repo.

### Opsi

**A. 2 repo per modul (backend + frontend)** — 50+ repo
- ❌ Overhead besar: 25 repo × (CI, versioning, sync) untuk 1 produk internal.
- ❌ Perubahan lintas modul = PR lintas repo. Tidak direkomendasikan.

**B. Monorepo penuh (backend + frontend + modul, 1 repo)**
- ✅ Satu PR bisa sentuh core + modul + frontend; atomic.
- ⚠️ Stack campur (PHP + Node) → tooling monorepo (composer path repo + turborepo/
  nx) lebih rumit; CI dan deploy backend/frontend tercampur.
- Layak kalau tim kecil ingin satu tempat segalanya.

**C. REKOMENDASI — Backend monorepo + frontend terpisah (2 repo utama)**
```
laravel-modular-api/          # repo backend monorepo
├── app/                      # core (generik, tanpa kode modul)
├── modules/                  # 25 modul bisnis (nwidart) — mount di sini
│   ├── Sales/
│   ├── Customers/
│   ├── Projects/
│   └── ...
└── routes/ database/ ...

wasnaker-frontend/            # repo SPA (Next.js)
└── features/                 # feature folder per modul (bukan repo terpisah)
    ├── sales/
    ├── customers/
    └── ...

wasnaker-porting-docs/        # docs/analisis/tracker (sudah ada)
apidocs.*.lan/                # output Scribe per instance (sudah ada)
```
- ✅ nwidart native scan `modules/` di dalam app — nol infrastruktur tambahan.
- ✅ Commit lintas core+modul atomic; CI tunggal untuk backend.
- ✅ Frontend siklus sendiri (stack beda, deploy beda).
- ✅ Modules komunikasi via Events/interfaces — core tetap tidak kenal modul
  (hard rule tetap berlaku di monorepo).

### Kapan naik ke repo per-modul?
Kalau modul akan dipakai lintas app/klien berbeda dengan siklus rilis sendiri
(jadi produk reusable) → ekstrak per-modul jadi composer package
(`naker/module-sales`, dst). **YAGNI sekarang** — 1 produk internal, monorepo
backend cukup.

### Trade-off yang jujur
- Monorepo backend: semua modul naik versi bersama-sama (coupling rilis) —
  untuk 1 produk internal ini justru keuntungan (satu deploy, satu versi API).
- Multi-repo per modul: isolasi rilis, tapi biaya operasional 25× lipat.

---

## Topik 3 — Opini: Laravel + Inertia vs API-only + Next.js

Inertia = **paradigma berbeda** dari rencana kita sekarang: Laravel jadi satu
aplikasi penuh (server-rendered pages, React/Vue/Svelte di-hydrate via adapter
Inertia), controller return Inertia response, data lewat props, auth session —
TIDAK ada lapisan REST API antara frontend dan backend.

### Perbandingan jujur

| Kriteria | Inertia (monolith modern) | API-only + Next.js (rencana sekarang) |
|----------|---------------------------|---------------------------------------|
| Kecepatan shipping CRUD (25 modul form-heavy) | ⚡ Sangat cepat — tanpa lapisan API, tanpa state management, tanpa fetch boilerplate; Ziggy untuk route | Lebih lambat — tiap fitur butuh endpoint + Scribe + fetch + state |
| Multi-client (mobile, API publik, integrasi) | ❌ Bukan untuk ini — frontend terikat ke server (session, satu origin) | ✅ Justru kekuatannya |
| Tim frontend/backend paralel | Satu tim, satu repo, satu deploy | Bisa terpisah, deploy independen |
| Realtime (Reverb/Echo) | Bisa (Echo), tapi SPA lebih alami | Natural |
| Kontrol UX/state kompleks (kanban, drag-drop, chat) | Cukup (React tetap dipakai) | Maksimal |
| Complexity | Rendah (satu origin, satu auth) | Tinggi (dua origin, token auth) |

### Posisi saya

1. **Inertia tidak menggantikan API** — dia menggantikan *SPA terpisah*.
   Kalau target punya client non-browser (mobile, integrasi, API publik),
   API-only tetap wajib; Inertia hanya mengubah frontend utama.

2. **Untuk 25 modul CRUD internal (pola Perfex: form-heavy admin panel),
   Inertia adalah pilihan yang lebih lazy dan produktif** daripada
   Next.js + API. Tanpa lapisan API, tiap modul = model + controller +
   Inertia page — bukan model + controller + endpoint + docs + fetch + state.

3. **Keputusan backend TIDAK berubah**: core modular (`laravel-modular-api`)
   tetap dipakai apa pun pilihan frontend. Modul nwidart jalan sama di app
   Inertia (web routes) maupun API-only. Inertia menyentuh frontend, bukan
   arsitektur backend.

4. **Jangan campur tanpa alasan**: Inertia untuk panel + API untuk eksternal
   = dua surface, dua auth (session + token) — kompleksitas ganda. Terima
   kalau memang butuh keduanya (panel internal + API publik), bukan karena
   ragu.

5. **Biaya konversi**: frontend Next.js sudah dibuat (SPA catch-all di nginx
   + web.php fallback). Pindah ke Inertia = hapus fallback SPA, pasang
   Inertia middleware + Ziggy, tulis ulang halaman sebagai Inertia pages.
   Balik arah yang harus diperhitungkan.

### Rekomendasi

- Pertahankan core **API-only versioned** (keputusan sudah benar & sudah
  dibangun; Scribe/Sanctum/multi-client tetap bernilai untuk client lain).
- Untuk frontend utama: putuskan berdasarkan **ada/tidaknya client
  non-browser**:
  - Hanya browser internal → **Inertia** (lebih cepat, lebih sedikit kode)
  - Ada mobile/API publik/third-party → **Next.js terpisah** (rencana sekarang)
- Jika ragu: Next.js + API lebih aman untuk masa depan multi-client, dan
  tidak perlu dibongkar — Inertia bisa dievaluasi per-modul nanti.

---

## Open Questions (belum diputuskan)

1. Nama final: `laravel-modular-api` vs `laravel-api-core` — pilih satu.
2. Frontend: repo terpisah (rekomendasi) vs ikut monorepo penuh (Opsi B).
3. Frontend: **Inertia (monolith) vs Next.js (SPA)** — tergantung ada/tidaknya
   client non-browser; lihat Topik 3.
4. Rename repo GitHub `lrvl-wasnaker_core` → nama final + update remote lokal
   + composer.json name + APP_NAME + README + default modul dikosongkan.
5. Sales module: tetap di vendor (composer package) atau pindah ke
   `modules/Sales` saat monorepo dibentuk.
