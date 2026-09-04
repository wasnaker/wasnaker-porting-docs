# Analisis: Tampilan Branch — Customer Tab "Branches" vs Profile "My Branch"

Dibuat: 2026-09-04. Sumber: wasnaker-core (backend, staging) + wasnaker-frontend.

## 1. BACKEND

| Aspek | Customer → Tab Branches | Profile → My Branch |
|---|---|---|
| Endpoint | `GET /api/v1/customers/{id}/branches` (CustomerController@branches) | `GET /api/v1/user/company` (ApiController@company) |
| Registrasi route | Via manifest modul (`modules/Customer/manifest.php` → `detail_tabs[].api`) | Route tetap di `routes/api.php` |
| Resolusi data | Berdasarkan `{id}` customer yg dipilih user; gate `allowAccessTo()` | Otomatis by `admin_id` user login (customer dulu, lalu surveyor; kosong → `{type:null, company:null, branches:[]}`) |
| RBAC | Middleware `permission:branch:view\|customer:view-connected` + di controller: full-access lihat semua; caller **surveyor** (view-connected) → **hanya cabang dgn connection ACTIVE** (`connectedCustomerIds`, else `whereIn [0]`); caller non-surveyor non-full → 403 | Tanpa permission tambahan — data selalu milik user sendiri |
| Scope relasi | `Customer::find($id)->branches()` — semua row `type=branch` dgn `parent_id = id` customer yg dipilih | `companyPayload()`: company = HO (row user, atau `parent_id`-nya kalau user = cabang); branches = semua anak HO (user HO) **atau hanya row cabang user** (user cabang) |
| Eager load | `vat, admin:id,name, province:id,name, regency:id,name` | `ENTITY_WITH` (sama: vat/admin/province/regency) |
| Format response | `{ "data": [...] }` — list polos | `{ "type", "company", "entity", "branches" }` — ada konteks posisi user (entity) |

Inti perbedaan backend: **customer = endpoint master-detail multi-role** (siapa pun yg punya akses ke customer bisa lihat cabangnya, dgn aturan view-connected utk surveyor); **profile = self-service** (hanya entity milik user login, tanpa parameter).

## 2. FRONTEND

| Aspek | Customer → Tab Branches | Profile → My Branch |
|---|---|---|
| Arsitektur render | **Generic/data-driven**: `SmallTable` → `TabContent` (fetch `tab.api`, `{id}` diganti id terpilih) → `TabView`; **nol kode khusus branch** di `customers/page.tsx` — tab datang dari `ext.detail_tabs` manifest | **Halaman khusus**: `src/app/(with-layouts)/profile/branch/page.tsx`, render manual `TableRoot` |
| Fetch data | Per active tab di SmallTable (+`refreshKey`) | Hook `useMyCompany()` (`useQuery`, key `["spine","user-company",token]`) |
| Kolom | Otomatis: union `Object.keys` row − `hideKeys`, + renderer `tabCustomValue`: `is_active`→StatusBadge, `parent`→code+name, `admin`/`province`/`regency`→name, `vat`→npwp font-mono | Tetap/hardcode: **Code, Nama(+phone), Wilayah (gabungan provinsi+kabupaten), Admin, Status** (StatusBadge) |
| Aksi per item | Ada: toolbar Edit/Delete + toggle ◀▶ (toolbar SmallTable) | Read-only, tanpa aksi |
| Copy/subtitle | Masih "…tab Branches (master-detail — coming soon)" — **usang** | Dinamis: "Anda terdaftar di cabang ini" (user = branch) vs "total N cabang" |

## 3. Temuan / Anomali UI (customer tab)

1. **Nama cabang tidak tampil**: `tabHideKeys` global di halaman customers menghide `"name"` (dan `"type","parent_id","admin_id","vat_id"`) untuk SEMUA tab non-overview. Di tab Branches efeknya: daftar cabang cuma menunjukkan `code, address, email, phone, vat, province, regency, admin, is_active` — **kolom Nama cabang hilang**, padahal itu info utama. Profile justru menampilkan nama.
2. Subtitle "coming soon" bertentangan dgn kenyataan — backend `branches()` + manifest tab sudah jalan; kemungkinan teks lama saat halaman masih list-only.
3. TabView men-`String()` value objek yg tidak punya customValue → `[object Object]`. Di tab Branches saat ini semua objek (vat/admin/province/regency) kebetulan punya renderer di `detailCustom`, jadi aman — tapi rapuh jika backend menambah key objek baru.

## 4. Kesimpulan

- Backend: dua jalur berbeda secara semantik — customer = lihat cabang customer LAIN (multi-role + connected-filter), profile = lihat cabang company SENDIRI (self). Data relasi sama (self-ref `parent_id`, `type=branch`).
- Frontend: customer = 1 halaman generic yg bisa menampilkan tab apa pun dari manifest; profile = bespoke. Karena generic, fix anomali cukup di config (hideKeys/customValue/subtitle) tanpa kode baru per tab.
