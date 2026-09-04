# Usulan Fix: Fenomena "Berdenyut" pada Tab Branch (Customers) vs "Flicker Halus" (Profile My Branch)

Tanggal: 2026-09-04 · Repo: wasnaker-frontend (staging) · Status: **usulan — belum diterapkan**

## 1. Fenomena (laporan user)

- Membuka tab **Branches** di menu Customers utk sebuah record yg belum pernah dibuka
  = terasa **"berdenyut"** (area konten mati/skeleton dulu, lalu muncul penuh).
  4 record customer → 4 denyut saat pertama dibuka.
- Membuka ulang record yg sama = **flicker halus** (langsung tampil, seperti
  membuka My Branch di Profile).
- Record ke-4 yg belum pernah dibuka = berdenyut lagi.
- Redis (LXC 113), Varnish (LXC 112), Laravel Octane TIDAK menghilangkan denyut —
  hanya sedikit menguranginya.

## 2. Diagnosis (akar masalah — dari kode)

Lokasi: `src/components/spine/tab-content.tsx` (komponen fetch tab generik,
dipakai SEMUA tab SEMUA halaman via SmallTable).

```ts
// baris 53-61
const { data, isPending, isError, error } = useQuery({
  queryKey: ["spine", "tab", url, refreshKey],   // ← key = URL endpoint
  queryFn: async () => { ... },
  enabled: inlineData === undefined,
});
// baris 68
if (isPending && !data) return <TabSkeleton />;  // ← fase kosong = denyut
```

Mekanisme denyut:
1. `queryKey` berisi `url` → tiap record punya key sendiri
   (`/customers/1/branches`, `/customers/2/branches`, …).
2. Record pertama kali dibuka = **cache miss** → fetch jaringan → `isPending && !data`
   → render `<TabSkeleton />` → konten mati (skeleton) lalu hidup (tabel) = 1 denyut.
3. Record yg pernah dibuka = cache React Query panas → `data` langsung ada →
   render tabel tanpa skeleton = flicker halus.
4. Kenapa infra tidak menyembuhkan: denyut = **cache miss + fase skeleton di
   CLIENT**, bukan latency server murni. Octane/Varnish/Redis hanya memperpendek
   fase skeleton ("sedikit mengurangi" — sesuai pengamatan), fase kosong tetap ada
   utk setiap key baru. API auth dinamis juga tidak di-cache Varnish.

Pembanding yg selalu halus — Profile My Branch (`use-my-company.ts`):
`queryKey: ["spine", "user-company", token]` → key STABIL, tidak bergantung URL
record; sekali load, selalu dari cache. Tidak pernah cold → tidak pernah denyut.

## 3. Usulan Fix (1 baris, root cause)

File: `src/components/spine/tab-content.tsx`

```ts
const { data, isPending, isError, error } = useQuery({
  queryKey: ["spine", "tab", url, refreshKey],
  queryFn: async () => {
    const res = await api<{ data?: unknown }>(url);
    if (!res.ok) throw new Error(res.error ?? "Gagal memuat");
    return res.data?.data ?? res.data;
  },
  enabled: inlineData === undefined,
  placeholderData: (prev) => prev,   // ← data lama tetap tampil selama fetch
});
```

Efek: saat ganti record (key baru, cache miss), React Query v5 menampilkan data
query sebelumnya sebagai placeholder → tabel lama tetap terlihat selama fetch →
konten berganti langsung, TANPA skeleton → denyut hilang, semua record terasa
seperti flicker halus. Berlaku utk semua tab semua halaman (1 titik fix).

Catatan:
- React Query v5 (`^5.101.2`) — pola `placeholderData: (prev) => prev` adalah
  penerus `keepPreviousData` v4. Tidak perlu versi lain.
- Perilaku setelah Edit (refreshKey naik): data lama (sebelum edit) tampil sesaat
  saat refetch — konsisten dgn pola SWR yg sudah dikomentari di file.
- Opsional lanjutan (jika masih terasa): `staleTime` kecil + prefetch record
  tetangga di SmallTable; TIDAK wajib utk menghilangkan denyut.

## 5. Lampiran Kode — Before / After (untuk evaluasi & jejak)

### 5.1 Fix 1 (root fix) — `src/components/spine/tab-content.tsx`

BEFORE:
```tsx
  const { data, isPending, isError, error } = useQuery({
    queryKey: ["spine", "tab", url, refreshKey],
    queryFn: async () => {
      const res = await api<{ data?: unknown }>(url);
      if (!res.ok) throw new Error(res.error ?? "Gagal memuat");
      return res.data?.data ?? res.data;
    },
    enabled: inlineData === undefined,
  });
```

AFTER:
```tsx
  const { data, isPending, isError, error } = useQuery({
    queryKey: ["spine", "tab", url, refreshKey],
    queryFn: async () => {
      const res = await api<{ data?: unknown }>(url);
      if (!res.ok) throw new Error(res.error ?? "Gagal memuat");
      return res.data?.data ?? res.data;
    },
    enabled: inlineData === undefined,
    // Denyut fix: ganti record (key baru/cache miss) -> data query sebelumnya
    // tetap tampil sebagai placeholder selama fetch. Tidak ada fase skeleton.
    // (React Query v5: pengganti keepPreviousData v4.)
    placeholderData: (prev) => prev,
  });
```

### 5.2 Fix 2 (opsional, AJAX proaktif/prefetch) — `src/app/(with-layouts)/customers/page.tsx`

Pola: begitu daftar customer dimuat / seleksi berubah, panaskan cache tab
Branches utk record lain di daftar. Saat record dibuka, data sudah ada -> halus
bahkan utk record pertama kali dibuka. (di file ini `qc`, `items`, `selectedId`,
`refreshKey`, `api`, `tabs` sudah tersedia; `tabs` dari manifest via
`useModuleExtensions`.)

BEFORE: (tidak ada prefetch — fetch terjadi hanya saat tab dirender)

AFTER — sisipkan setelah definisi `selectItem`:
```tsx
  // AJAX proaktif: panaskan cache tab branches record lain di daftar.
  // Record tetangga (sebelum/sesudah yg dipilih) — hemat & tepat sasaran.
  useEffect(() => {
    if (selectedId == null || items.length === 0) return;
    const branchTab = tabs.find((t) => t.api?.includes("/branches"));
    if (!branchTab?.api) return;
    const idx = items.findIndex((it) => it.id === Number(selectedId));
    if (idx < 0) return;
    for (const offset of [-1, 1]) {
      const neighbour = items[idx + offset];
      if (!neighbour) continue;
      const url = branchTab.api.replace("{id}", String(neighbour.id));
      void qc.prefetchQuery({
        queryKey: ["spine", "tab", url, refreshKey],
        queryFn: async () => {
          const res = await api<{ data?: unknown }>(url);
          if (!res.ok) throw new Error(res.error ?? "Gagal memuat");
          return res.data?.data ?? res.data;
        },
        staleTime: 30_000,
      });
    }
  }, [qc, items, tabs, selectedId, refreshKey]);
```

Catatan evaluasi Fix 2:
- Butuh tambahan `useEffect` di import react (baris 3: `import { useMemo, useState } from "react"` → tambah `useEffect`).
- queryKey/queryFn harus IDENTIK dgn TabContent (`["spine","tab",url,refreshKey]` + parsing `res.data?.data ?? res.data`) agar cache-nya sama. Duplikasi queryFn di 2 tempat = risiko drift; kalau diputuskan permanen, extract ke satu helper kecil (mis. `fetchTab(url)`) di `services/spine/`.
- Varian lebih boros: prefetch SEMUA record halaman utk semua tab manifest (tanpa filter tetangga) — hanya disarankan kalau jumlah record per halaman kecil (seperti kasus 4 record user).
- staleTime 30s: hasil prefetch dianggap segar 30 detik → tidak refetch ulang saat dibuka cepat.

## 6. Verifikasi setelah diterapkan (sama utk Fix 1 & Fix 2)

1. Buka record customer 1 → tab Branches: denyut hilang (langsung isi/skeleton hanya saat benar-benar belum ada data sama sekali utk tab itu).
2. Ganti cepat record 1→2→3→4: semua mulus tanpa skeleton di antara.
3. Edit record → refreshKey: data lama tampil sesaat lalu terganti (bukan blank).
4. Halaman lain yg pakai tab generik (Activity, modul lain) ikut terasa halus.
