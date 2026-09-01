# Porting Frontend — Spine (nextjs-spine)

Status: **aktif** (mulai 1 Sep 2026)
Target visual: TailAdmin (nextadmin sebagai pembanding)
Prinsip: modul mendaftar (manifest), core merender (registry) — pola dari aplikasi sumber.

## Arsitektur

- Frontend: `laravelspine/nextjs-spine` (Next.js App Router + TS + Tailwind v4)
- Theme: design tokens di `app/globals.css` (semantic, tanpa hardcoded)
- Kontrak modul → frontend: `GET /api/v1/modules/{name}/manifest` → `{menu[], widgets[]}`
- Modul contoh: `laravelspine/boilerplates` (Sample) — HOOK listener + API + manifest

## Checklist

### Theme & Layout
- [x] Design tokens (surface/line/ink/accent/status) — globals.css
- [x] Komponen UI dasar (Button, Input, Card, Badge, PageHeader, dll) — lib/ui.tsx
- [x] Layout 2 panel: Sidebar kiri + konten kanan
- [x] Topbar (judul halaman aktif "Spine / {page}")
- [x] Theme toggle dark/light (next-themes)
- [x] User dropdown di Topbar (Profile/Settings/Logout — data /auth/me)
- [ ] Toggle sidebar (collapse)
- [ ] Search global ⌘K (nunggu hook global_search_*)

### Auth
- [x] Login/Register/Logout/Me — /api/v1/auth/*
- [x] AuthProvider reaktif (user, loading, signIn, logout)

### Dashboard
- [x] Header welcome + info user
- [x] Stat cards (ActivityLogs, Tags)
- [x] Widget area: Activity feed + quick links
- [ ] Widget dari manifest modul (render widgets[] per area)
- [ ] Widget order/visibility per user (padanan dashboard_widgets_order)

### Sidebar
- [x] Menu core statis (Beranda/API/Hook/Tenant) + contoh halaman saat login
- [ ] Menu dari manifest modul (render menu[] semua modul aktif)

### Contoh halaman (API nyata)
- [x] Settings, Meta, Tags, QR Code, Number to Word, PDF, Activity Logs
- [x] Settings dari manifest modul: GET /api/v1/settings/schema → tab + field generic → PUT per key
- [x] Tab core Email (SMTP: host/port/user/pass/encryption/from) + tombol Test SMTP (field type action → /api/v1/mail/test)
- [x] Tab core General, Company Information, Localization (position 5/10/15)
- [x] Tab core PDF (font/size/logo width/heading colors — position 30)
- [x] Tab core Misc (upload size, activity log retention, table defaults — position 40)
- [x] Tab core SMS (driver select + Twilio creds) — SmsService override config dari settings (sms_driver/sms_twilio_*), fallback config/sms.php
- [ ] Tab core Realtime — DEFERRED: bangun saat Reverb dipakai sungguhan
- [ ] Halaman Sample modul (GET/POST /api/v1/sample)

## Catatan keputusan
- Registry menu/widget: config-driven dulu → upgrade ke API-driven (manifest) saat modul di-port. Sudah jalan API-nya; frontend tinggal konsumsi.
- Jangan commit hostname .lan / path internal di repo publik.
