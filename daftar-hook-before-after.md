# Hooks `app.ciptamasjaya.co.id` — application/ (BEFORE → AFTER)

*Ground truth: setiap pemanggilan `do_action()` di **`application/`** (modules/ dikecualikan), 30 Agu 2026 — **418 kejadian**, 150 file. Pola: gist JamesSimpson (per file + nomor baris) + kolom AFTER.*

Status: `✅ ported` = event Spine sudah dibuat, `✅ native` = pakai event Laravel bawaan, `⏳` = ditunda (fitur/modul belum dibangun), `SKIP` = frontend (API-only), `NATIVE` = ServiceProvider/Middleware.

## `application/core/AdminController.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 13 | `hooks()->do_action('pre_upgrade_database')` | ServiceProvider/Middleware (native) | NATIVE |
| 21 | `hooks()->do_action('pre_admin_init')` | ServiceProvider/Middleware (native) | NATIVE |
| 73 | `hooks()->do_action('admin_init')` | `ServiceProvider::boot()` | ✅ native |

## `application/core/App_Controller.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 93 | `hooks()->do_action('app_init')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/core/App_Model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('model_init')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/helpers/admin_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_admin_head')` | — (frontend Next.js) | SKIP |
| 22 | `hooks()->do_action_deprecated('after_js_scripts_render')` | — (frontend Next.js) | SKIP |
| 24 | `hooks()->do_action('app_admin_footer')` | — (frontend Next.js) | SKIP |
| 215 | `hooks()->do_action('after_load_admin_language')` | — (frontend Next.js) | SKIP |

## `application/helpers/assets_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_admin_assets')` | — | ⏳ modul |
| 16 | `hooks()->do_action('app_client_assets')` | — | ⏳ modul |
| 18 | `hooks()->do_action('app_client_assets_added')` | — | ⏳ modul |
| 87 | `hooks()->do_action('app_admin_assets_added')` | — | ⏳ modul |

## `application/helpers/clients_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 734 | `hooks()->do_action('after_load_client_language')` | — (frontend Next.js) | SKIP |

## `application/helpers/database_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 108 | `hooks()->do_action('notification_created')` | — | ⏳ modul |

## `application/helpers/deprecated_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('deprecated_function_run')` | — | ⏳ modul |
| 36 | `hooks()->do_action('deprecated_hook_run')` | — | ⏳ modul |

## `application/helpers/general_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 20 | `hooks()->do_action('before_generate_short_link')` | — (frontend Next.js) | SKIP |
| 61 | `hooks()->do_action('before_archive_short_link')` | — (frontend Next.js) | SKIP |

## `application/helpers/invoices_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 387 | `hooks()->do_action('invoice_status_changed')` | — | ⏳ modul |

## `application/helpers/pdf_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 37 | `hooks()->do_action('load_pdf_language')` | — (frontend Next.js) | SKIP |

## `application/helpers/template_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 284 | `hooks()->do_action('app_external_form_head')` | — (frontend Next.js) | SKIP |

## `application/helpers/themes_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 133 | `hooks()->do_action_deprecated('customers_after_js_scripts_load')` | — (frontend Next.js) | SKIP |
| 135 | `hooks()->do_action('app_customers_footer')` | — (frontend Next.js) | SKIP |
| 153 | `hooks()->do_action('app_customers_head')` | — (frontend Next.js) | SKIP |

## `application/helpers/upload_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 39 | `hooks()->do_action('before_upload_estimate_request_attachment')` | — | ⏳ validasi FileService |
| 117 | `hooks()->do_action('before_upload_newsfeed_attachment')` | — | ⏳ validasi FileService |
| 165 | `hooks()->do_action('before_upload_project_attachment')` | — | ⏳ validasi FileService |
| 277 | `hooks()->do_action('before_upload_contract_attachment')` | — | ⏳ validasi FileService |
| 511 | `hooks()->do_action('before_upload_client_attachment')` | — | ⏳ validasi FileService |
| 567 | `hooks()->do_action('before_upload_expense_attachment')` | — | ⏳ validasi FileService |
| 602 | `hooks()->do_action('before_upload_ticket_attachment')` | — | ⏳ validasi FileService |
| 655 | `hooks()->do_action('before_upload_company_logo_attachment')` | — | ⏳ validasi FileService |
| 709 | `hooks()->do_action('before_upload_signature_image_attachment')` | — | ⏳ validasi FileService |
| 752 | `hooks()->do_action('before_upload_favicon_attachment')` | — | ⏳ validasi FileService |
| 789 | `hooks()->do_action('before_upload_staff_profile_image')` | — | ⏳ validasi FileService |
| 857 | `hooks()->do_action('before_upload_contact_profile_image')` | — | ⏳ validasi FileService |
| 938 | `hooks()->do_action('before_upload_project_discussion_comment_attachment')` | — | ⏳ validasi FileService |

## `application/hooks/InitHook.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 55 | `hooks()->do_action('modules_loaded')` | `ServiceProvider::boot()` | ✅ native |

## `application/controllers/Authentication.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('clients_authentication_constructor')` | — (frontend Next.js) | SKIP |
| 61 | `hooks()->do_action('after_contact_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 180 | `hooks()->do_action('after_client_register')` | ServiceProvider/Middleware (native) | NATIVE |
| 202 | `hooks()->do_action('after_client_register_logged_in')` | ServiceProvider/Middleware (native) | NATIVE |
| 267 | `hooks()->do_action('before_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 280 | `hooks()->do_action('after_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 301 | `hooks()->do_action('after_client_logout')` | `Illuminate\Auth\Events\Logout` | ✅ native |

## `application/controllers/Clients.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('after_clients_area_init')` | ServiceProvider/Middleware (native) | NATIVE |
| 1139 | `hooks()->do_action('before_remove_contact_profile_image')` | — | ⏳ menunggu fitur Spine |

## `application/controllers/Contacts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 30 | `hooks()->do_action('after_clients_area_init')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/controllers/Contract.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 77 | `hooks()->do_action('contract_html_viewed')` | — (frontend Next.js) | SKIP |

## `application/controllers/Download.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 39 | `hooks()->do_action('before_output_preview_video')` | — (frontend Next.js) | SKIP |
| 83 | `hooks()->do_action('before_output_preview_image')` | — (frontend Next.js) | SKIP |

## `application/controllers/Estimate.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 91 | `hooks()->do_action('estimate_html_viewed')` | — (frontend Next.js) | SKIP |

## `application/controllers/Forms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 178 | `hooks()->do_action('estimate_requests_created')` | — | ⏳ modul |
| 242 | `hooks()->do_action('estimate_request_form_submitted')` | — | ⏳ modul |
| 464 | `hooks()->do_action('after_add_task')` | — | ⏳ modul |
| 490 | `hooks()->do_action('lead_created')` | — | ⏳ modul |
| 564 | `hooks()->do_action('web_to_lead_form_submitted')` | — | ⏳ modul |
| 784 | `hooks()->do_action('ticket_form_submitted')` | — | ⏳ modul |

## `application/controllers/Invoice.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 77 | `hooks()->do_action('invoice_html_viewed')` | — (frontend Next.js) | SKIP |

## `application/controllers/Knowledge_base.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('customers_area_knowledge_base_construct')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/controllers/Proposal.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 96 | `hooks()->do_action('proposal_html_viewed')` | — (frontend Next.js) | SKIP |

## `application/controllers/Verification.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 51 | `hooks()->do_action('contact_email_verified_but_requires_admin_confirmation')` | — | ⏳ modul |
| 55 | `hooks()->do_action('contact_email_verified')` | — | ⏳ modul |

## `application/controllers/admin/Authentication.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 23 | `hooks()->do_action('admin_auth_init')` | ServiceProvider/Middleware (native) | NATIVE |
| 81 | `hooks()->do_action('after_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 112 | `hooks()->do_action('after_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 123 | `hooks()->do_action('after_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 171 | `hooks()->do_action('before_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 179 | `hooks()->do_action('after_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 228 | `hooks()->do_action('after_user_logout')` | `Illuminate\Auth\Events\Logout` | ✅ native |

## `application/controllers/admin/Auto_update.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('before_perform_update')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/controllers/admin/Clients.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 645 | `hooks()->do_action('after_contact_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 873 | `hooks()->do_action('before_do_bulk_action_for_customers')` | — (frontend Next.js) | SKIP |

## `application/controllers/admin/Emails.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 240 | `hooks()->do_action('before_send_test_smtp_email')` | `Mail test flow (native)` | ✅ native |
| 272 | `hooks()->do_action('smtp_test_email_success')` | `Mail test flow (native)` | ✅ native |
| 276 | `hooks()->do_action('smtp_test_email_failed')` | `Mail test flow (native)` | ✅ native |

## `application/controllers/admin/Expenses.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 125 | `hooks()->do_action('before_do_bulk_action_for_expenses')` | — (frontend Next.js) | SKIP |

## `application/controllers/admin/Invoice_items.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 172 | `hooks()->do_action('before_do_bulk_action_for_items')` | — (frontend Next.js) | SKIP |

## `application/controllers/admin/Leads.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 600 | `hooks()->do_action('lead_converted_to_customer')` | — | ⏳ modul |
| 1264 | `hooks()->do_action('before_do_bulk_action_for_leads')` | — (frontend Next.js) | SKIP |

## `application/controllers/admin/Misc.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 497 | `hooks()->do_action('before_change_maximum_number_of_digits_to_decimal_fields')` | — | ⏳ modul |
| 539 | `hooks()->do_action('before_change_decimal_places')` | — | ⏳ modul |

## `application/controllers/admin/Newsfeed.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 371 | `hooks()->do_action('before_pin_post')` | — | ⏳ modul |
| 381 | `hooks()->do_action('before_unpin_post')` | — | ⏳ modul |
| 458 | `hooks()->do_action('before_delete_post')` | — | ⏳ modul |

## `application/controllers/admin/Projects.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 715 | `hooks()->do_action('before_do_bulk_action_for_project_files')` | — (frontend Next.js) | SKIP |

## `application/controllers/admin/Proposals.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 357 | `hooks()->do_action('proposal_converted_to_estimate')` | — | ⏳ modul |
| 387 | `hooks()->do_action('proposal_converted_to_invoice')` | — | ⏳ modul |

## `application/controllers/admin/Settings.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 175 | `hooks()->do_action('before_remove_company_logo')` | — | ⏳ menunggu fitur Spine |
| 197 | `hooks()->do_action('before_remove_favicon')` | — | ⏳ menunggu fitur Spine |

## `application/controllers/admin/Staff.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 27 | `hooks()->do_action('staff_member_edit_view_profile')` | — (frontend Next.js) | SKIP |
| 119 | `hooks()->do_action('before_save_dashboard_widgets_order')` | — (frontend Next.js) | SKIP |
| 132 | `hooks()->do_action('before_save_dashboard_widgets_visibility')` | — (frontend Next.js) | SKIP |
| 148 | `hooks()->do_action('before_save_hidden_table_columns')` | — (frontend Next.js) | SKIP |
| 157 | `hooks()->do_action('before_staff_change_language')` | — | ⏳ menunggu fitur Spine |
| 208 | `hooks()->do_action('edit_logged_in_staff_profile')` | — | ⏳ menunggu fitur Spine |
| 246 | `hooks()->do_action('before_remove_staff_profile_image')` | — | ⏳ menunggu fitur Spine |
| 288 | `hooks()->do_action('staff_profile_access')` | — | ⏳ menunggu fitur Spine |
| 442 | `hooks()->do_action('before_save_completed_checklist_visibility')` | — | ⏳ modul |

## `application/controllers/admin/Tasks.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 151 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 578 | `hooks()->do_action('task_checklist_item_finished')` | — | ⏳ modul |
| 887 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 936 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 1111 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 1117 | `hooks()->do_action('before_do_bulk_action_for_tasks')` | — (frontend Next.js) | SKIP |

## `application/controllers/admin/Tickets.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 684 | `hooks()->do_action('before_do_bulk_action_for_tickets')` | — (frontend Next.js) | SKIP |

## `application/controllers/gateways/Stripe.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 210 | `hooks()->do_action('customer_subscribed_to_subscription')` | — | ⏳ modul |

## `application/models/Announcements_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 104 | `hooks()->do_action('announcement_created')` | — | ⏳ modul |
| 130 | `hooks()->do_action('announcement_updated')` | — | ⏳ modul |
| 148 | `hooks()->do_action('before_delete_announcement')` | — | ⏳ modul |
| 156 | `hooks()->do_action('announcement_deleted')` | — | ⏳ modul |

## `application/models/Authentication_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 37 | `hooks()->do_action('failed_login_attempt')` | — | ⏳ modul |
| 48 | `hooks()->do_action('non_existent_user_login_attempt')` | — | ⏳ modul |
| 59 | `hooks()->do_action('inactive_user_login_attempt')` | — | ⏳ modul |
| 75 | `hooks()->do_action('before_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 92 | `hooks()->do_action('before_client_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 131 | `hooks()->do_action('before_contact_logout')` | `Illuminate\Auth\Events\Logout` | ✅ native |
| 136 | `hooks()->do_action('before_staff_logout')` | `Illuminate\Auth\Events\Logout` | ✅ native |
| 285 | `hooks()->do_action('set_password_email_sent')` | `PasswordBroker (native)` | ✅ native |
| 347 | `hooks()->do_action('forgot_password_email_sent')` | `PasswordBroker (native)` | ✅ native |
| 541 | `hooks()->do_action('before_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |

## `application/models/Client_groups_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 93 | `hooks()->do_action('customer_group_deleted')` | — | ⏳ modul |

## `application/models/Client_vault_entries_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 99 | `hooks()->do_action('customer_vault_entry_deleted')` | — | ⏳ modul |

## `application/models/Clients_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 197 | `hooks()->do_action('after_client_added')` | — | ⏳ modul |
| 297 | `hooks()->do_action('after_client_updated')` | — | ⏳ modul |
| 418 | `hooks()->do_action('contact_updated')` | — | ⏳ modul |
| 604 | `hooks()->do_action('contact_created')` | — | ⏳ modul |
| 678 | `hooks()->do_action('contact_created')` | — | ⏳ modul |
| 732 | `hooks()->do_action('customer_updated_company_info')` | — | ⏳ modul |
| 844 | `hooks()->do_action('before_client_deleted')` | — | ⏳ modul |
| 1011 | `hooks()->do_action('after_client_deleted')` | — | ⏳ modul |
| 1034 | `hooks()->do_action('before_delete_contact')` | — | ⏳ modul |
| 1198 | `hooks()->do_action('contact_deleted')` | — | ⏳ modul |
| 1318 | `hooks()->do_action('contact_status_changed')` | — | ⏳ modul |
| 1345 | `hooks()->do_action('client_status_changed')` | — | ⏳ modul |
| 1666 | `hooks()->do_action('before_remove_contact_profile_image')` | — | ⏳ menunggu fitur Spine |

## `application/models/Contracts_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 135 | `hooks()->do_action('after_contract_added')` | — | ⏳ modul |
| 186 | `hooks()->do_action('after_contract_updated')` | — | ⏳ modul |
| 416 | `hooks()->do_action('before_contract_deleted')` | — | ⏳ modul |

## `application/models/Credit_notes_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 124 | `hooks()->do_action('credit_note_sent')` | — | ⏳ modul |
| 224 | `hooks()->do_action('after_create_credit_note')` | — | ⏳ modul |
| 353 | `hooks()->do_action('after_update_credit_note')` | — | ⏳ modul |
| 409 | `hooks()->do_action('before_credit_note_deleted')` | — | ⏳ modul |
| 456 | `hooks()->do_action('after_credit_note_deleted')` | — | ⏳ modul |
| 471 | `hooks()->do_action('credit_note_status_changed')` | — | ⏳ modul |
| 634 | `hooks()->do_action('created_credit_note_from_invoice')` | — | ⏳ modul |
| 665 | `hooks()->do_action('credit_note_refund_created')` | — | ⏳ modul |
| 694 | `hooks()->do_action('credit_note_refund_updated')` | — | ⏳ modul |
| 743 | `hooks()->do_action('credit_note_refund_deleted')` | — | ⏳ modul |
| 793 | `hooks()->do_action('credits_applied')` | — | ⏳ modul |

## `application/models/Cron_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 47 | `hooks()->do_action('before_cron_run')` | — | ⏳ menunggu fitur Spine |
| 103 | `hooks()->do_action('after_cron_run')` | — | ⏳ menunggu fitur Spine |
| 303 | `hooks()->do_action('after_ticket_status_changed')` | — | ⏳ modul |
| 408 | `hooks()->do_action('before_check_recurring_tasks')` | — | ⏳ modul |
| 485 | `hooks()->do_action('after_check_recurring_tasks')` | — | ⏳ modul |
| 1380 | `hooks()->do_action('after_add_task')` | — | ⏳ modul |
| 1444 | `hooks()->do_action('existing_lead_email_inserted_from_email_integration')` | — | ⏳ modul |
| 1530 | `hooks()->do_action('lead_created')` | — | ⏳ modul |
| 1532 | `hooks()->do_action('lead_created_from_email_integration')` | — | ⏳ modul |

## `application/models/Departments_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 71 | `hooks()->do_action('after_department_added')` | — | ⏳ modul |
| 153 | `hooks()->do_action('before_delete_department')` | — | ⏳ modul |

## `application/models/Emails_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 487 | `hooks()->do_action('email_template_sent')` | `Illuminate\Mail\Events\MessageSent` | ✅ native |

## `application/models/Estimate_request_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 33 | `hooks()->do_action('estimate_request_assigned_changed')` | — | ⏳ modul |
| 88 | `hooks()->do_action('estimate_request_status_changed')` | — | ⏳ modul |
| 253 | `hooks()->do_action('before_estimate_request_deleted')` | — | ⏳ modul |

## `application/models/Estimates_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 283 | `hooks()->do_action('estimate_converted_to_invoice')` | — | ⏳ modul |
| 551 | `hooks()->do_action('after_estimate_added')` | — | ⏳ modul |
| 777 | `hooks()->do_action('after_estimate_updated')` | — | ⏳ modul |
| 849 | `hooks()->do_action('estimate_accepted')` | — | ⏳ modul |
| 876 | `hooks()->do_action('estimate_declined')` | — | ⏳ modul |
| 974 | `hooks()->do_action('before_estimate_deleted')` | — | ⏳ modul |
| 1268 | `hooks()->do_action('estimate_sent')` | — | ⏳ modul |

## `application/models/Expenses_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 150 | `hooks()->do_action('after_expense_added')` | — | ⏳ modul |
| 418 | `hooks()->do_action('after_expense_updated')` | — | ⏳ modul |
| 634 | `hooks()->do_action('expense_converted_to_invoice')` | — | ⏳ modul |

## `application/models/Invoice_items_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 62 | `hooks()->do_action('item_coppied')` | — | ⏳ modul |
| 178 | `hooks()->do_action('item_created')` | — | ⏳ modul |
| 248 | `hooks()->do_action('item_updated')` | — | ⏳ modul |
| 286 | `hooks()->do_action('item_deleted')` | — | ⏳ modul |

## `application/models/Invoices_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 162 | `hooks()->do_action('invoice_marked_as_cancelled')` | — | ⏳ modul |
| 180 | `hooks()->do_action('invoice_unmarked_as_cancelled')` | — | ⏳ modul |
| 535 | `hooks()->do_action('after_invoice_added')` | — | ⏳ modul |
| 707 | `hooks()->do_action('invoice_copied')` | — | ⏳ modul |
| 1065 | `hooks()->do_action('after_invoice_updated')` | — | ⏳ modul |
| 1141 | `hooks()->do_action('before_invoice_deleted')` | — | ⏳ modul |
| 1417 | `hooks()->do_action('invoice_overdue_reminder_sent')` | — | ⏳ modul |
| 1501 | `hooks()->do_action('invoice_due_reminder_sent')` | — | ⏳ modul |
| 1632 | `hooks()->do_action('invoice_sent')` | — | ⏳ modul |

## `application/models/Leads_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 126 | `hooks()->do_action('lead_created')` | — | ⏳ modul |
| 282 | `hooks()->do_action('lead_status_changed')` | — | ⏳ modul |
| 322 | `hooks()->do_action('before_lead_deleted')` | — | ⏳ modul |
| 415 | `hooks()->do_action('lead_marked_as_lost')` | — | ⏳ modul |
| 476 | `hooks()->do_action('lead_marked_as_junk')` | — | ⏳ modul |
| 824 | `hooks()->do_action('lead_status_changed')` | — | ⏳ modul |

## `application/models/Misc_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 300 | `hooks()->do_action('note_created')` | — | ⏳ modul |
| 310 | `hooks()->do_action('before_update_note')` | — | ⏳ modul |
| 321 | `hooks()->do_action('note_updated')` | — | ⏳ modul |
| 339 | `hooks()->do_action('before_delete_note')` | — | ⏳ modul |
| 351 | `hooks()->do_action('note_deleted')` | — | ⏳ modul |

## `application/models/Payment_modes_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 199 | `hooks()->do_action('before_get_payment_gateways')` | — | ⏳ modul |

## `application/models/Payments_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 363 | `hooks()->do_action('after_payment_added')` | — | ⏳ modul |
| 410 | `hooks()->do_action('before_payment_deleted')` | — | ⏳ modul |
| 477 | `hooks()->do_action('after_payment_added')` | — | ⏳ modul |

## `application/models/Projects_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 479 | `hooks()->do_action('before_remove_project_file')` | — | ⏳ menunggu fitur Spine |
| 851 | `hooks()->do_action('after_add_project')` | — | ⏳ modul |
| 1049 | `hooks()->do_action('project_status_changed')` | — | ⏳ modul |
| 1067 | `hooks()->do_action('after_update_project')` | — | ⏳ modul |
| 1105 | `hooks()->do_action('project_status_changed')` | — | ⏳ modul |
| 1679 | `hooks()->do_action('after_add_discussion_comment')` | — | ⏳ modul |
| 2076 | `hooks()->do_action('project_copied')` | — | ⏳ modul |

## `application/models/Proposals_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 158 | `hooks()->do_action('proposal_created')` | — | ⏳ modul |
| 320 | `hooks()->do_action('after_proposal_updated')` | — | ⏳ modul |
| 742 | `hooks()->do_action('proposal_accepted')` | — | ⏳ modul |
| 750 | `hooks()->do_action('proposal_declined')` | — | ⏳ modul |
| 964 | `hooks()->do_action('proposal_sent')` | — | ⏳ modul |

## `application/models/Staff_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 17 | `hooks()->do_action('before_delete_staff_member')` | — | ⏳ menunggu fitur Spine |
| 321 | `hooks()->do_action('staff_member_deleted')` | — | ⏳ menunggu fitur Spine |
| 489 | `hooks()->do_action('staff_member_created')` | — | ⏳ menunggu fitur Spine |
| 640 | `hooks()->do_action('staff_member_updated')` | — | ⏳ menunggu fitur Spine |
| 692 | `hooks()->do_action('staff_member_profile_updated')` | — | ⏳ menunggu fitur Spine |

## `application/models/Tasks_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 255 | `hooks()->do_action('after_add_task')` | — | ⏳ modul |
| 659 | `hooks()->do_action('after_add_task')` | — | ⏳ modul |
| 795 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 868 | `hooks()->do_action('task_checklist_item_created')` | — | ⏳ modul |
| 1016 | `hooks()->do_action('task_comment_added')` | — | ⏳ modul |
| 1073 | `hooks()->do_action('task_follower_added')` | — | ⏳ modul |
| 1158 | `hooks()->do_action('task_assignee_added')` | — | ⏳ modul |
| 1398 | `hooks()->do_action('task_comment_updated')` | — | ⏳ modul |
| 1447 | `hooks()->do_action('task_comment_deleted')` | — | ⏳ modul |
| 1573 | `hooks()->do_action('task_status_changed')` | — | ⏳ modul |
| 1621 | `hooks()->do_action('task_status_changed')` | — | ⏳ modul |
| 1698 | `hooks()->do_action('task_deleted')` | — | ⏳ modul |
| 1909 | `hooks()->do_action('task_timer_started')` | — | ⏳ modul |
| 2202 | `hooks()->do_action('task_timer_deleted')` | — | ⏳ modul |

## `application/models/Templates_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 28 | `hooks()->do_action('new_template_added')` | — | ⏳ modul |
| 73 | `hooks()->do_action('after_template_updated')` | — | ⏳ modul |
| 86 | `hooks()->do_action('before_template_deleted')` | — | ⏳ modul |
| 93 | `hooks()->do_action('after_template_deleted')` | — | ⏳ modul |

## `application/models/Tickets_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 522 | `hooks()->do_action('after_ticket_status_changed')` | — | ⏳ modul |
| 602 | `hooks()->do_action('after_ticket_reply_added')` | — | ⏳ modul |
| 623 | `hooks()->do_action('before_delete_ticket_reply')` | — | ⏳ modul |
| 940 | `hooks()->do_action('ticket_created')` | — | ⏳ modul |
| 979 | `hooks()->do_action('before_ticket_deleted')` | — | ⏳ modul |
| 1103 | `hooks()->do_action('ticket_settings_updated')` | — | ⏳ modul |
| 1187 | `hooks()->do_action('after_ticket_status_changed')` | — | ⏳ modul |

## `application/services/ViewsTracking.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 47 | `hooks()->do_action('before_insert_views_tracking')` | — (frontend Next.js) | SKIP |

## `application/services/upgrade/Response.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 11 | `hooks()->do_action('auto_upgrade_failed_to_extract_zip_file')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/libraries/App.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 80 | `hooks()->do_action('app_base_after_construct_action')` | — (frontend Next.js) | SKIP |
| 362 | `hooks()->do_action('before_update_database')` | ServiceProvider/Middleware (native) | NATIVE |
| 374 | `hooks()->do_action('database_updated')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/libraries/App_clients_area_constructor.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 49 | `hooks()->do_action('clients_init')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/libraries/App_module_installer.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 30 | `hooks()->do_action('pre_upload_module')` | — (frontend Next.js) | SKIP |
| 48 | `hooks()->do_action('module_installed')` | `Spine\Events\ModuleInstalled` | ✅ ported |

## `application/libraries/App_modules.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 86 | `hooks()->do_action('pre_activate_module')` | ServiceProvider/Middleware (native) | NATIVE |
| 102 | `hooks()->do_action('module_activated')` | `Spine\Events\ModuleActivated` | ✅ ported |
| 123 | `hooks()->do_action('pre_deactivate_module')` | ServiceProvider/Middleware (native) | NATIVE |
| 140 | `hooks()->do_action('module_deactivated')` | `Spine\Events\ModuleDeactivated` | ✅ ported |
| 168 | `hooks()->do_action('pre_uninstall_module')` | ServiceProvider/Middleware (native) | NATIVE |
| 197 | `hooks()->do_action('module_uninstalled')` | `Spine\Events\ModuleUninstalled` | ✅ ported |
| 365 | `hooks()->do_action('module_')` | — | ⏳ modul |

## `application/libraries/App_tabs.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 112 | `hooks()->do_action('before_get_tabs')` | — (frontend Next.js) | SKIP |

## `application/libraries/App_tags.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 85 | `hooks()->do_action('new_tag_created')` | — | ⏳ modul |

## `application/libraries/assets/App_css.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 44 | `hooks()->do_action('before_compile_css_assets')` | — (frontend Next.js) | SKIP |

## `application/libraries/assets/App_scripts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 43 | `hooks()->do_action('before_compile_scripts_assets')` | — | ⏳ modul |

## `application/libraries/mails/App_mail_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 123 | `hooks()->do_action('failed_to_send_email_template')` | `Illuminate\Mail\Events\MessageSending` | ✅ native |
| 205 | `hooks()->do_action('email_template_sent')` | `Illuminate\Mail\Events\MessageSent` | ✅ native |

## `application/libraries/sms/App_sms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 143 | `hooks()->do_action('sms_trigger_triggered')` | `Spine\Events\SmsSent` | ✅ ported |

## `application/libraries/pdf/App_pdf.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 86 | `hooks()->do_action('pdf_construct')` | ServiceProvider/Middleware (native) | NATIVE |
| 182 | `hooks()->do_action('pdf_close')` | — | ⏳ modul |
| 191 | `hooks()->do_action('pdf_header')` | — (frontend Next.js) | SKIP |
| 201 | `hooks()->do_action('pdf_footer')` | — (frontend Next.js) | SKIP |

## `application/libraries/pdf/PDF_Signature.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 67 | `hooks()->do_action('before_customer_pdf_signature')` | — (frontend Next.js) | SKIP |
| 84 | `hooks()->do_action('after_customer_pdf_signature')` | — (frontend Next.js) | SKIP |

## `application/views/admin/dashboard/dashboard.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 13 | `hooks()->do_action('before_start_render_dashboard_content')` | — (frontend Next.js) | SKIP |
| 21 | `hooks()->do_action('after_dashboard_top_container')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('after_dashboard_half_container')` | — (frontend Next.js) | SKIP |
| 51 | `hooks()->do_action('after_dashboard')` | — (frontend Next.js) | SKIP |

## `application/views/admin/dashboard/widgets/user_data.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 59 | `hooks()->do_action('after_user_data_widget_tabs')` | — (frontend Next.js) | SKIP |
| 149 | `hooks()->do_action('after_user_data_widge_tabs_content')` | — (frontend Next.js) | SKIP |

## `application/views/admin/emails/email_templates.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('before_tickets_email_templates')` | — (frontend Next.js) | SKIP |
| 46 | `hooks()->do_action('before_estimates_email_templates')` | — (frontend Next.js) | SKIP |
| 82 | `hooks()->do_action('before_contracts_email_templates')` | — (frontend Next.js) | SKIP |
| 117 | `hooks()->do_action('before_invoices_email_templates')` | — (frontend Next.js) | SKIP |
| 153 | `hooks()->do_action('before_subscriptions_email_templates')` | — (frontend Next.js) | SKIP |
| 189 | `hooks()->do_action('before_credit_notes_email_templates')` | — (frontend Next.js) | SKIP |
| 225 | `hooks()->do_action('before_tasks_email_templates')` | — (frontend Next.js) | SKIP |
| 260 | `hooks()->do_action('before_customers_email_templates')` | — (frontend Next.js) | SKIP |
| 300 | `hooks()->do_action('before_proposals_email_templates')` | — (frontend Next.js) | SKIP |
| 335 | `hooks()->do_action('before_projects_email_templates')` | — (frontend Next.js) | SKIP |
| 369 | `hooks()->do_action('before_staff_email_templates')` | — (frontend Next.js) | SKIP |
| 404 | `hooks()->do_action('before_leads_email_templates')` | — (frontend Next.js) | SKIP |
| 439 | `hooks()->do_action('before_estimate_request_email_templates')` | — (frontend Next.js) | SKIP |
| 474 | `hooks()->do_action('before_notifications_email_templates')` | — (frontend Next.js) | SKIP |
| 509 | `hooks()->do_action('before_gdpr_email_templates')` | — (frontend Next.js) | SKIP |
| 544 | `hooks()->do_action('after_email_templates')` | — (frontend Next.js) | SKIP |

## `application/views/admin/includes/alerts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 31 | `hooks()->do_action('before_start_render_content')` | — | ⏳ modul |

## `application/views/admin/includes/aside.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 56 | `hooks()->do_action('before_render_aside_menu')` | — (frontend Next.js) | SKIP |
| 112 | `hooks()->do_action('after_render_single_aside_menu')` | — (frontend Next.js) | SKIP |
| 128 | `hooks()->do_action('after_render_aside_menu')` | — (frontend Next.js) | SKIP |

## `application/views/admin/includes/elfinder_tinymce.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('elfinder_tinymce_head')` | — (frontend Next.js) | SKIP |

## `application/views/admin/includes/head.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 26 | `hooks()->do_action('after_body_start')` | — (frontend Next.js) | SKIP |

## `application/views/admin/includes/header.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 71 | `hooks()->do_action('after_render_top_search')` | — (frontend Next.js) | SKIP |

## `application/views/admin/includes/scripts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 4 | `hooks()->do_action('before_js_scripts_render')` | — (frontend Next.js) | SKIP |

## `application/views/admin/includes/setup_menu.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 60 | `hooks()->do_action('after_render_single_setup_menu')` | — (frontend Next.js) | SKIP |

## `application/views/admin/contracts/contract.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 256 | `hooks()->do_action('after_contract_view_as_client_link')` | — (frontend Next.js) | SKIP |

## `application/views/admin/staff/member.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 228 | `hooks()->do_action('staff_render_permissions')` | — (frontend Next.js) | SKIP |

## `application/views/admin/staff/myprofile.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('before_staff_myprofile')` | — (frontend Next.js) | SKIP |

## `application/views/admin/estimate_request/forms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('forms_table_start')` | — (frontend Next.js) | SKIP |

## `application/views/admin/clients/modals/contact.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 235 | `hooks()->do_action('after_contact_modal_content_loaded')` | — (frontend Next.js) | SKIP |

## `application/views/admin/clients/groups/profile.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 33 | `hooks()->do_action('after_customer_billing_and_shipping_tab')` | — | ⏳ modul |
| 43 | `hooks()->do_action('after_customer_admins_tab')` | — | ⏳ modul |
| 49 | `hooks()->do_action('after_custom_profile_tab_content')` | — (frontend Next.js) | SKIP |

## `application/views/admin/invoices/invoice_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 176 | `hooks()->do_action('after_invoice_view_as_client_link')` | — (frontend Next.js) | SKIP |
| 234 | `hooks()->do_action('after_invoice_preview_more_menu')` | — (frontend Next.js) | SKIP |

## `application/views/admin/invoices/invoice_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 30 | `hooks()->do_action('before_render_invoice_template')` | — | ⏳ modul |
| 747 | `hooks()->do_action('after_render_invoice_template')` | — | ⏳ modul |

## `application/views/admin/estimates/estimate_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 125 | `hooks()->do_action('after_estimate_view_as_client_link')` | — (frontend Next.js) | SKIP |

## `application/views/admin/settings/all.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 72 | `hooks()->do_action('before_settings_group_view')` | — (frontend Next.js) | SKIP |
| 74 | `hooks()->do_action('after_settings_group_view')` | — (frontend Next.js) | SKIP |
| 192 | `hooks()->do_action('settings_group_end')` | — | ⏳ modul |

## `application/views/admin/settings/includes/cronjob.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 31 | `hooks()->do_action('after_cron_settings_last_tab')` | — (frontend Next.js) | SKIP |
| 163 | `hooks()->do_action('after_cron_settings_last_tab_content')` | — (frontend Next.js) | SKIP |

## `application/views/admin/settings/includes/e_sign.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 9 | `hooks()->do_action('after_settings_e_sign_fields')` | — (frontend Next.js) | SKIP |

## `application/views/admin/settings/includes/info.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 1 | `hooks()->do_action('before_system_info')` | — (frontend Next.js) | SKIP |
| 526 | `hooks()->do_action('after_system_info_files_permissions')` | — (frontend Next.js) | SKIP |
| 536 | `hooks()->do_action('after_system_last_info_row')` | — (frontend Next.js) | SKIP |

## `application/views/admin/settings/includes/leads.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 2 | `hooks()->do_action('before_leads_settings')` | — | ⏳ modul |
| 88 | `hooks()->do_action('after_leads_settings')` | — | ⏳ modul |

## `application/views/admin/settings/includes/misc.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 47 | `hooks()->do_action('after_misc_settings')` | — | ⏳ modul |

## `application/views/admin/settings/includes/payment_gateways.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 35 | `hooks()->do_action('before_render_payment_gateway_settings')` | — | ⏳ modul |

## `application/views/admin/settings/includes/pdf.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 82 | `hooks()->do_action('after_pdf_signature_settings_fields')` | — (frontend Next.js) | SKIP |
| 146 | `hooks()->do_action('after_pdf_document_formats')` | — (frontend Next.js) | SKIP |

## `application/views/admin/settings/includes/pusher.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 8 | `hooks()->do_action('after_pusher_cluster_option')` | — | ⏳ modul |

## `application/views/admin/settings/includes/sales.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 23 | `hooks()->do_action('after_finance_settings_last_tab')` | — (frontend Next.js) | SKIP |
| 333 | `hooks()->do_action('after_finance_settings_tabs_content')` | — (frontend Next.js) | SKIP |

## `application/views/admin/settings/includes/sms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 2 | `hooks()->do_action('before_sms_gateways_settings')` | — (frontend Next.js) | SKIP |
| 108 | `hooks()->do_action('after_sms_trigger_textarea_content')` | — (frontend Next.js) | SKIP |

## `application/views/admin/proposals/proposals_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 130 | `hooks()->do_action('after_proposal_view_as_client_link')` | — (frontend Next.js) | SKIP |

## `application/views/admin/leads/_kan_ban_card.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 42 | `hooks()->do_action('before_leads_kanban_card_icons')` | — (frontend Next.js) | SKIP |
| 50 | `hooks()->do_action('after_leads_kanban_card_icons')` | — (frontend Next.js) | SKIP |

## `application/views/admin/leads/email_integration.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 9 | `hooks()->do_action('before_leads_email_integration_form')` | — | ⏳ modul |

## `application/views/admin/leads/forms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('forms_table_start')` | — (frontend Next.js) | SKIP |

## `application/views/admin/leads/lead.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 117 | `hooks()->do_action('after_lead_lead_tabs')` | — (frontend Next.js) | SKIP |
| 131 | `hooks()->do_action('before_lead_email_activity')` | — | ⏳ modul |
| 152 | `hooks()->do_action('after_lead_email_activity')` | — | ⏳ modul |
| 355 | `hooks()->do_action('after_lead_tabs_content')` | — (frontend Next.js) | SKIP |
| 360 | `hooks()->do_action('lead_modal_profile_bottom')` | — (frontend Next.js) | SKIP |

## `application/views/admin/subscriptions/manage.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 71 | `hooks()->do_action('before_subscriptions_table')` | — (frontend Next.js) | SKIP |

## `application/views/admin/utilities/bulk_pdf_exporter.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 90 | `hooks()->do_action('after_bulk_pdf_export_options')` | — (frontend Next.js) | SKIP |

## `application/views/admin/utilities/calendar.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('after_calendar_loaded')` | — (frontend Next.js) | SKIP |

## `application/views/admin/utilities/calendar_filters.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 7 | `hooks()->do_action('before_calendar_filters')` | — (frontend Next.js) | SKIP |
| 104 | `hooks()->do_action('after_calendar_filters')` | — (frontend Next.js) | SKIP |

## `application/views/admin/invoice_items/manage.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 38 | `hooks()->do_action('before_items_page_content')` | — (frontend Next.js) | SKIP |

## `application/views/admin/credit_notes/credit_note_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 111 | `hooks()->do_action('credit_note_menu_links_start')` | — (frontend Next.js) | SKIP |

## `application/views/admin/expenses/expense.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 43 | `hooks()->do_action('before_expense_form_name')` | — | ⏳ modul |
| 310 | `hooks()->do_action('before_expense_form_template_close')` | — | ⏳ modul |

## `application/views/admin/tickets/add.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 180 | `hooks()->do_action('new_ticket_admin_page_loaded')` | — (frontend Next.js) | SKIP |

## `application/views/admin/tickets/list.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 68 | `hooks()->do_action('before_render_tickets_list_table')` | — (frontend Next.js) | SKIP |

## `application/views/admin/tickets/single.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 66 | `hooks()->do_action('add_single_ticket_tab_menu_item')` | — (frontend Next.js) | SKIP |
| 429 | `hooks()->do_action('add_single_ticket_tab_menu_content')` | — (frontend Next.js) | SKIP |
| 656 | `hooks()->do_action('ticket_admin_single_page_loaded')` | — (frontend Next.js) | SKIP |

## `application/views/admin/projects/project_overview.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 150 | `hooks()->do_action('admin_area_after_project_progress')` | — | ⏳ modul |

## `application/views/admin/projects/view.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 104 | `hooks()->do_action('before_render_project_view')` | — (frontend Next.js) | SKIP |

## `application/views/admin/tasks/task.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 162 | `hooks()->do_action('task_priorities_select')` | — (frontend Next.js) | SKIP |
| 253 | `hooks()->do_action('task_modal_rel_type_select')` | — (frontend Next.js) | SKIP |

## `application/views/admin/tasks/tasks_filter_by.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 5 | `hooks()->do_action('tasks_filters_hidden_html')` | — (frontend Next.js) | SKIP |

## `application/views/admin/tasks/view_task_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 328 | `hooks()->do_action('before_task_description_section')` | — (frontend Next.js) | SKIP |

## `application/views/admin/custom_fields/customfield.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 67 | `hooks()->do_action('after_custom_fields_select_options')` | — (frontend Next.js) | SKIP |

## `application/views/admin/gdpr/index.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 44 | `hooks()->do_action('before_admin_gdpr_settings')` | ServiceProvider/Middleware (native) | NATIVE |

## `application/views/authentication/login_admin.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('after_admin_login_form_start')` | — (frontend Next.js) | SKIP |
| 38 | `hooks()->do_action('before_admin_login_form_close')` | — (frontend Next.js) | SKIP |

## `application/views/authentication/includes/head.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 204 | `hooks()->do_action('app_admin_authentication_head')` | — (frontend Next.js) | SKIP |

## `application/views/forms/estimate_request.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_estimate_request_form_head')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('estimate_request_form_start')` | — (frontend Next.js) | SKIP |
| 71 | `hooks()->do_action('estimate_request_form_end')` | — (frontend Next.js) | SKIP |
| 159 | `hooks()->do_action('app_estimate_request_form_footer')` | — (frontend Next.js) | SKIP |

## `application/views/forms/public_ticket.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 2 | `hooks()->do_action('public_ticket_start')` | — | ⏳ modul |
| 12 | `hooks()->do_action('public_ticket_end')` | — | ⏳ modul |

## `application/views/forms/ticket.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('app_ticket_form_head')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('ticket_form_start')` | — (frontend Next.js) | SKIP |
| 33 | `hooks()->do_action('ticket_form_after_subject')` | — | ⏳ modul |
| 38 | `hooks()->do_action('ticket_form_after_name')` | — | ⏳ modul |
| 42 | `hooks()->do_action('ticket_form_after_email')` | — | ⏳ modul |
| 54 | `hooks()->do_action('ticket_form_after_department')` | — | ⏳ modul |
| 57 | `hooks()->do_action('ticket_form_after_priority')` | — | ⏳ modul |
| 61 | `hooks()->do_action('ticket_form_after_service')` | — | ⏳ modul |
| 65 | `hooks()->do_action('ticket_form_after_custom_fields')` | — | ⏳ modul |
| 68 | `hooks()->do_action('ticket_form_after_message')` | — | ⏳ modul |
| 83 | `hooks()->do_action('ticket_form_after_attachments')` | — | ⏳ modul |
| 114 | `hooks()->do_action('ticket_form_after_submit_button')` | — | ⏳ modul |
| 116 | `hooks()->do_action('ticket_form_end')` | — (frontend Next.js) | SKIP |
| 193 | `hooks()->do_action('app_ticket_form_footer')` | — (frontend Next.js) | SKIP |

## `application/views/forms/web_to_lead.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_web_to_lead_form_head')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('web_to_lead_form_start')` | — (frontend Next.js) | SKIP |
| 64 | `hooks()->do_action('web_to_lead_form_end')` | — (frontend Next.js) | SKIP |
| 146 | `hooks()->do_action('app_web_to_lead_form_footer')` | — (frontend Next.js) | SKIP |

## `application/views/themes/perfex/head.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('customers_after_body_start')` | — (frontend Next.js) | SKIP |

## `application/views/themes/perfex/index.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 16 | `hooks()->do_action('customers_content_container_start')` | — (frontend Next.js) | SKIP |
| 24 | `hooks()->do_action('before_customers_area_sub_menu_start')` | — (frontend Next.js) | SKIP |
| 27 | `hooks()->do_action('after_customers_area_sub_menu_end')` | — (frontend Next.js) | SKIP |

## `application/views/themes/perfex/template_parts/identity_confirmation_form.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 11 | `hooks()->do_action('before_confirmation_identity_fields')` | — | ⏳ modul |
| 54 | `hooks()->do_action('after_confirmation_identity_fields')` | — | ⏳ modul |

## `application/views/themes/perfex/template_parts/navigation.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 17 | `hooks()->do_action('customers_navigation_start')` | — (frontend Next.js) | SKIP |
| 32 | `hooks()->do_action('customers_navigation_end')` | — (frontend Next.js) | SKIP |
| 111 | `hooks()->do_action('customers_navigation_after_profile')` | — (frontend Next.js) | SKIP |

## `application/views/themes/perfex/views/files.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 5 | `hooks()->do_action('after_customers_area_files_heading')` | — (frontend Next.js) | SKIP |
| 13 | `hooks()->do_action('after_customers_area_files_dropzone')` | — (frontend Next.js) | SKIP |
| 89 | `hooks()->do_action('after_customers_area_files')` | — | ⏳ modul |

## `application/views/themes/perfex/views/home.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('client_area_after_project_overview')` | — | ⏳ modul |

## `application/views/themes/perfex/views/knowledge_base.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 17 | `hooks()->do_action('after_kb_groups_customers_area')` | — | ⏳ modul |

## `application/views/themes/perfex/views/knowledge_base_article.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 42 | `hooks()->do_action('after_single_knowledge_base_article_customers_area')` | — | ⏳ modul |

## `application/views/themes/perfex/views/login.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 12 | `hooks()->do_action('clients_login_form_start')` | — (frontend Next.js) | SKIP |
| 59 | `hooks()->do_action('clients_login_form_end')` | — (frontend Next.js) | SKIP |

## `application/views/themes/perfex/views/open_ticket.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 6 | `hooks()->do_action('before_client_open_ticket_form_start')` | — (frontend Next.js) | SKIP |

## `application/views/themes/perfex/views/profile.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 11 | `hooks()->do_action('before_client_profile_form_loaded')` | — (frontend Next.js) | SKIP |
| 111 | `hooks()->do_action('after_client_profile_form_loaded')` | — (frontend Next.js) | SKIP |
| 161 | `hooks()->do_action('after_client_profile_password_form_loaded')` | — (frontend Next.js) | SKIP |
