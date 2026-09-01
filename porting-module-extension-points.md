# Graphify — Peta Modul: Widget, Settings Tab, Menu (query graph modules)

Sumber: graph `graph-app-ciptamasjaya-modules` (20 file utama modul, 180 nodes).
Metode: query node dengan kata kunci `add_dashboard_widget` / `settings_tab` / `menu_admin_items` / `activation_hook`.
Tanggal: 1 Sep 2026.

## Tabel modul → extension point

| Modul | Dashboard widget | Settings tab | Menu admin | Activation hook | Permissions |
|---|---|---|---|---|---|
| billings | ✅ `billings_add_dashboard_widget` | ✅ `billings_settings_tab` | — | — | — |
| cmj_dashboards | ✅ `cmj_dashboards_add_dashboard_widget` | — | — | ✅ `module_activation_hook` | — |
| goals | ✅ `goals_add_dashboard_widget` | — | — | — | — |
| inspections | ✅ `inspections_add_dashboard_widget` | ✅ `inspections_settings_tab` | — | — | — |
| jobreports | ✅ `jobreports_add_dashboard_widget` | ✅ `jobreports_settings_tab` | — | — | — |
| licences | ✅ `licences_add_dashboard_widget` | ✅ `licences_settings_tab` | — | — | — |
| offices | ✅ `offices_add_dashboard_widget` | ✅ `offices_settings_tab` | — | — | — |
| perfex_dashboard | — | — | ✅ `module_menu_admin_items` | ✅ `module_activation_hook` | ✅ `permissions` |
| quotations | ✅ `quotations_add_dashboard_widget` | ✅ `quotations_settings_tab` | — | — | — |
| schedules | ✅ `schedules_add_dashboard_widget` | ✅ `schedules_settings_tab` | — | — | — |
| scorecards | — | ✅ `scorecards_settings_tab` | — | — | — |
| surveys | — | ✅ `survey_cron_settings_tab` + `_content` | — | — | — |
| telegrams | — | ✅ `telegrams_settings_tab` | — | — | — |

## Pola yang terkonfirmasi

1. **Widget + settings tab berdampingan**: hampir semua modul bisnis (billings, inspections, jobreports, licences, offices, quotations, schedules) mendaftarkan keduanya sekaligus — `_add_dashboard_widget()` + `_settings_tab()`.
2. **Variasi per modul**: goals (hanya widget), telegrams/scorecards/surveys (hanya settings), perfex_dashboard (menu + activation + permissions, bukan widget/settings).
3. **Kontrak manifest Spine menangkap pola ini**: `menu[]` + `widgets[]` + `settings[]` di manifest modul — field opsional, mengakomodasi variasi di atas.

## Implikasi porting

- Saat porting modul bisnis (inspections, billings, licences, dll): manifest harus isi `widgets[]` DAN `settings[]`.
- `perfex_dashboard` = contoh modul yang menambah menu sidebar — manifest `menu[]`.
- Graph ini tersedia di `graph-app-ciptamasjaya-modules.html` (lihat dashboard graphify internal).
