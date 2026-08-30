#!/usr/bin/env python3
"""Generator daftar hook + filter — was.naker-porting-docs.

Menghasilkan dari /www/wwwroot/app.ciptamasjaya.co.id:
1. daftar-hook-lengkap.md        — do_action + apply_filters, dedupe per nama, semua app
2. daftar-hook-before-after.md   — do_action per kejadian (application/ saja, gaya gist)
                                    + section apply_filters per kejadian (application/ saja)

Jalankan: python3 scripts/gen-hooks.py   (dari repo root)
"""
import re, os, collections

APP = '/www/wwwroot/app.ciptamasjaya.co.id'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_LENGKAP = os.path.join(HERE, '..', 'daftar-hook-lengkap.md')
OUT_BA = os.path.join(HERE, '..', 'daftar-hook-before-after.md')

# ---------------- klasifikasi do_action ----------------
SPINE_EVENTS = {
    'sms_trigger_triggered': 'SmsSent',
    'module_installed': 'ModuleInstalled',
    'module_uninstalled': 'ModuleUninstalled',
    'module_activated': 'ModuleActivated',
    'module_deactivated': 'ModuleDeactivated',
    'notification_created': 'NotificationSent',
}
NATIVE_MAP = {
    'after_staff_login': 'Illuminate\\Auth\\Events\\Login',
    'before_staff_login': 'Illuminate\\Auth\\Events\\Login',
    'after_contact_login': 'Illuminate\\Auth\\Events\\Login',
    'before_client_login': 'Illuminate\\Auth\\Events\\Login',
    'after_user_logout': 'Illuminate\\Auth\\Events\\Logout',
    'before_staff_logout': 'Illuminate\\Auth\\Events\\Logout',
    'after_client_logout': 'Illuminate\\Auth\\Events\\Logout',
    'before_contact_logout': 'Illuminate\\Auth\\Events\\Logout',
    'before_user_reset_password': 'Illuminate\\Auth\\Events\\PasswordReset',
    'after_user_reset_password': 'Illuminate\\Auth\\Events\\PasswordReset',
    'forgot_password_email_sent': 'PasswordBroker (native)',
    'set_password_email_sent': 'PasswordBroker (native)',
    'email_template_sent': 'Illuminate\\Mail\\Events\\MessageSent',
    'failed_to_send_email_template': 'Illuminate\\Mail\\Events\\MessageSending',
    'before_send_test_smtp_email': 'Mail test flow (native)',
    'smtp_test_email_success': 'Mail test flow (native)',
    'smtp_test_email_failed': 'Mail test flow (native)',
    'modules_loaded': 'ServiceProvider::boot()',
    'admin_init': 'ServiceProvider::boot()',
}
SPINE_DEFERRED = {
    'before_cron_run': 'cron Spine',
    'after_cron_run': 'cron Spine',
    'before_update_backup_options': 'SettingUpdated saat settings-save',
    'staff_member_created': 'CRUD staff (app konsumen)',
    'staff_member_updated': 'CRUD staff (app konsumen)',
    'staff_member_profile_updated': 'CRUD staff (app konsumen)',
    'staff_member_deleted': 'CRUD staff (app konsumen)',
    'before_delete_staff_member': 'CRUD staff (app konsumen)',
    'edit_logged_in_staff_profile': 'CRUD staff (app konsumen)',
    'staff_profile_access': 'CRUD staff (app konsumen)',
    'before_staff_change_language': 'CRUD staff (app konsumen)',
    'pdf_construct': 'PdfService (lifecycle)',
    'pdf_close': 'PdfService (lifecycle)',
}
FRONTEND_KW = ['html_viewed', '_view', '_tabs', '_tab_', 'sidebar', 'menu', 'widget', 'forms_table',
    '_footer', '_head', '_body', '_css', '_js', 'table_', '_table', 'dashboard', 'calendar', '_modal',
    '_select', '_input', '_link', '_icon', '_page', 'print', '_logo', '_image', '_thumb', '_avatar',
    '_preview', '_export', '_download', 'bulk_action', '_filter', '_search', '_sort', '_column', '_row',
    '_pag', '_chart', '_graph', '_dropdown', '_card', '_list', '_grid', '_panel', '_section', '_banner',
    '_hero', '_nav', '_breadcrumb', '_header', '_title', '_label', '_badge', '_tooltip', '_popover',
    '_toast', '_notification', '_email_preview', '_pdf_', '_map', '_gps', '_signature', '_draw',
    '_canvas', '_upload', '_dropzone', '_editor', '_wysiwyg', '_datepicker', '_select2', '_chosen',
    '_autocomplete', '_slider', '_toggle', '_switch', '_radio', '_checkbox', '_color', '_font', '_theme',
    '_lang', '_locale', '_widgets_order', '_widgets_visibility', '_hidden_table', '_table_columns',
    '_per_page', '_redirect', '_anchor', '_profile_image', '_company_logo', '_favicon', '_iso_logo',
    '_watermark', '_stamp', '_tabs_content', '_tab_content', '_form_start', '_form_end',
    '_container_start', '_heading', '_textarea_content', '_gateways_settings', '_settings_view',
    '_settings_group', '_settings_fields', '_settings_last_tab', '_email_templates', '_e_sign',
    '_signature_settings', '_options', '_select_options', '_after_profile', '_navigation_after',
    '_login_form', '_authentication_constructor', '_render_permissions', '_system_info',
    '_files_permissions', '_custom_profile', '_client_profile', '_staff_myprofile', '_modal_profile',
    '_pdf_signature', '_action', '_trigger', '_template_close', '_area', '_content', '_render_']
INFRA_KW = ['modules_loaded', 'admin_init', 'before_update_database', 'database_updated', 'app_init',
    '_init', '_boot', '_register', '_autoload', '_migration', '_upgrade', '_version', '_license_key',
    '_cron_', '_queue', '_job', '_worker', '_scheduler', '_health', '_cache_', '_clear_cache', '_flush',
    '_optimize', '_deploy', '_env', '_config_', '_maintenance', '_debug', '_log_', '_activity_',
    '_audit', '_webhook', '_security', '_captcha', '_session', '_deprecated', '_construct', '_setup',
    '_reset_', '_resetted', 'After_Hooks_Setup', '_hooks_setup', 'before_perform_update',
    'before_system_info', 'before_admin_gdpr_settings', 'pre_upgrade_database', 'pre_uninstall_module',
    'pre_activate_module', 'pre_deactivate_module', 'pre_upload_module', 'auto_upgrade']
SKIP_FORCE = {
    'after_pusher_cluster_option', 'settings_group_end', 'before_save_completed_checklist_visibility',
    'before_start_render_content', 'before_expense_form_template_close', 'after_kb_groups_customers_area',
}

# ---------------- klasifikasi apply_filters ----------------
FILTER_NATIVE = {
    'staff_can': 'Gate/permission (native)',
    'send_email_template_to': 'Mailable (native)',
}
FILTER_SPINE = {
    'pdf_info_and_table_separator': 'PdfService',
    'pdf_signature_break_lines': 'PdfService',
    'proposal_html_pdf_data': 'PdfService',
}
FILTER_KW_NATIVE = ['_can', 'permission', 'is_staff_member', 'has_permission']


def map_action(name):
    if name in SPINE_EVENTS:
        return f"`Spine\\Events\\{SPINE_EVENTS[name]}`", '✅ ported'
    if name in NATIVE_MAP:
        return f"`{NATIVE_MAP[name]}`", '✅ native'
    if name in SPINE_DEFERRED:
        return f"— ({SPINE_DEFERRED[name]})", '⏳ Spine'
    if name.startswith('before_upload_'):
        return '— (validasi FileService)', '⏳ Spine'
    if name.startswith('before_remove_'):
        return '— (menunggu fitur Spine)', '⏳ Spine'
    if name in SKIP_FORCE or any(k in name for k in FRONTEND_KW):
        return '— (frontend Next.js)', 'SKIP'
    if any(k in name for k in INFRA_KW):
        return 'ServiceProvider/Middleware (native)', 'NATIVE'
    return '—', '⏳ modul'


def map_filter(name):
    if name in FILTER_NATIVE:
        return f"`{FILTER_NATIVE[name]}`", '✅ native'
    if name in FILTER_SPINE:
        return f"— ({FILTER_SPINE[name]})", '⏳ Spine'
    if any(k in name for k in FILTER_KW_NATIVE):
        return 'Gate/permission (native)', '✅ native'
    if any(k in name for k in FRONTEND_KW) or name.startswith('_html') or name.endswith('_html') \
            or 'table' in name or 'select' in name or 'option' in name:
        return '— (frontend Next.js)', 'SKIP'
    if any(k in name for k in INFRA_KW):
        return 'ServiceProvider/config (native)', 'NATIVE'
    if name.startswith('pdf_') or '_pdf' in name:
        return '— (PdfService)', '⏳ Spine'
    return 'Pipeline / Eloquent model events', '⏳'


CALL_ACTION = re.compile(r"(hooks\(\)->)?do_action(?:_deprecated)?\(\s*'([^']+)'")
CALL_FILTER = re.compile(r"(hooks\(\)->)?apply_filters(?:_deprecated)?\(\s*'([^']+)'")


def extract(scope_dirs, regex):
    files = collections.OrderedDict()
    for base in scope_dirs:
        for root, dirs, fns in os.walk(os.path.join(APP, base)):
            if any(x in root for x in ('/vendor', '/node_modules', '/backups')):
                continue
            for fn in sorted(fns):
                if not fn.endswith('.php'):
                    continue
                p = os.path.join(root, fn)
                try:
                    src = open(p, encoding='utf-8', errors='ignore').read()
                except OSError:
                    continue
                rows = []
                for m in regex.finditer(src):
                    line = src.count('\n', 0, m.start()) + 1
                    rows.append((line, m.group(2)))
                if rows:
                    files[os.path.relpath(p, APP)] = rows
    return files


def write_lengkap(action_names, filter_names):
    def section(title, items, mapper, with_after=False):
        md = [f"## {title}", ""]
        if with_after:
            md += ["| Hook | Frekuensi | AFTER | Status |", "|---|---|---|---|"]
            for c, n in sorted(items, reverse=True):
                a, s = mapper(n)
                md.append(f"| `{n}` | {c} | {a} | {s} |")
        else:
            md += ["| Hook | Frekuensi |", "|---|---|"]
            for c, n in sorted(items, reverse=True):
                md.append(f"| `{n}` | {c} |")
        md.append("")
        return md

    a1 = [(c, n) for n, c in action_names.items() if map_action(n)[1] == '✅ ported']
    a2 = [(c, n) for n, c in action_names.items() if map_action(n)[1] == '✅ native']
    a3 = [(c, n) for n, c in action_names.items() if map_action(n)[1] == '⏳ Spine']
    a4 = [(c, n) for n, c in action_names.items() if map_action(n)[1] == '⏳ modul']
    b = [(c, n) for n, c in action_names.items() if map_action(n)[1] == 'SKIP']
    c = [(c, n) for n, c in action_names.items() if map_action(n)[1] == 'NATIVE']

    md = ["# Daftar Lengkap Hook & Filter — app.ciptamasjaya.co.id", "",
          f"*Ground truth 30 Agu 2026: **{len(action_names)} hook unik** (`do_action`) + **{len(filter_names)} filter unik** (`apply_filters`) dari `application/` + `modules/`.*", ""]
    md += ["## A. BACKEND — do_action (wajib ada di backend)", ""]
    md += section(f"### A.1 Sudah di-port ke Spine ({len(a1)}) ✅", a1, map_action, with_after=True)
    md += section(f"### A.2 Native Laravel ({len(a2)}) ✅", a2, map_action, with_after=True)
    md += section(f"### A.3 Deferred di Spine ({len(a3)}) ⏳", a3, map_action, with_after=True)
    md += section(f"### A.4 Domain → modul ({len(a4)}) ⏳", a4, map_action)
    md += section(f"## B. FRONTEND / VIEW — SKIP ({len(b)})", b, map_action)
    md += section(f"## C. INFRA / bootstrap — NATIVE ({len(c)})", c, map_action)
    md += section(f"## D. apply_filters() — Pipeline/Eloquent events ({len(filter_names)})", 
                  [(c, n) for n, c in filter_names.items()], map_filter, with_after=True)
    open(OUT_LENGKAP, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    return len(action_names), len(filter_names)


def write_ba(actions, filters):
    total_a = sum(len(r) for r in actions.values())
    total_f = sum(len(r) for r in filters.values())
    md = ["# Hooks & Filters `app.ciptamasjaya.co.id` — application/ (BEFORE → AFTER)", "",
          f"*Ground truth 30 Agu 2026: **{total_a} kejadian do_action** + **{total_f} kejadian apply_filters** di `application/` (modules/ dikecualikan), gaya gist JamesSimpson + kolom AFTER.*", "",
          "Status: `✅ ported` = event Spine, `✅ native` = Laravel bawaan, `⏳ Spine` = menunggu fitur Spine, `⏳ modul` = saat modul di-port, `SKIP` = frontend, `NATIVE` = ServiceProvider/Middleware.", ""]
    md.append("## do_action() — per kejadian")
    md.append("")
    for rel, rows in actions.items():
        md.append(f"### `{rel}`")
        md.append("| Line | Hook (BEFORE) | AFTER (Spine) | Status |"); md.append("|---|---|---|---|")
        for line, name in rows:
            a, s = map_action(name)
            md.append(f"| {line} | `hooks()->do_action('{name}')` | {a} | {s} |")
        md.append("")
    md.append("## apply_filters() — per kejadian")
    md.append("")
    for rel, rows in filters.items():
        md.append(f"### `{rel}`")
        md.append("| Line | Filter (BEFORE) | AFTER (Laravel) | Status |"); md.append("|---|---|---|---|")
        for line, name in rows:
            a, s = map_filter(name)
            md.append(f"| {line} | `hooks()->apply_filters('{name}', …)` | {a} | {s} |")
        md.append("")
    open(OUT_BA, 'w', encoding='utf-8').write('\n'.join(md))
    return total_a, total_f, len(actions), len(filters)


action_names, filter_names = collections.Counter(), collections.Counter()
for rows in extract(('application', 'modules'), CALL_ACTION).values():
    for _, n in rows:
        action_names[n] += 1
for rows in extract(('application', 'modules'), CALL_FILTER).values():
    for _, n in rows:
        filter_names[n] += 1

ta, tf = write_lengkap(action_names, filter_names)
ba, bf, fa, ff = write_ba(extract(('application',), CALL_ACTION), extract(('application',), CALL_FILTER))
print(f"lengkap: {ta} hook + {tf} filter")
print(f"before-after: {ba} kejadian do_action ({fa} file) + {bf} kejadian apply_filters ({ff} file)")
