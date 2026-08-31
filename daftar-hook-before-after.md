# Hooks & Filters — application/ (BEFORE → AFTER)

*Ground truth 30 Agu 2026: **418 kejadian do_action** + **468 kejadian apply_filters** di `application/` (modules/ dikecualikan), gaya gist JamesSimpson + kolom AFTER.*

Status: `✅ ported` = event Spine, `✅ native` = Laravel bawaan, `⏳ Spine` = menunggu fitur Spine, `⏳ modul` = saat modul di-port, `SKIP` = frontend, `NATIVE` = ServiceProvider/Middleware.

## do_action() — per kejadian

### `application/core/AdminController.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 13 | `hooks()->do_action('pre_upgrade_database')` | ServiceProvider/Middleware (native) | NATIVE |
| 21 | `hooks()->do_action('pre_admin_init')` | ServiceProvider/Middleware (native) | NATIVE |
| 73 | `hooks()->do_action('admin_init')` | `ServiceProvider::boot()` | ✅ native |

### `application/core/App_Controller.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 93 | `hooks()->do_action('app_init')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/core/App_Model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('model_init')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/helpers/admin_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_admin_head')` | — (frontend Next.js) | SKIP |
| 22 | `hooks()->do_action('after_js_scripts_render')` | — (frontend Next.js) | SKIP |
| 24 | `hooks()->do_action('app_admin_footer')` | — (frontend Next.js) | SKIP |
| 215 | `hooks()->do_action('after_load_admin_language')` | — (frontend Next.js) | SKIP |

### `application/helpers/assets_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_admin_assets')` | — | ⏳ modul |
| 16 | `hooks()->do_action('app_client_assets')` | — | ⏳ modul |
| 18 | `hooks()->do_action('app_client_assets_added')` | — | ⏳ modul |
| 87 | `hooks()->do_action('app_admin_assets_added')` | — | ⏳ modul |

### `application/helpers/clients_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 734 | `hooks()->do_action('after_load_client_language')` | — (frontend Next.js) | SKIP |

### `application/helpers/database_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 108 | `hooks()->do_action('notification_created')` | `Spine\Events\NotificationSent` | ✅ ported |

### `application/helpers/deprecated_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('deprecated_function_run')` | — | ⏳ modul |
| 36 | `hooks()->do_action('deprecated_hook_run')` | — | ⏳ modul |

### `application/helpers/general_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 20 | `hooks()->do_action('before_generate_short_link')` | — (frontend Next.js) | SKIP |
| 61 | `hooks()->do_action('before_archive_short_link')` | — (frontend Next.js) | SKIP |

### `application/helpers/invoices_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 387 | `hooks()->do_action('invoice_status_changed')` | — | ⏳ modul |

### `application/helpers/pdf_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 37 | `hooks()->do_action('load_pdf_language')` | — (frontend Next.js) | SKIP |

### `application/helpers/template_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 284 | `hooks()->do_action('app_external_form_head')` | — (frontend Next.js) | SKIP |

### `application/helpers/themes_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 133 | `hooks()->do_action('customers_after_js_scripts_load')` | — (frontend Next.js) | SKIP |
| 135 | `hooks()->do_action('app_customers_footer')` | — (frontend Next.js) | SKIP |
| 153 | `hooks()->do_action('app_customers_head')` | — (frontend Next.js) | SKIP |

### `application/helpers/upload_helper.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 39 | `hooks()->do_action('before_upload_estimate_request_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 117 | `hooks()->do_action('before_upload_newsfeed_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 165 | `hooks()->do_action('before_upload_project_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 277 | `hooks()->do_action('before_upload_contract_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 511 | `hooks()->do_action('before_upload_client_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 567 | `hooks()->do_action('before_upload_expense_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 602 | `hooks()->do_action('before_upload_ticket_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 655 | `hooks()->do_action('before_upload_company_logo_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 709 | `hooks()->do_action('before_upload_signature_image_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 752 | `hooks()->do_action('before_upload_favicon_attachment')` | `Spine\Events\FileUploading` | ✅ ported |
| 789 | `hooks()->do_action('before_upload_staff_profile_image')` | `Spine\Events\FileUploading` | ✅ ported |
| 857 | `hooks()->do_action('before_upload_contact_profile_image')` | `Spine\Events\FileUploading` | ✅ ported |
| 938 | `hooks()->do_action('before_upload_project_discussion_comment_attachment')` | `Spine\Events\FileUploading` | ✅ ported |

### `application/hooks/InitHook.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 55 | `hooks()->do_action('modules_loaded')` | `ServiceProvider::boot()` | ✅ native |

### `application/controllers/Authentication.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('clients_authentication_constructor')` | — (frontend Next.js) | SKIP |
| 61 | `hooks()->do_action('after_contact_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 180 | `hooks()->do_action('after_client_register')` | ServiceProvider/Middleware (native) | NATIVE |
| 202 | `hooks()->do_action('after_client_register_logged_in')` | ServiceProvider/Middleware (native) | NATIVE |
| 267 | `hooks()->do_action('before_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 280 | `hooks()->do_action('after_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 301 | `hooks()->do_action('after_client_logout')` | `Illuminate\Auth\Events\Logout` | ✅ native |

### `application/controllers/Clients.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('after_clients_area_init')` | — (frontend Next.js) | SKIP |
| 1139 | `hooks()->do_action('before_remove_contact_profile_image')` | — (menunggu fitur Spine) | ⏳ Spine |

### `application/controllers/Contacts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 30 | `hooks()->do_action('after_clients_area_init')` | — (frontend Next.js) | SKIP |

### `application/controllers/Contract.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 77 | `hooks()->do_action('contract_html_viewed')` | — (frontend Next.js) | SKIP |

### `application/controllers/Download.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 39 | `hooks()->do_action('before_output_preview_video')` | — (frontend Next.js) | SKIP |
| 83 | `hooks()->do_action('before_output_preview_image')` | — (frontend Next.js) | SKIP |

### `application/controllers/Estimate.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 91 | `hooks()->do_action('estimate_html_viewed')` | — (frontend Next.js) | SKIP |

### `application/controllers/Forms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 178 | `hooks()->do_action('estimate_requests_created')` | — | ⏳ modul |
| 242 | `hooks()->do_action('estimate_request_form_submitted')` | — | ⏳ modul |
| 464 | `hooks()->do_action('after_add_task')` | — | ⏳ modul |
| 490 | `hooks()->do_action('lead_created')` | — | ⏳ modul |
| 564 | `hooks()->do_action('web_to_lead_form_submitted')` | — | ⏳ modul |
| 784 | `hooks()->do_action('ticket_form_submitted')` | — | ⏳ modul |

### `application/controllers/Invoice.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 77 | `hooks()->do_action('invoice_html_viewed')` | — (frontend Next.js) | SKIP |

### `application/controllers/Knowledge_base.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('customers_area_knowledge_base_construct')` | — (frontend Next.js) | SKIP |

### `application/controllers/Proposal.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 96 | `hooks()->do_action('proposal_html_viewed')` | — (frontend Next.js) | SKIP |

### `application/controllers/Verification.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 51 | `hooks()->do_action('contact_email_verified_but_requires_admin_confirmation')` | — | ⏳ modul |
| 55 | `hooks()->do_action('contact_email_verified')` | — | ⏳ modul |

### `application/controllers/admin/Authentication.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 23 | `hooks()->do_action('admin_auth_init')` | ServiceProvider/Middleware (native) | NATIVE |
| 81 | `hooks()->do_action('after_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 112 | `hooks()->do_action('after_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 123 | `hooks()->do_action('after_staff_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 171 | `hooks()->do_action('before_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 179 | `hooks()->do_action('after_user_reset_password')` | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| 228 | `hooks()->do_action('after_user_logout')` | `Illuminate\Auth\Events\Logout` | ✅ native |

### `application/controllers/admin/Auto_update.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('before_perform_update')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/controllers/admin/Clients.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 645 | `hooks()->do_action('after_contact_login')` | `Illuminate\Auth\Events\Login` | ✅ native |
| 873 | `hooks()->do_action('before_do_bulk_action_for_customers')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Emails.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 240 | `hooks()->do_action('before_send_test_smtp_email')` | `Mail test flow (native)` | ✅ native |
| 272 | `hooks()->do_action('smtp_test_email_success')` | `Mail test flow (native)` | ✅ native |
| 276 | `hooks()->do_action('smtp_test_email_failed')` | `Mail test flow (native)` | ✅ native |

### `application/controllers/admin/Expenses.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 125 | `hooks()->do_action('before_do_bulk_action_for_expenses')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Invoice_items.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 172 | `hooks()->do_action('before_do_bulk_action_for_items')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Leads.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 600 | `hooks()->do_action('lead_converted_to_customer')` | — | ⏳ modul |
| 1264 | `hooks()->do_action('before_do_bulk_action_for_leads')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Misc.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 497 | `hooks()->do_action('before_change_maximum_number_of_digits_to_decimal_fields')` | — | ⏳ modul |
| 539 | `hooks()->do_action('before_change_decimal_places')` | — | ⏳ modul |

### `application/controllers/admin/Newsfeed.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 371 | `hooks()->do_action('before_pin_post')` | — | ⏳ modul |
| 381 | `hooks()->do_action('before_unpin_post')` | — | ⏳ modul |
| 458 | `hooks()->do_action('before_delete_post')` | — | ⏳ modul |

### `application/controllers/admin/Projects.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 715 | `hooks()->do_action('before_do_bulk_action_for_project_files')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Proposals.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 357 | `hooks()->do_action('proposal_converted_to_estimate')` | — | ⏳ modul |
| 387 | `hooks()->do_action('proposal_converted_to_invoice')` | — | ⏳ modul |

### `application/controllers/admin/Settings.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 175 | `hooks()->do_action('before_remove_company_logo')` | — (menunggu fitur Spine) | ⏳ Spine |
| 197 | `hooks()->do_action('before_remove_favicon')` | — (menunggu fitur Spine) | ⏳ Spine |

### `application/controllers/admin/Staff.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 27 | `hooks()->do_action('staff_member_edit_view_profile')` | — (frontend Next.js) | SKIP |
| 119 | `hooks()->do_action('before_save_dashboard_widgets_order')` | — (frontend Next.js) | SKIP |
| 132 | `hooks()->do_action('before_save_dashboard_widgets_visibility')` | — (frontend Next.js) | SKIP |
| 148 | `hooks()->do_action('before_save_hidden_table_columns')` | — (frontend Next.js) | SKIP |
| 157 | `hooks()->do_action('before_staff_change_language')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 208 | `hooks()->do_action('edit_logged_in_staff_profile')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 246 | `hooks()->do_action('before_remove_staff_profile_image')` | — (menunggu fitur Spine) | ⏳ Spine |
| 288 | `hooks()->do_action('staff_profile_access')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 442 | `hooks()->do_action('before_save_completed_checklist_visibility')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Tasks.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 151 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 578 | `hooks()->do_action('task_checklist_item_finished')` | — | ⏳ modul |
| 887 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 936 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 1111 | `hooks()->do_action('after_update_task')` | — | ⏳ modul |
| 1117 | `hooks()->do_action('before_do_bulk_action_for_tasks')` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Tickets.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 684 | `hooks()->do_action('before_do_bulk_action_for_tickets')` | — (frontend Next.js) | SKIP |

### `application/controllers/gateways/Stripe.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 210 | `hooks()->do_action('customer_subscribed_to_subscription')` | — | ⏳ modul |

### `application/models/Announcements_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 104 | `hooks()->do_action('announcement_created')` | — | ⏳ modul |
| 130 | `hooks()->do_action('announcement_updated')` | — | ⏳ modul |
| 148 | `hooks()->do_action('before_delete_announcement')` | — | ⏳ modul |
| 156 | `hooks()->do_action('announcement_deleted')` | — | ⏳ modul |

### `application/models/Authentication_model.php`
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

### `application/models/Client_groups_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 93 | `hooks()->do_action('customer_group_deleted')` | — | ⏳ modul |

### `application/models/Client_vault_entries_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 99 | `hooks()->do_action('customer_vault_entry_deleted')` | — | ⏳ modul |

### `application/models/Clients_model.php`
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
| 1666 | `hooks()->do_action('before_remove_contact_profile_image')` | — (menunggu fitur Spine) | ⏳ Spine |

### `application/models/Contracts_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 135 | `hooks()->do_action('after_contract_added')` | — | ⏳ modul |
| 186 | `hooks()->do_action('after_contract_updated')` | — | ⏳ modul |
| 416 | `hooks()->do_action('before_contract_deleted')` | — | ⏳ modul |

### `application/models/Credit_notes_model.php`
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

### `application/models/Cron_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 47 | `hooks()->do_action('before_cron_run')` | — (cron Spine) | ⏳ Spine |
| 103 | `hooks()->do_action('after_cron_run')` | — (cron Spine) | ⏳ Spine |
| 303 | `hooks()->do_action('after_ticket_status_changed')` | — | ⏳ modul |
| 408 | `hooks()->do_action('before_check_recurring_tasks')` | — | ⏳ modul |
| 485 | `hooks()->do_action('after_check_recurring_tasks')` | — | ⏳ modul |
| 1380 | `hooks()->do_action('after_add_task')` | — | ⏳ modul |
| 1444 | `hooks()->do_action('existing_lead_email_inserted_from_email_integration')` | — | ⏳ modul |
| 1530 | `hooks()->do_action('lead_created')` | — | ⏳ modul |
| 1532 | `hooks()->do_action('lead_created_from_email_integration')` | — | ⏳ modul |

### `application/models/Departments_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 71 | `hooks()->do_action('after_department_added')` | — | ⏳ modul |
| 153 | `hooks()->do_action('before_delete_department')` | — | ⏳ modul |

### `application/models/Emails_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 487 | `hooks()->do_action('email_template_sent')` | `Illuminate\Mail\Events\MessageSent` | ✅ native |

### `application/models/Estimate_request_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 33 | `hooks()->do_action('estimate_request_assigned_changed')` | — | ⏳ modul |
| 88 | `hooks()->do_action('estimate_request_status_changed')` | — | ⏳ modul |
| 253 | `hooks()->do_action('before_estimate_request_deleted')` | — | ⏳ modul |

### `application/models/Estimates_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 283 | `hooks()->do_action('estimate_converted_to_invoice')` | — | ⏳ modul |
| 551 | `hooks()->do_action('after_estimate_added')` | — | ⏳ modul |
| 777 | `hooks()->do_action('after_estimate_updated')` | — | ⏳ modul |
| 849 | `hooks()->do_action('estimate_accepted')` | — | ⏳ modul |
| 876 | `hooks()->do_action('estimate_declined')` | — | ⏳ modul |
| 974 | `hooks()->do_action('before_estimate_deleted')` | — | ⏳ modul |
| 1268 | `hooks()->do_action('estimate_sent')` | — | ⏳ modul |

### `application/models/Expenses_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 150 | `hooks()->do_action('after_expense_added')` | — | ⏳ modul |
| 418 | `hooks()->do_action('after_expense_updated')` | — | ⏳ modul |
| 634 | `hooks()->do_action('expense_converted_to_invoice')` | — | ⏳ modul |

### `application/models/Invoice_items_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 62 | `hooks()->do_action('item_coppied')` | — | ⏳ modul |
| 178 | `hooks()->do_action('item_created')` | — | ⏳ modul |
| 248 | `hooks()->do_action('item_updated')` | — | ⏳ modul |
| 286 | `hooks()->do_action('item_deleted')` | — | ⏳ modul |

### `application/models/Invoices_model.php`
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

### `application/models/Leads_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 126 | `hooks()->do_action('lead_created')` | — | ⏳ modul |
| 282 | `hooks()->do_action('lead_status_changed')` | — | ⏳ modul |
| 322 | `hooks()->do_action('before_lead_deleted')` | — | ⏳ modul |
| 415 | `hooks()->do_action('lead_marked_as_lost')` | — | ⏳ modul |
| 476 | `hooks()->do_action('lead_marked_as_junk')` | — | ⏳ modul |
| 824 | `hooks()->do_action('lead_status_changed')` | — | ⏳ modul |

### `application/models/Misc_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 300 | `hooks()->do_action('note_created')` | — | ⏳ modul |
| 310 | `hooks()->do_action('before_update_note')` | — | ⏳ modul |
| 321 | `hooks()->do_action('note_updated')` | — | ⏳ modul |
| 339 | `hooks()->do_action('before_delete_note')` | — | ⏳ modul |
| 351 | `hooks()->do_action('note_deleted')` | — | ⏳ modul |

### `application/models/Payment_modes_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 199 | `hooks()->do_action('before_get_payment_gateways')` | — | ⏳ modul |

### `application/models/Payments_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 363 | `hooks()->do_action('after_payment_added')` | — | ⏳ modul |
| 410 | `hooks()->do_action('before_payment_deleted')` | — | ⏳ modul |
| 477 | `hooks()->do_action('after_payment_added')` | — | ⏳ modul |

### `application/models/Projects_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 479 | `hooks()->do_action('before_remove_project_file')` | — (menunggu fitur Spine) | ⏳ Spine |
| 851 | `hooks()->do_action('after_add_project')` | — | ⏳ modul |
| 1049 | `hooks()->do_action('project_status_changed')` | — | ⏳ modul |
| 1067 | `hooks()->do_action('after_update_project')` | — | ⏳ modul |
| 1105 | `hooks()->do_action('project_status_changed')` | — | ⏳ modul |
| 1679 | `hooks()->do_action('after_add_discussion_comment')` | — | ⏳ modul |
| 2076 | `hooks()->do_action('project_copied')` | — | ⏳ modul |

### `application/models/Proposals_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 158 | `hooks()->do_action('proposal_created')` | — | ⏳ modul |
| 320 | `hooks()->do_action('after_proposal_updated')` | — | ⏳ modul |
| 742 | `hooks()->do_action('proposal_accepted')` | — | ⏳ modul |
| 750 | `hooks()->do_action('proposal_declined')` | — | ⏳ modul |
| 964 | `hooks()->do_action('proposal_sent')` | — | ⏳ modul |

### `application/models/Staff_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 17 | `hooks()->do_action('before_delete_staff_member')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 321 | `hooks()->do_action('staff_member_deleted')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 489 | `hooks()->do_action('staff_member_created')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 640 | `hooks()->do_action('staff_member_updated')` | — (CRUD staff (app konsumen)) | ⏳ Spine |
| 692 | `hooks()->do_action('staff_member_profile_updated')` | — (CRUD staff (app konsumen)) | ⏳ Spine |

### `application/models/Tasks_model.php`
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

### `application/models/Templates_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 28 | `hooks()->do_action('new_template_added')` | — | ⏳ modul |
| 73 | `hooks()->do_action('after_template_updated')` | — | ⏳ modul |
| 86 | `hooks()->do_action('before_template_deleted')` | — | ⏳ modul |
| 93 | `hooks()->do_action('after_template_deleted')` | — | ⏳ modul |

### `application/models/Tickets_model.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 522 | `hooks()->do_action('after_ticket_status_changed')` | — | ⏳ modul |
| 602 | `hooks()->do_action('after_ticket_reply_added')` | — | ⏳ modul |
| 623 | `hooks()->do_action('before_delete_ticket_reply')` | — | ⏳ modul |
| 940 | `hooks()->do_action('ticket_created')` | — | ⏳ modul |
| 979 | `hooks()->do_action('before_ticket_deleted')` | — | ⏳ modul |
| 1103 | `hooks()->do_action('ticket_settings_updated')` | — | ⏳ modul |
| 1187 | `hooks()->do_action('after_ticket_status_changed')` | — | ⏳ modul |

### `application/services/ViewsTracking.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 47 | `hooks()->do_action('before_insert_views_tracking')` | — (frontend Next.js) | SKIP |

### `application/services/upgrade/Response.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 11 | `hooks()->do_action('auto_upgrade_failed_to_extract_zip_file')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/libraries/App.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 80 | `hooks()->do_action('app_base_after_construct_action')` | — (frontend Next.js) | SKIP |
| 362 | `hooks()->do_action('before_update_database')` | ServiceProvider/Middleware (native) | NATIVE |
| 374 | `hooks()->do_action('database_updated')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/libraries/App_clients_area_constructor.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 49 | `hooks()->do_action('clients_init')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/libraries/App_module_installer.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 30 | `hooks()->do_action('pre_upload_module')` | — (frontend Next.js) | SKIP |
| 48 | `hooks()->do_action('module_installed')` | `Spine\Events\ModuleInstalled` | ✅ ported |

### `application/libraries/App_modules.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 86 | `hooks()->do_action('pre_activate_module')` | ServiceProvider/Middleware (native) | NATIVE |
| 102 | `hooks()->do_action('module_activated')` | `Spine\Events\ModuleActivated` | ✅ ported |
| 123 | `hooks()->do_action('pre_deactivate_module')` | ServiceProvider/Middleware (native) | NATIVE |
| 140 | `hooks()->do_action('module_deactivated')` | `Spine\Events\ModuleDeactivated` | ✅ ported |
| 168 | `hooks()->do_action('pre_uninstall_module')` | ServiceProvider/Middleware (native) | NATIVE |
| 197 | `hooks()->do_action('module_uninstalled')` | `Spine\Events\ModuleUninstalled` | ✅ ported |
| 365 | `hooks()->do_action('module_')` | — | ⏳ modul |

### `application/libraries/App_tabs.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 112 | `hooks()->do_action('before_get_tabs')` | — (frontend Next.js) | SKIP |

### `application/libraries/App_tags.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 85 | `hooks()->do_action('new_tag_created')` | — | ⏳ modul |

### `application/libraries/assets/App_css.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 44 | `hooks()->do_action('before_compile_css_assets')` | — (frontend Next.js) | SKIP |

### `application/libraries/assets/App_scripts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 43 | `hooks()->do_action('before_compile_scripts_assets')` | — | ⏳ modul |

### `application/libraries/mails/App_mail_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 123 | `hooks()->do_action('failed_to_send_email_template')` | `Illuminate\Mail\Events\MessageSending` | ✅ native |
| 205 | `hooks()->do_action('email_template_sent')` | `Illuminate\Mail\Events\MessageSent` | ✅ native |

### `application/libraries/sms/App_sms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 143 | `hooks()->do_action('sms_trigger_triggered')` | `Spine\Events\SmsSent` | ✅ ported |

### `application/libraries/pdf/App_pdf.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 86 | `hooks()->do_action('pdf_construct')` | — (PdfService (lifecycle)) | ⏳ Spine |
| 182 | `hooks()->do_action('pdf_close')` | — (PdfService (lifecycle)) | ⏳ Spine |
| 191 | `hooks()->do_action('pdf_header')` | — (frontend Next.js) | SKIP |
| 201 | `hooks()->do_action('pdf_footer')` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/PDF_Signature.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 67 | `hooks()->do_action('before_customer_pdf_signature')` | — (frontend Next.js) | SKIP |
| 84 | `hooks()->do_action('after_customer_pdf_signature')` | — (frontend Next.js) | SKIP |

### `application/views/admin/dashboard/dashboard.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 13 | `hooks()->do_action('before_start_render_dashboard_content')` | — (frontend Next.js) | SKIP |
| 21 | `hooks()->do_action('after_dashboard_top_container')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('after_dashboard_half_container')` | — (frontend Next.js) | SKIP |
| 51 | `hooks()->do_action('after_dashboard')` | — (frontend Next.js) | SKIP |

### `application/views/admin/dashboard/widgets/user_data.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 59 | `hooks()->do_action('after_user_data_widget_tabs')` | — (frontend Next.js) | SKIP |
| 149 | `hooks()->do_action('after_user_data_widge_tabs_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/emails/email_templates.php`
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

### `application/views/admin/includes/alerts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 31 | `hooks()->do_action('before_start_render_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/aside.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 56 | `hooks()->do_action('before_render_aside_menu')` | — (frontend Next.js) | SKIP |
| 112 | `hooks()->do_action('after_render_single_aside_menu')` | — (frontend Next.js) | SKIP |
| 128 | `hooks()->do_action('after_render_aside_menu')` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/elfinder_tinymce.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('elfinder_tinymce_head')` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/head.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 26 | `hooks()->do_action('after_body_start')` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/header.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 71 | `hooks()->do_action('after_render_top_search')` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/scripts.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 4 | `hooks()->do_action('before_js_scripts_render')` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/setup_menu.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 60 | `hooks()->do_action('after_render_single_setup_menu')` | — (frontend Next.js) | SKIP |

### `application/views/admin/contracts/contract.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 256 | `hooks()->do_action('after_contract_view_as_client_link')` | — (frontend Next.js) | SKIP |

### `application/views/admin/staff/member.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 228 | `hooks()->do_action('staff_render_permissions')` | — (frontend Next.js) | SKIP |

### `application/views/admin/staff/myprofile.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('before_staff_myprofile')` | — (frontend Next.js) | SKIP |

### `application/views/admin/estimate_request/forms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('forms_table_start')` | — (frontend Next.js) | SKIP |

### `application/views/admin/clients/modals/contact.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 235 | `hooks()->do_action('after_contact_modal_content_loaded')` | — (frontend Next.js) | SKIP |

### `application/views/admin/clients/groups/profile.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 33 | `hooks()->do_action('after_customer_billing_and_shipping_tab')` | — | ⏳ modul |
| 43 | `hooks()->do_action('after_customer_admins_tab')` | — | ⏳ modul |
| 49 | `hooks()->do_action('after_custom_profile_tab_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/invoices/invoice_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 176 | `hooks()->do_action('after_invoice_view_as_client_link')` | — (frontend Next.js) | SKIP |
| 234 | `hooks()->do_action('after_invoice_preview_more_menu')` | — (frontend Next.js) | SKIP |

### `application/views/admin/invoices/invoice_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 30 | `hooks()->do_action('before_render_invoice_template')` | — (frontend Next.js) | SKIP |
| 747 | `hooks()->do_action('after_render_invoice_template')` | — (frontend Next.js) | SKIP |

### `application/views/admin/estimates/estimate_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 125 | `hooks()->do_action('after_estimate_view_as_client_link')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/all.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 72 | `hooks()->do_action('before_settings_group_view')` | — (frontend Next.js) | SKIP |
| 74 | `hooks()->do_action('after_settings_group_view')` | — (frontend Next.js) | SKIP |
| 192 | `hooks()->do_action('settings_group_end')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/cronjob.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 31 | `hooks()->do_action('after_cron_settings_last_tab')` | — (frontend Next.js) | SKIP |
| 163 | `hooks()->do_action('after_cron_settings_last_tab_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/e_sign.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 9 | `hooks()->do_action('after_settings_e_sign_fields')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/info.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 1 | `hooks()->do_action('before_system_info')` | — (frontend Next.js) | SKIP |
| 526 | `hooks()->do_action('after_system_info_files_permissions')` | — (frontend Next.js) | SKIP |
| 536 | `hooks()->do_action('after_system_last_info_row')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/leads.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 2 | `hooks()->do_action('before_leads_settings')` | — | ⏳ modul |
| 88 | `hooks()->do_action('after_leads_settings')` | — | ⏳ modul |

### `application/views/admin/settings/includes/misc.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 47 | `hooks()->do_action('after_misc_settings')` | — | ⏳ modul |

### `application/views/admin/settings/includes/payment_gateways.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 35 | `hooks()->do_action('before_render_payment_gateway_settings')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/pdf.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 82 | `hooks()->do_action('after_pdf_signature_settings_fields')` | — (frontend Next.js) | SKIP |
| 146 | `hooks()->do_action('after_pdf_document_formats')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/pusher.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 8 | `hooks()->do_action('after_pusher_cluster_option')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/sales.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 23 | `hooks()->do_action('after_finance_settings_last_tab')` | — (frontend Next.js) | SKIP |
| 333 | `hooks()->do_action('after_finance_settings_tabs_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/sms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 2 | `hooks()->do_action('before_sms_gateways_settings')` | — (frontend Next.js) | SKIP |
| 108 | `hooks()->do_action('after_sms_trigger_textarea_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/proposals/proposals_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 130 | `hooks()->do_action('after_proposal_view_as_client_link')` | — (frontend Next.js) | SKIP |

### `application/views/admin/leads/_kan_ban_card.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 42 | `hooks()->do_action('before_leads_kanban_card_icons')` | — (frontend Next.js) | SKIP |
| 50 | `hooks()->do_action('after_leads_kanban_card_icons')` | — (frontend Next.js) | SKIP |

### `application/views/admin/leads/email_integration.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 9 | `hooks()->do_action('before_leads_email_integration_form')` | — | ⏳ modul |

### `application/views/admin/leads/forms.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('forms_table_start')` | — (frontend Next.js) | SKIP |

### `application/views/admin/leads/lead.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 117 | `hooks()->do_action('after_lead_lead_tabs')` | — (frontend Next.js) | SKIP |
| 131 | `hooks()->do_action('before_lead_email_activity')` | — | ⏳ modul |
| 152 | `hooks()->do_action('after_lead_email_activity')` | — | ⏳ modul |
| 355 | `hooks()->do_action('after_lead_tabs_content')` | — (frontend Next.js) | SKIP |
| 360 | `hooks()->do_action('lead_modal_profile_bottom')` | — (frontend Next.js) | SKIP |

### `application/views/admin/subscriptions/manage.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 71 | `hooks()->do_action('before_subscriptions_table')` | — (frontend Next.js) | SKIP |

### `application/views/admin/utilities/bulk_pdf_exporter.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 90 | `hooks()->do_action('after_bulk_pdf_export_options')` | — (frontend Next.js) | SKIP |

### `application/views/admin/utilities/calendar.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 19 | `hooks()->do_action('after_calendar_loaded')` | — (frontend Next.js) | SKIP |

### `application/views/admin/utilities/calendar_filters.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 7 | `hooks()->do_action('before_calendar_filters')` | — (frontend Next.js) | SKIP |
| 104 | `hooks()->do_action('after_calendar_filters')` | — (frontend Next.js) | SKIP |

### `application/views/admin/invoice_items/manage.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 38 | `hooks()->do_action('before_items_page_content')` | — (frontend Next.js) | SKIP |

### `application/views/admin/credit_notes/credit_note_preview_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 111 | `hooks()->do_action('credit_note_menu_links_start')` | — (frontend Next.js) | SKIP |

### `application/views/admin/expenses/expense.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 43 | `hooks()->do_action('before_expense_form_name')` | — | ⏳ modul |
| 310 | `hooks()->do_action('before_expense_form_template_close')` | — (frontend Next.js) | SKIP |

### `application/views/admin/tickets/add.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 180 | `hooks()->do_action('new_ticket_admin_page_loaded')` | — (frontend Next.js) | SKIP |

### `application/views/admin/tickets/list.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 68 | `hooks()->do_action('before_render_tickets_list_table')` | — (frontend Next.js) | SKIP |

### `application/views/admin/tickets/single.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 66 | `hooks()->do_action('add_single_ticket_tab_menu_item')` | — (frontend Next.js) | SKIP |
| 429 | `hooks()->do_action('add_single_ticket_tab_menu_content')` | — (frontend Next.js) | SKIP |
| 656 | `hooks()->do_action('ticket_admin_single_page_loaded')` | — (frontend Next.js) | SKIP |

### `application/views/admin/projects/project_overview.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 150 | `hooks()->do_action('admin_area_after_project_progress')` | — (frontend Next.js) | SKIP |

### `application/views/admin/projects/view.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 104 | `hooks()->do_action('before_render_project_view')` | — (frontend Next.js) | SKIP |

### `application/views/admin/tasks/task.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 162 | `hooks()->do_action('task_priorities_select')` | — (frontend Next.js) | SKIP |
| 253 | `hooks()->do_action('task_modal_rel_type_select')` | — (frontend Next.js) | SKIP |

### `application/views/admin/tasks/tasks_filter_by.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 5 | `hooks()->do_action('tasks_filters_hidden_html')` | — (frontend Next.js) | SKIP |

### `application/views/admin/tasks/view_task_template.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 328 | `hooks()->do_action('before_task_description_section')` | — (frontend Next.js) | SKIP |

### `application/views/admin/custom_fields/customfield.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 67 | `hooks()->do_action('after_custom_fields_select_options')` | — (frontend Next.js) | SKIP |

### `application/views/admin/gdpr/index.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 44 | `hooks()->do_action('before_admin_gdpr_settings')` | ServiceProvider/Middleware (native) | NATIVE |

### `application/views/authentication/login_admin.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('after_admin_login_form_start')` | — (frontend Next.js) | SKIP |
| 38 | `hooks()->do_action('before_admin_login_form_close')` | — (frontend Next.js) | SKIP |

### `application/views/authentication/includes/head.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 204 | `hooks()->do_action('app_admin_authentication_head')` | — (frontend Next.js) | SKIP |

### `application/views/forms/estimate_request.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_estimate_request_form_head')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('estimate_request_form_start')` | — (frontend Next.js) | SKIP |
| 71 | `hooks()->do_action('estimate_request_form_end')` | — (frontend Next.js) | SKIP |
| 159 | `hooks()->do_action('app_estimate_request_form_footer')` | — (frontend Next.js) | SKIP |

### `application/views/forms/public_ticket.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 2 | `hooks()->do_action('public_ticket_start')` | — | ⏳ modul |
| 12 | `hooks()->do_action('public_ticket_end')` | — | ⏳ modul |

### `application/views/forms/ticket.php`
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

### `application/views/forms/web_to_lead.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 10 | `hooks()->do_action('app_web_to_lead_form_head')` | — (frontend Next.js) | SKIP |
| 30 | `hooks()->do_action('web_to_lead_form_start')` | — (frontend Next.js) | SKIP |
| 64 | `hooks()->do_action('web_to_lead_form_end')` | — (frontend Next.js) | SKIP |
| 146 | `hooks()->do_action('app_web_to_lead_form_footer')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/head.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 14 | `hooks()->do_action('customers_after_body_start')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/index.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 16 | `hooks()->do_action('customers_content_container_start')` | — (frontend Next.js) | SKIP |
| 24 | `hooks()->do_action('before_customers_area_sub_menu_start')` | — (frontend Next.js) | SKIP |
| 27 | `hooks()->do_action('after_customers_area_sub_menu_end')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/template_parts/identity_confirmation_form.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 11 | `hooks()->do_action('before_confirmation_identity_fields')` | — | ⏳ modul |
| 54 | `hooks()->do_action('after_confirmation_identity_fields')` | — | ⏳ modul |

### `application/views/themes/perfex/template_parts/navigation.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 17 | `hooks()->do_action('customers_navigation_start')` | — (frontend Next.js) | SKIP |
| 32 | `hooks()->do_action('customers_navigation_end')` | — (frontend Next.js) | SKIP |
| 111 | `hooks()->do_action('customers_navigation_after_profile')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/files.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 5 | `hooks()->do_action('after_customers_area_files_heading')` | — (frontend Next.js) | SKIP |
| 13 | `hooks()->do_action('after_customers_area_files_dropzone')` | — (frontend Next.js) | SKIP |
| 89 | `hooks()->do_action('after_customers_area_files')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/home.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 15 | `hooks()->do_action('client_area_after_project_overview')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/knowledge_base.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 17 | `hooks()->do_action('after_kb_groups_customers_area')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/knowledge_base_article.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 42 | `hooks()->do_action('after_single_knowledge_base_article_customers_area')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/login.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 12 | `hooks()->do_action('clients_login_form_start')` | — (frontend Next.js) | SKIP |
| 59 | `hooks()->do_action('clients_login_form_end')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/open_ticket.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 6 | `hooks()->do_action('before_client_open_ticket_form_start')` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/profile.php`
| Line | Hook (BEFORE) | AFTER (Spine) | Status |
|---|---|---|---|
| 11 | `hooks()->do_action('before_client_profile_form_loaded')` | — (frontend Next.js) | SKIP |
| 111 | `hooks()->do_action('after_client_profile_form_loaded')` | — (frontend Next.js) | SKIP |
| 161 | `hooks()->do_action('after_client_profile_password_form_loaded')` | — (frontend Next.js) | SKIP |

## apply_filters() — per kejadian

### `application/core/AdminController.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 90 | `hooks()->apply_filters('admin_area_auto_loaded_vars', …)` | — (frontend Next.js) | SKIP |

### `application/core/App_Loader.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 22 | `hooks()->apply_filters('app_view_data', …)` | — (frontend Next.js) | SKIP |

### `application/core/App_Security.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 19 | `hooks()->apply_filters('csrf_exclude_uris', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/admin_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 137 | `hooks()->apply_filters('staff_can', …)` | `Gate/permission (native)` | ✅ native |
| 143 | `hooks()->apply_filters('staff_can', …)` | `Gate/permission (native)` | ✅ native |
| 147 | `hooks()->apply_filters('staff_can', …)` | `Gate/permission (native)` | ✅ native |
| 312 | `hooks()->apply_filters('admin_body_class', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/clients_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 77 | `hooks()->apply_filters('is_client_id_used', …)` | Pipeline / Eloquent model events | ⏳ |
| 86 | `hooks()->apply_filters('customer_has_subscriptions', …)` | Pipeline / Eloquent model events | ⏳ |
| 154 | `hooks()->apply_filters('client_filtered_visible_tabs', …)` | — (frontend Next.js) | SKIP |
| 416 | `hooks()->apply_filters('is_client_using_multiple_currencies', …)` | Pipeline / Eloquent model events | ⏳ |
| 763 | `hooks()->apply_filters('customer_have_transactions', …)` | Pipeline / Eloquent model events | ⏳ |
| 806 | `hooks()->apply_filters('get_contact_permissions', …)` | Gate/permission (native) | ✅ native |
| 1142 | `hooks()->apply_filters('all_client_attachments', …)` | Pipeline / Eloquent model events | ⏳ |
| 1246 | `hooks()->apply_filters('automatic_calling_codes_enabled', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/core_hooks_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 88 | `hooks()->apply_filters('customers_area_estimate_request_link', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/countries_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 11 | `hooks()->apply_filters('all_countries', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/credit_notes_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 52 | `hooks()->apply_filters('invoices_statuses_available_for_credits', …)` | Pipeline / Eloquent model events | ⏳ |
| 108 | `hooks()->apply_filters('format_credit_note_number', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/custom_fields_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 68 | `hooks()->apply_filters('show_custom_fields_edit_link_on_clients_area', …)` | — (frontend Next.js) | SKIP |
| 495 | `hooks()->apply_filters('items_custom_fields_for_table_sql', …)` | — (frontend Next.js) | SKIP |
| 505 | `hooks()->apply_filters('custom_fields_where_items_table_add_edit_preview', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/database_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 94 | `hooks()->apply_filters('notification_data', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/datatables_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 78 | `hooks()->apply_filters('datatables_query_order_column', …)` | — (frontend Next.js) | SKIP |
| 116 | `hooks()->apply_filters('use_match_for_custom_fields_table_search', …)` | — (frontend Next.js) | SKIP |
| 229 | `hooks()->apply_filters('datatables_sql_query_results', …)` | — (frontend Next.js) | SKIP |
| 281 | `hooks()->apply_filters('null_columns_sort_as_last', …)` | — (frontend Next.js) | SKIP |
| 371 | `hooks()->apply_filters('datatables_language_array', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/deprecated_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 23 | `hooks()->apply_filters('deprecated_function_trigger_error', …)` | — (frontend Next.js) | SKIP |
| 43 | `hooks()->apply_filters('deprecated_hook_trigger_error', …)` | — (frontend Next.js) | SKIP |
| 141 | `hooks()->apply_filters('project_status_color_class', …)` | — (frontend Next.js) | SKIP |
| 171 | `hooks()->apply_filters('project_status_label', …)` | — (frontend Next.js) | SKIP |
| 461 | `hooks()->apply_filters('client_email_templates', …)` | — (frontend Next.js) | SKIP |
| 508 | `hooks()->apply_filters('staff_email_templates', …)` | — (frontend Next.js) | SKIP |
| 575 | `hooks()->apply_filters('email_template_language', …)` | — (frontend Next.js) | SKIP |
| 697 | `hooks()->apply_filters('item_preview_rate', …)` | — (frontend Next.js) | SKIP |
| 740 | `hooks()->apply_filters('item_tax_table_row', …)` | — (frontend Next.js) | SKIP |
| 748 | `hooks()->apply_filters('item_tax_table_row', …)` | — (frontend Next.js) | SKIP |
| 764 | `hooks()->apply_filters('item_preview_amount_with_currency', …)` | — (frontend Next.js) | SKIP |
| 805 | `hooks()->apply_filters('before_return_table_items_html_and_taxes', …)` | — (frontend Next.js) | SKIP |
| 916 | `hooks()->apply_filters('money_after_format_with_currency', …)` | Pipeline / Eloquent model events | ⏳ |
| 1058 | `hooks()->apply_filters('staff_permissions_conditions', …)` | Gate/permission (native) | ✅ native |

### `application/helpers/email_templates_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 72 | `hooks()->apply_filters('email_template_parsed', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/emails_tracking_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 75 | `hooks()->apply_filters('available_tracking_templates', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/estimates_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 114 | `hooks()->apply_filters('estimate_status_pdf_color', …)` | — (frontend Next.js) | SKIP |
| 163 | `hooks()->apply_filters('estimate_status_label', …)` | — (frontend Next.js) | SKIP |
| 200 | `hooks()->apply_filters('estimate_status_color_class', …)` | — (frontend Next.js) | SKIP |
| 238 | `hooks()->apply_filters('format_estimate_number', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/files_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 123 | `hooks()->apply_filters('html5_video_extensions', …)` | Pipeline / Eloquent model events | ⏳ |
| 488 | `hooks()->apply_filters('markdown_extensions', …)` | Pipeline / Eloquent model events | ⏳ |
| 507 | `hooks()->apply_filters('mark_down_safe_mode', …)` | Pipeline / Eloquent model events | ⏳ |
| 617 | `hooks()->apply_filters('delete_old_temporary_files_older_than', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/func_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 131 | `hooks()->apply_filters('sec2qty_formatted', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/general_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 274 | `hooks()->apply_filters('get_current_date_format', …)` | Pipeline / Eloquent model events | ⏳ |
| 471 | `hooks()->apply_filters('available_date_formats', …)` | Pipeline / Eloquent model events | ⏳ |
| 517 | `hooks()->apply_filters('before_get_language_text', …)` | — (frontend Next.js) | SKIP |
| 536 | `hooks()->apply_filters('after_get_language_text', …)` | — (frontend Next.js) | SKIP |
| 577 | `hooks()->apply_filters('after_format_date', …)` | Pipeline / Eloquent model events | ⏳ |
| 616 | `hooks()->apply_filters('after_format_datetime', …)` | Pipeline / Eloquent model events | ⏳ |
| 633 | `hooks()->apply_filters('before_sql_date_format', …)` | Pipeline / Eloquent model events | ⏳ |
| 639 | `hooks()->apply_filters('to_sql_date_formatted', …)` | Pipeline / Eloquent model events | ⏳ |
| 666 | `hooks()->apply_filters('to_sql_date_formatted', …)` | Pipeline / Eloquent model events | ⏳ |
| 712 | `hooks()->apply_filters('before_get_locales', …)` | — (frontend Next.js) | SKIP |
| 723 | `hooks()->apply_filters('before_get_locale', …)` | — (frontend Next.js) | SKIP |
| 855 | `hooks()->apply_filters('app_happy_text_regex', …)` | Pipeline / Eloquent model events | ⏳ |
| 858 | `hooks()->apply_filters('app_happy_text_color', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/invoices_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 290 | `hooks()->apply_filters('invoice_status_pdf_color', …)` | — (frontend Next.js) | SKIP |
| 458 | `hooks()->apply_filters('format_invoice_number', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/misc_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 68 | `hooks()->apply_filters('system_favourite_colors', …)` | — (frontend Next.js) | SKIP |
| 123 | `hooks()->apply_filters('acceptance_info_array', …)` | Pipeline / Eloquent model events | ⏳ |
| 203 | `hooks()->apply_filters('alert_class', …)` | Pipeline / Eloquent model events | ⏳ |
| 428 | `hooks()->apply_filters('scheduled_email_default_date', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/modules_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 315 | `hooks()->apply_filters('old_filter_name', …)` | — (frontend Next.js) | SKIP |
| 317 | `hooks()->apply_filters('old_filter_name', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/payment_gateways_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 13 | `hooks()->apply_filters('payment_gateway_logo_width', …)` | — (frontend Next.js) | SKIP |
| 14 | `hooks()->apply_filters('payment_gateway_logo_height', …)` | — (frontend Next.js) | SKIP |
| 32 | `hooks()->apply_filters('payment_gateway_logo_url', …)` | — (frontend Next.js) | SKIP |
| 84 | `hooks()->apply_filters('payment_gateway_head', …)` | — (frontend Next.js) | SKIP |
| 107 | `hooks()->apply_filters('payment_gateway_scripts', …)` | Pipeline / Eloquent model events | ⏳ |
| 117 | `hooks()->apply_filters('payment_gateway_footer', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/pdf_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 72 | `hooks()->apply_filters('pdf_logo_url', …)` | — (frontend Next.js) | SKIP |
| 101 | `hooks()->apply_filters('pdf_fonts_list', …)` | — (frontend Next.js) | SKIP |
| 142 | `hooks()->apply_filters('pdf_format_array', …)` | — (PdfService) | ⏳ Spine |

### `application/helpers/projects_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 219 | `hooks()->apply_filters('project_filtered_visible_tabs', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/proposals_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 154 | `hooks()->apply_filters('proposal_number_format', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/relation_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 144 | `hooks()->apply_filters('get_relation_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 330 | `hooks()->apply_filters('relation_values', …)` | Pipeline / Eloquent model events | ⏳ |
| 411 | `hooks()->apply_filters('init_relation_options', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/sales_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 69 | `hooks()->apply_filters('number_after_format', …)` | Pipeline / Eloquent model events | ⏳ |
| 145 | `hooks()->apply_filters('app_format_money', …)` | Pipeline / Eloquent model events | ⏳ |
| 188 | `hooks()->apply_filters('ajax_on_total_items', …)` | Pipeline / Eloquent model events | ⏳ |
| 272 | `hooks()->apply_filters('info_format_custom_field', …)` | Pipeline / Eloquent model events | ⏳ |
| 338 | `hooks()->apply_filters('customer_info_format_company_name', …)` | Pipeline / Eloquent model events | ⏳ |
| 416 | `hooks()->apply_filters('customer_info_text', …)` | Pipeline / Eloquent model events | ⏳ |
| 489 | `hooks()->apply_filters('proposal_info_text', …)` | Pipeline / Eloquent model events | ⏳ |
| 527 | `hooks()->apply_filters('organization_info_text', …)` | Pipeline / Eloquent model events | ⏳ |
| 538 | `hooks()->apply_filters('app_decimal_places', …)` | Pipeline / Eloquent model events | ⏳ |
| 812 | `hooks()->apply_filters('items_table_class', …)` | — (frontend Next.js) | SKIP |
| 840 | `hooks()->apply_filters('sales_number_format', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/sms_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 64 | `hooks()->apply_filters('sms_gateways', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/staff_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 173 | `hooks()->apply_filters('staff_permissions', …)` | Gate/permission (native) | ✅ native |
| 353 | `hooks()->apply_filters('total_recent_searches', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/subscriptions_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 94 | `hooks()->apply_filters('subscription_invoice_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 173 | `hooks()->apply_filters('subscription_statuses', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/tasks_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 19 | `hooks()->apply_filters('task_status_name', …)` | Pipeline / Eloquent model events | ⏳ |
| 43 | `hooks()->apply_filters('tasks_priorities', …)` | Pipeline / Eloquent model events | ⏳ |
| 312 | `hooks()->apply_filters('tasks_related_table_columns', …)` | — (frontend Next.js) | SKIP |
| 530 | `hooks()->apply_filters('before_get_task_timer_round_off_options', …)` | — (frontend Next.js) | SKIP |
| 542 | `hooks()->apply_filters('before_get_task_timer_round_off_times', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/template_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 14 | `hooks()->apply_filters('html_purify_content', …)` | — (frontend Next.js) | SKIP |
| 34 | `hooks()->apply_filters('html_purify_safe_iframe_regexp', …)` | Pipeline / Eloquent model events | ⏳ |
| 47 | `hooks()->apply_filters('html_purifier_config', …)` | Pipeline / Eloquent model events | ⏳ |
| 305 | `hooks()->apply_filters('logo_href', …)` | Pipeline / Eloquent model events | ⏳ |
| 318 | `hooks()->apply_filters('company_logo', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/themes_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 161 | `hooks()->apply_filters('customers_theme_assets_url', …)` | — (frontend Next.js) | SKIP |
| 170 | `hooks()->apply_filters('customers_theme_assets_path', …)` | — (frontend Next.js) | SKIP |
| 179 | `hooks()->apply_filters('terms_and_condition_url', …)` | Pipeline / Eloquent model events | ⏳ |
| 187 | `hooks()->apply_filters('privacy_policy_url', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/helpers/tickets_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 137 | `hooks()->apply_filters('show_ticket_submitter_on_clients_area_table', …)` | — (frontend Next.js) | SKIP |
| 168 | `hooks()->apply_filters('clients_area_tickets_summary', …)` | — (frontend Next.js) | SKIP |
| 192 | `hooks()->apply_filters('forbidden_ticket_statuses_to_change_in_clients_area', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/upload_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 672 | `hooks()->apply_filters('company_logo_upload_allowed_extensions', …)` | — (frontend Next.js) | SKIP |
| 803 | `hooks()->apply_filters('staff_profile_image_upload_allowed_extensions', …)` | — (frontend Next.js) | SKIP |
| 821 | `hooks()->apply_filters('staff_profile_image_thumb_width', …)` | — (frontend Next.js) | SKIP |
| 822 | `hooks()->apply_filters('staff_profile_image_thumb_height', …)` | — (frontend Next.js) | SKIP |
| 830 | `hooks()->apply_filters('staff_profile_image_small_width', …)` | — (frontend Next.js) | SKIP |
| 831 | `hooks()->apply_filters('staff_profile_image_small_height', …)` | — (frontend Next.js) | SKIP |
| 875 | `hooks()->apply_filters('contact_profile_image_upload_allowed_extensions', …)` | — (frontend Next.js) | SKIP |
| 893 | `hooks()->apply_filters('contact_profile_image_thumb_width', …)` | — (frontend Next.js) | SKIP |
| 894 | `hooks()->apply_filters('contact_profile_image_thumb_height', …)` | — (frontend Next.js) | SKIP |
| 902 | `hooks()->apply_filters('contact_profile_image_small_width', …)` | — (frontend Next.js) | SKIP |
| 903 | `hooks()->apply_filters('contact_profile_image_small_height', …)` | — (frontend Next.js) | SKIP |
| 1150 | `hooks()->apply_filters('get_upload_path_by_type', …)` | — (frontend Next.js) | SKIP |

### `application/helpers/widgets_helper.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 64 | `hooks()->apply_filters('get_dashboard_widgets', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/Clients.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 355 | `hooks()->apply_filters('client_project_total_tasks', …)` | Pipeline / Eloquent model events | ⏳ |
| 362 | `hooks()->apply_filters('client_project_tasks_not_completed', …)` | Pipeline / Eloquent model events | ⏳ |
| 369 | `hooks()->apply_filters('client_project_tasks_completed', …)` | Pipeline / Eloquent model events | ⏳ |
| 506 | `hooks()->apply_filters('customers_area_files_where', …)` | — (frontend Next.js) | SKIP |
| 609 | `hooks()->apply_filters('customers_area_list_default_ticket_statuses', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/Contract.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 69 | `hooks()->apply_filters('contract_html_pdf_data', …)` | — (frontend Next.js) | SKIP |
| 79 | `hooks()->apply_filters('contract_customers_area_view_data', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/Cron.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 17 | `hooks()->apply_filters('cron_functions_execute_seconds', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/controllers/Download.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 231 | `hooks()->apply_filters('download_file_path', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/controllers/Estimate.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 66 | `hooks()->apply_filters('customers_area_download_estimate_filename', …)` | — (frontend Next.js) | SKIP |
| 82 | `hooks()->apply_filters('estimate_html_pdf_data', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/Forms.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 448 | `hooks()->apply_filters('before_add_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 691 | `hooks()->apply_filters('disable_navigation_on_public_ticket_view', …)` | — (frontend Next.js) | SKIP |
| 719 | `hooks()->apply_filters('ticket_form_settings', …)` | Pipeline / Eloquent model events | ⏳ |
| 776 | `hooks()->apply_filters('ticket_external_form_insert_data', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/controllers/Invoice.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 12 | `hooks()->apply_filters('before_client_view_invoice', …)` | — (frontend Next.js) | SKIP |
| 72 | `hooks()->apply_filters('invoice_html_pdf_data', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/Migration.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 212 | `hooks()->apply_filters('migration_tables_to_replace_old_links', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/Proposal.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 84 | `hooks()->apply_filters('proposal_html_pdf_data', …)` | — (PdfService) | ⏳ Spine |
| 98 | `hooks()->apply_filters('proposal_customers_area_view_data', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Clients.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 157 | `hooks()->apply_filters('check_vault_entries_visibility', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/controllers/admin/Dashboard.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 55 | `hooks()->apply_filters('projects_activity_dashboard_limit', …)` | — (frontend Next.js) | SKIP |
| 81 | `hooks()->apply_filters('before_dashboard_render', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Estimates.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 534 | `hooks()->apply_filters('estimate_file_name_admin_area', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Invoices.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 650 | `hooks()->apply_filters('before_admin_view_invoice_pdf', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Leads.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 174 | `hooks()->apply_filters('lead_view_data', …)` | — (frontend Next.js) | SKIP |
| 808 | `hooks()->apply_filters('lead_form_available_database_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/controllers/admin/Projects.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 265 | `hooks()->apply_filters('admin_total_project_tasks_where', …)` | Pipeline / Eloquent model events | ⏳ |
| 337 | `hooks()->apply_filters('default_tickets_list_statuses', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Tasks.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 144 | `hooks()->apply_filters('before_update_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 880 | `hooks()->apply_filters('before_update_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 929 | `hooks()->apply_filters('before_update_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 1105 | `hooks()->apply_filters('before_update_task', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/controllers/admin/Tickets.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 60 | `hooks()->apply_filters('default_tickets_list_statuses', …)` | — (frontend Next.js) | SKIP |

### `application/controllers/admin/Utilities.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 272 | `hooks()->apply_filters('before_init_media', …)` | ServiceProvider/config (native) | NATIVE |
| 365 | `hooks()->apply_filters('bulk_pdf_export_available_features', …)` | — (frontend Next.js) | SKIP |

### `application/language/indonesia/indonesia_num_words_lang.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 134 | `hooks()->apply_filters('before_number_format_render_languge_currencies', …)` | — (frontend Next.js) | SKIP |

### `application/language/english/english_num_words_lang.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 134 | `hooks()->apply_filters('before_number_format_render_languge_currencies', …)` | — (frontend Next.js) | SKIP |

### `application/models/Announcements_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 99 | `hooks()->apply_filters('before_announcement_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 125 | `hooks()->apply_filters('before_announcement_updated', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Clients_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 13 | `hooks()->apply_filters('contact_columns', …)` | — (frontend Next.js) | SKIP |
| 146 | `hooks()->apply_filters('before_client_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 239 | `hooks()->apply_filters('before_client_updated', …)` | Pipeline / Eloquent model events | ⏳ |
| 354 | `hooks()->apply_filters('before_update_contact', …)` | Pipeline / Eloquent model events | ⏳ |
| 515 | `hooks()->apply_filters('before_create_contact', …)` | Pipeline / Eloquent model events | ⏳ |
| 641 | `hooks()->apply_filters('before_create_contact', …)` | Pipeline / Eloquent model events | ⏳ |
| 724 | `hooks()->apply_filters('customer_update_company_info', …)` | Pipeline / Eloquent model events | ⏳ |
| 1311 | `hooks()->apply_filters('change_contact_status', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Contracts_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 126 | `hooks()->apply_filters('before_contract_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 172 | `hooks()->apply_filters('before_contract_updated', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Credit_notes_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 17 | `hooks()->apply_filters('before_get_credit_notes_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 196 | `hooks()->apply_filters('before_create_credit_note', …)` | Pipeline / Eloquent model events | ⏳ |
| 269 | `hooks()->apply_filters('before_update_credit_note', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Cron_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 92 | `hooks()->apply_filters('cron_retry_email_queue_seconds', …)` | ServiceProvider/config (native) | NATIVE |
| 170 | `hooks()->apply_filters('delete_two_checkout_log_older_than_days', …)` | ServiceProvider/config (native) | NATIVE |
| 195 | `hooks()->apply_filters('event_notifications', …)` | — (frontend Next.js) | SKIP |
| 237 | `hooks()->apply_filters('event_notifications', …)` | — (frontend Next.js) | SKIP |
| 439 | `hooks()->apply_filters('recurring_task_status', …)` | Pipeline / Eloquent model events | ⏳ |
| 600 | `hooks()->apply_filters('send_recurring_system_expenses_email', …)` | Pipeline / Eloquent model events | ⏳ |
| 835 | `hooks()->apply_filters('send_recurring_invoices_system_email', …)` | Pipeline / Eloquent model events | ⏳ |
| 1340 | `hooks()->apply_filters('leads_email_integration_email_body_for_database', …)` | — (frontend Next.js) | SKIP |
| 1368 | `hooks()->apply_filters('before_add_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 1400 | `hooks()->apply_filters('leads_email_integration_lead_check', …)` | Pipeline / Eloquent model events | ⏳ |
| 1468 | `hooks()->apply_filters('before_insert_lead_from_email_integration', …)` | Pipeline / Eloquent model events | ⏳ |
| 1654 | `hooks()->apply_filters('imap_fetch_from_email_by_reply_to_header', …)` | — (frontend Next.js) | SKIP |
| 1676 | `hooks()->apply_filters('imap_auto_import_ticket_data', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Departments_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 67 | `hooks()->apply_filters('before_department_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 125 | `hooks()->apply_filters('before_department_updated', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Emails_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 195 | `hooks()->apply_filters('before_send_simple_email', …)` | Pipeline / Eloquent model events | ⏳ |
| 277 | `hooks()->apply_filters('send_email_template_to', …)` | `Mailable (native)` | ✅ native |
| 338 | `hooks()->apply_filters('before_parse_email_template_message', …)` | Pipeline / Eloquent model events | ⏳ |
| 342 | `hooks()->apply_filters('after_parse_email_template_message', …)` | Pipeline / Eloquent model events | ⏳ |
| 408 | `hooks()->apply_filters('before_email_template_send', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Estimate_request_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 311 | `hooks()->apply_filters('default_estimate_request_status_color', …)` | — (frontend Next.js) | SKIP |

### `application/models/Estimates_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 18 | `hooks()->apply_filters('before_set_estimate_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 510 | `hooks()->apply_filters('before_estimate_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 631 | `hooks()->apply_filters('before_estimate_updated', …)` | Pipeline / Eloquent model events | ⏳ |
| 1244 | `hooks()->apply_filters('send_estimate_to_customer_file_name', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Expenses_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 124 | `hooks()->apply_filters('before_expense_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 413 | `hooks()->apply_filters('before_expense_updated', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Invoice_items_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 232 | `hooks()->apply_filters('before_update_item', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Invoices_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 130 | `hooks()->apply_filters('get_invoice', …)` | Pipeline / Eloquent model events | ⏳ |
| 382 | `hooks()->apply_filters('before_invoice_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 585 | `hooks()->apply_filters('invoices_ids_available_for_merging', …)` | Pipeline / Eloquent model events | ⏳ |
| 808 | `hooks()->apply_filters('before_invoice_updated', …)` | Pipeline / Eloquent model events | ⏳ |
| 1359 | `hooks()->apply_filters('invoice_overdue_notice_attach_pdf', …)` | — (PdfService) | ⏳ Spine |
| 1445 | `hooks()->apply_filters('invoice_due_notice_attach_pdf', …)` | — (PdfService) | ⏳ Spine |
| 1529 | `hooks()->apply_filters('invoice_object_before_send_to_client', …)` | Pipeline / Eloquent model events | ⏳ |
| 1539 | `hooks()->apply_filters('after_invoice_sent_template_statement', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Knowledge_base_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 47 | `hooks()->apply_filters('total_related_articles', …)` | Pipeline / Eloquent model events | ⏳ |
| 91 | `hooks()->apply_filters('before_add_kb_article', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Leads_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 96 | `hooks()->apply_filters('before_lead_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 724 | `hooks()->apply_filters('default_lead_status_color', …)` | — (frontend Next.js) | SKIP |
| 862 | `hooks()->apply_filters('lead_activity_log_default_sort', …)` | — (frontend Next.js) | SKIP |

### `application/models/Misc_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 19 | `hooks()->apply_filters('notifications_limit', …)` | Pipeline / Eloquent model events | ⏳ |
| 283 | `hooks()->apply_filters('get_notes', …)` | Pipeline / Eloquent model events | ⏳ |
| 294 | `hooks()->apply_filters('create_note_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 799 | `hooks()->apply_filters('global_search_result_query', …)` | — (frontend Next.js) | SKIP |

### `application/models/Payment_modes_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 31 | `hooks()->apply_filters('before_add_online_payment_modes', …)` | Pipeline / Eloquent model events | ⏳ |
| 37 | `hooks()->apply_filters('before_add_payment_gateways', …)` | Pipeline / Eloquent model events | ⏳ |
| 207 | `hooks()->apply_filters('app_payment_gateways', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Payments_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 131 | `hooks()->apply_filters('before_process_gateway_func', …)` | Pipeline / Eloquent model events | ⏳ |
| 203 | `hooks()->apply_filters('before_payment_recorded', …)` | Pipeline / Eloquent model events | ⏳ |
| 384 | `hooks()->apply_filters('before_payment_updated', …)` | Pipeline / Eloquent model events | ⏳ |
| 445 | `hooks()->apply_filters('before_payment_recorded', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Projects_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 39 | `hooks()->apply_filters('project_settings', …)` | Pipeline / Eloquent model events | ⏳ |
| 44 | `hooks()->apply_filters('before_get_project_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 271 | `hooks()->apply_filters('project_get', …)` | Pipeline / Eloquent model events | ⏳ |
| 369 | `hooks()->apply_filters('project_tasks_array_default_order', …)` | Pipeline / Eloquent model events | ⏳ |
| 383 | `hooks()->apply_filters('get_projects_tasks', …)` | Pipeline / Eloquent model events | ⏳ |
| 758 | `hooks()->apply_filters('before_add_project', …)` | Pipeline / Eloquent model events | ⏳ |
| 1021 | `hooks()->apply_filters('before_update_project', …)` | Pipeline / Eloquent model events | ⏳ |
| 1592 | `hooks()->apply_filters('before_add_project_discussion_comment', …)` | Pipeline / Eloquent model events | ⏳ |
| 2302 | `hooks()->apply_filters('before_log_project_activity', …)` | ServiceProvider/config (native) | NATIVE |

### `application/models/Proposals_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 17 | `hooks()->apply_filters('before_set_proposal_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 92 | `hooks()->apply_filters('before_create_proposal', …)` | Pipeline / Eloquent model events | ⏳ |
| 221 | `hooks()->apply_filters('before_proposal_updated', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Settings_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 35 | `hooks()->apply_filters('before_settings_updated', …)` | Pipeline / Eloquent model events | ⏳ |
| 76 | `hooks()->apply_filters('before_single_setting_updated_in_loop', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Staff_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 512 | `hooks()->apply_filters('before_update_staff_member', …)` | Pipeline / Eloquent model events | ⏳ |
| 673 | `hooks()->apply_filters('before_staff_update_profile', …)` | Pipeline / Eloquent model events | ⏳ |
| 709 | `hooks()->apply_filters('before_staff_change_password', …)` | Pipeline / Eloquent model events | ⏳ |
| 753 | `hooks()->apply_filters('before_staff_status_change', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Statement_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 234 | `hooks()->apply_filters('statement', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Tasks_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 39 | `hooks()->apply_filters('before_get_task_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 133 | `hooks()->apply_filters('get_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 210 | `hooks()->apply_filters('before_add_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 532 | `hooks()->apply_filters('before_add_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 767 | `hooks()->apply_filters('before_update_task', …)` | Pipeline / Eloquent model events | ⏳ |
| 1292 | `hooks()->apply_filters('add_task_attachment_as_comment', …)` | Pipeline / Eloquent model events | ⏳ |
| 1350 | `hooks()->apply_filters('task_comments_order', …)` | Pipeline / Eloquent model events | ⏳ |
| 1920 | `hooks()->apply_filters('before_task_timer_stopped', …)` | Pipeline / Eloquent model events | ⏳ |
| 2281 | `hooks()->apply_filters('should_staff_receive_task_notification', …)` | — (frontend Next.js) | SKIP |

### `application/models/Templates_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 20 | `hooks()->apply_filters('before_template_added', …)` | Pipeline / Eloquent model events | ⏳ |
| 65 | `hooks()->apply_filters('before_template_deleted', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Tickets_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 51 | `hooks()->apply_filters('piped_ticket_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 460 | `hooks()->apply_filters('ticket_message_without_html_for_non_admin', …)` | Pipeline / Eloquent model events | ⏳ |
| 470 | `hooks()->apply_filters('before_ticket_reply_add', …)` | Pipeline / Eloquent model events | ⏳ |
| 487 | `hooks()->apply_filters('ticket_reply_status', …)` | Pipeline / Eloquent model events | ⏳ |
| 720 | `hooks()->apply_filters('ticket_replies_order', …)` | Pipeline / Eloquent model events | ⏳ |
| 809 | `hooks()->apply_filters('ticket_message_without_html_for_non_admin', …)` | Pipeline / Eloquent model events | ⏳ |
| 829 | `hooks()->apply_filters('before_ticket_created', …)` | Pipeline / Eloquent model events | ⏳ |
| 1054 | `hooks()->apply_filters('before_ticket_settings_updated', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Todo_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 12 | `hooks()->apply_filters('todos_limit', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/models/Utilities_model.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 44 | `hooks()->apply_filters('event_update_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 55 | `hooks()->apply_filters('event_create_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 142 | `hooks()->apply_filters('before_fetch_events', …)` | Pipeline / Eloquent model events | ⏳ |
| 512 | `hooks()->apply_filters('calendar_data', …)` | — (frontend Next.js) | SKIP |

### `application/services/CustomerProfileBadges.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 36 | `hooks()->apply_filters('customers_profile_tab_badge', …)` | — (frontend Next.js) | SKIP |

### `application/services/LeadProfileBadges.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 28 | `hooks()->apply_filters('lead_tab_badge_count', …)` | — (frontend Next.js) | SKIP |

### `application/services/messages/IsCronSetupRequired.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 87 | `hooks()->apply_filters('numbers_of_features_using_cron_job', …)` | ServiceProvider/config (native) | NATIVE |
| 88 | `hooks()->apply_filters('used_cron_features', …)` | ServiceProvider/config (native) | NATIVE |

### `application/libraries/App.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 202 | `hooks()->apply_filters('before_get_languages', …)` | — (frontend Next.js) | SKIP |
| 213 | `hooks()->apply_filters('table_params', …)` | — (frontend Next.js) | SKIP |
| 281 | `hooks()->apply_filters('get_option', …)` | — (frontend Next.js) | SKIP |
| 303 | `hooks()->apply_filters('quick_actions_links', …)` | — (frontend Next.js) | SKIP |
| 321 | `hooks()->apply_filters('show_setup_menu', …)` | — (frontend Next.js) | SKIP |
| 330 | `hooks()->apply_filters('tables_with_currency', …)` | — (frontend Next.js) | SKIP |
| 339 | `hooks()->apply_filters('get_media_folder', …)` | Pipeline / Eloquent model events | ⏳ |
| 412 | `hooks()->apply_filters('before_set_media_folder', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/App_bulk_pdf_export.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 185 | `hooks()->apply_filters('bulk_pdf_export_class', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/App_clients_area_constructor.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 62 | `hooks()->apply_filters('customers_area_autoloaded_vars', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/App_items_table.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 100 | `hooks()->apply_filters('item_preview_rate', …)` | — (frontend Next.js) | SKIP |
| 118 | `hooks()->apply_filters('item_preview_amount_with_currency', …)` | — (frontend Next.js) | SKIP |
| 240 | `hooks()->apply_filters('item_description_td_width', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/App_items_table_template.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 205 | `hooks()->apply_filters('item_tax_table_row', …)` | — (frontend Next.js) | SKIP |
| 208 | `hooks()->apply_filters('item_tax_table_row', …)` | — (frontend Next.js) | SKIP |
| 478 | `hooks()->apply_filters('items_table_amounts_exclude_currency_symbol', …)` | — (frontend Next.js) | SKIP |
| 486 | `hooks()->apply_filters('show_tax_per_item', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/App_menu.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 102 | `hooks()->apply_filters('nav_user_menu_items', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/App_number_to_word.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 178 | `hooks()->apply_filters('before_return_num_word', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/App_pusher.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 31 | `hooks()->apply_filters('pusher_options', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/Stripe_core.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 102 | `hooks()->apply_filters('stripe_webhook_events', …)` | ServiceProvider/config (native) | NATIVE |

### `application/libraries/import/Import_customers.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 16 | `hooks()->apply_filters('not_importable_clients_fields', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/import/Import_leads.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 16 | `hooks()->apply_filters('not_importable_leads_fields', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/gateways/Paypal_checkout_gateway.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 94 | `hooks()->apply_filters('paypal_checkout_button_style_params', …)` | Pipeline / Eloquent model events | ⏳ |
| 130 | `hooks()->apply_filters('paypal_checkout_order_create_data', …)` | Pipeline / Eloquent model events | ⏳ |
| 204 | `hooks()->apply_filters('paypal_checkout_payer_data', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/gateways/Paypal_gateway.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 88 | `hooks()->apply_filters('paypal_logo_url', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/mails/App_mail_template.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 100 | `hooks()->apply_filters('send_email_template_to', …)` | `Mailable (native)` | ✅ native |
| 134 | `hooks()->apply_filters('before_parse_email_template_message', …)` | Pipeline / Eloquent model events | ⏳ |
| 138 | `hooks()->apply_filters('after_parse_email_template_message', …)` | Pipeline / Eloquent model events | ⏳ |
| 163 | `hooks()->apply_filters('before_email_template_send', …)` | Pipeline / Eloquent model events | ⏳ |
| 287 | `hooks()->apply_filters('use_deprecated_from_email_header_template_field', …)` | — (frontend Next.js) | SKIP |
| 306 | `hooks()->apply_filters('email_template_from_headers', …)` | — (frontend Next.js) | SKIP |
| 514 | `hooks()->apply_filters('email_template_language', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/merge_fields/App_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 53 | `hooks()->apply_filters('register_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |
| 210 | `hooks()->apply_filters('available_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Client_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 479 | `hooks()->apply_filters('client_contact_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |
| 503 | `hooks()->apply_filters('client_statement_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Contract_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 120 | `hooks()->apply_filters('contract_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Credit_note_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 95 | `hooks()->apply_filters('credit_note_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Estimate_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 117 | `hooks()->apply_filters('estimate_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Estimate_request_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 129 | `hooks()->apply_filters('estimate_request_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Event_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 71 | `hooks()->apply_filters('event_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Invoice_batch_payments_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 40 | `hooks()->apply_filters('invoice_batch_payments_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Invoice_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 217 | `hooks()->apply_filters('invoice_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Leads_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 262 | `hooks()->apply_filters('lead_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Notifications_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 42 | `hooks()->apply_filters('notifications_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Other_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 27 | `hooks()->apply_filters('other_merge_fields_available_for', …)` | Pipeline / Eloquent model events | ⏳ |
| 98 | `hooks()->apply_filters('merge_field_logo_img_width', …)` | — (frontend Next.js) | SKIP |
| 132 | `hooks()->apply_filters('other_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Projects_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 225 | `hooks()->apply_filters('project_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Proposals_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 180 | `hooks()->apply_filters('proposal_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Staff_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 189 | `hooks()->apply_filters('staff_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |
| 212 | `hooks()->apply_filters('staff_reminder_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Subscriptions_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 84 | `hooks()->apply_filters('subscription_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Tasks_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 200 | `hooks()->apply_filters('task_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/merge_fields/Ticket_merge_fields.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 208 | `hooks()->apply_filters('ticket_merge_fields', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/libraries/sms/App_sms.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 87 | `hooks()->apply_filters('get_sms_gateways', …)` | Pipeline / Eloquent model events | ⏳ |
| 109 | `hooks()->apply_filters('sms_gateway_available_triggers', …)` | — (frontend Next.js) | SKIP |
| 406 | `hooks()->apply_filters('sms_triggers', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/sms/Sms_msg91.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 196 | `hooks()->apply_filters('msg91_common_options', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/App_pdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 178 | `hooks()->apply_filters('process_pdf_signature_on_close', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/Contract_pdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 14 | `hooks()->apply_filters('contract_html_pdf_data', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/Estimate_pdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 17 | `hooks()->apply_filters('estimate_html_pdf_data', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/Invoice_pdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 16 | `hooks()->apply_filters('invoice_html_pdf_data', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/PDF_Signature.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 51 | `hooks()->apply_filters('pdf_signature_break_lines', …)` | — (PdfService) | ⏳ Spine |
| 99 | `hooks()->apply_filters('blank_signature_line', …)` | — (frontend Next.js) | SKIP |
| 109 | `hooks()->apply_filters('pdf_signature_break_lines', …)` | — (PdfService) | ⏳ Spine |
| 128 | `hooks()->apply_filters('pdf_customer_signature_image_path', …)` | — (frontend Next.js) | SKIP |

### `application/libraries/pdf/Proposal_pdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 27 | `hooks()->apply_filters('proposal_html_pdf_data', …)` | — (PdfService) | ⏳ Spine |

### `application/views/admin/search.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 80 | `hooks()->apply_filters('global_search_result_output', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/emails/template.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 20 | `hooks()->apply_filters('show_deprecated_from_email_header_template_field', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/scripts.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 27 | `hooks()->apply_filters('pusher_options', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/setup_menu.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 64 | `hooks()->apply_filters('help_menu_item_link', …)` | — (frontend Next.js) | SKIP |
| 65 | `hooks()->apply_filters('help_menu_item_text', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/includes/modals/newsfeed_form.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 26 | `hooks()->apply_filters('total_pages_newsfeed', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/contracts/contract.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 309 | `hooks()->apply_filters('new_contract_default_content', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/contracts/manage.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 81 | `hooks()->apply_filters('contracts_table_default_order', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/contracts/table_html.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 26 | `hooks()->apply_filters('contracts_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/estimate_request/estimate_request.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 282 | `hooks()->apply_filters('contact_email_required', …)` | Pipeline / Eloquent model events | ⏳ |
| 286 | `hooks()->apply_filters('contact_email_unique', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/estimate_request/manage_request.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 41 | `hooks()->apply_filters('estimate_request_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/clients/client_js.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 169 | `hooks()->apply_filters('projects_table_default_order', …)` | — (frontend Next.js) | SKIP |
| 272 | `hooks()->apply_filters('contact_email_required', …)` | Pipeline / Eloquent model events | ⏳ |
| 277 | `hooks()->apply_filters('contact_email_unique', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/clients/manage.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 319 | `hooks()->apply_filters('customers_table_columns', …)` | — (frontend Next.js) | SKIP |
| 341 | `hooks()->apply_filters('customers_table_default_order', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/clients/groups/profile.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 24 | `hooks()->apply_filters('customer_profile_tab_custom_fields_text', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/clients/groups/proposals.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 26 | `hooks()->apply_filters('proposals_relation_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/payments/manage.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 15 | `hooks()->apply_filters('payments_table_default_order', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/invoices/invoice_template.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 300 | `hooks()->apply_filters('invoice_currency_disabled', …)` | Pipeline / Eloquent model events | ⏳ |
| 316 | `hooks()->apply_filters('invoice_currency_attributes', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/invoices/table_html.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 24 | `hooks()->apply_filters('invoices_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/estimates/estimate_template.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 214 | `hooks()->apply_filters('estimate_currency_disabled', …)` | Pipeline / Eloquent model events | ⏳ |
| 229 | `hooks()->apply_filters('estimate_currency_attributes', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/estimates/table_html.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 28 | `hooks()->apply_filters('estimates_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/info.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 528 | `hooks()->apply_filters('system_info_files_permissions_issue', …)` | Gate/permission (native) | ✅ native |

### `application/views/admin/settings/includes/leads.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 36 | `hooks()->apply_filters('lead_available_dupicate_validation_fields_option', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/localization.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 38 | `hooks()->apply_filters('settings_language_subtext', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/settings/includes/tickets.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 50 | `hooks()->apply_filters('cpanel_tickets_forwarder_path', …)` | Pipeline / Eloquent model events | ⏳ |
| 69 | `hooks()->apply_filters('ticket_form_file_location_settings', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/tables/all_contacts.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 129 | `hooks()->apply_filters('all_contacts_table_row', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/clients.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 39 | `hooks()->apply_filters('customers_table_sql_join', …)` | — (frontend Next.js) | SKIP |
| 159 | `hooks()->apply_filters('customers_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 264 | `hooks()->apply_filters('customers_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/contracts.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 108 | `hooks()->apply_filters('contracts_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 183 | `hooks()->apply_filters('contracts_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/estimate_request.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 51 | `hooks()->apply_filters('estimate_request_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 53 | `hooks()->apply_filters('estimate_request_table_additional_columns_sql', …)` | — (frontend Next.js) | SKIP |
| 141 | `hooks()->apply_filters('estimate_request_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/estimates.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 102 | `hooks()->apply_filters('estimates_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 180 | `hooks()->apply_filters('estimates_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/expenses.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 51 | `hooks()->apply_filters('expenses_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 176 | `hooks()->apply_filters('expenses_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/invoices.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 112 | `hooks()->apply_filters('invoices_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 187 | `hooks()->apply_filters('invoices_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/leads.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 92 | `hooks()->apply_filters('leads_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 99 | `hooks()->apply_filters('leads_table_additional_columns_sql', …)` | — (frontend Next.js) | SKIP |
| 236 | `hooks()->apply_filters('leads_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/projects.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 64 | `hooks()->apply_filters('projects_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 149 | `hooks()->apply_filters('projects_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/proposals.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 88 | `hooks()->apply_filters('proposals_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 157 | `hooks()->apply_filters('proposals_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/proposals_relations.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 50 | `hooks()->apply_filters('proposals_relation_table_sql_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/staff.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 35 | `hooks()->apply_filters('staff_table_sql_where', …)` | — (frontend Next.js) | SKIP |
| 101 | `hooks()->apply_filters('staff_table_row', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/tasks.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 39 | `hooks()->apply_filters('tasks_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 209 | `hooks()->apply_filters('tasks_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/tasks_relations.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 74 | `hooks()->apply_filters('tasks_related_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 234 | `hooks()->apply_filters('tasks_related_table_row_data', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/timesheets.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 18 | `hooks()->apply_filters('projects_timesheets_table_sql_columns', …)` | — (frontend Next.js) | SKIP |
| 25 | `hooks()->apply_filters('projects_timesheets_table_sql_join', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tables/includes/tasks_filter.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 68 | `hooks()->apply_filters('tasks_table_sql_where', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/proposals/manage.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 125 | `hooks()->apply_filters('proposals_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/proposals/proposal.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 115 | `hooks()->apply_filters('proposal_currency_disabled', …)` | Pipeline / Eloquent model events | ⏳ |
| 116 | `hooks()->apply_filters('proposal_currency_attributes', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/leads/email_integration.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 79 | `hooks()->apply_filters('leads_email_integration_check_every', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/leads/lead.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 55 | `hooks()->apply_filters('lead_email_activity_subject', …)` | ServiceProvider/config (native) | NATIVE |
| 250 | `hooks()->apply_filters('proposals_relation_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/leads/manage_leads.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 278 | `hooks()->apply_filters('leads_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/subscriptions/table_html.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 51 | `hooks()->apply_filters('subscriptions_table_default_order', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/credit_notes/credit_note.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 197 | `hooks()->apply_filters('credit_note_currency_disabled', …)` | Pipeline / Eloquent model events | ⏳ |
| 213 | `hooks()->apply_filters('credit_note_currency_attributes', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/expenses/expense.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 125 | `hooks()->apply_filters('expense_currency_disabled', …)` | Pipeline / Eloquent model events | ⏳ |
| 155 | `hooks()->apply_filters('expense_currency_attributes', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/expenses/manage.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 92 | `hooks()->apply_filters('expenses_table_default_order', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/expenses/table_html.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 43 | `hooks()->apply_filters('expenses_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tickets/add.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 73 | `hooks()->apply_filters('new_ticket_priority_selected', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tickets/single.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 257 | `hooks()->apply_filters('ticket_add_response_and_back_to_list_default', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/projects/manage.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 102 | `hooks()->apply_filters('projects_table_default_order', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/projects/project_timesheets.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 36 | `hooks()->apply_filters('projects_timesheets_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/projects/table_html.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 22 | `hooks()->apply_filters('projects_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/projects/view.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 177 | `hooks()->apply_filters('admin_project_progress_color', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tasks/_table.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 32 | `hooks()->apply_filters('tasks_table_columns', …)` | — (frontend Next.js) | SKIP |

### `application/views/admin/tasks/task.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 47 | `hooks()->apply_filters('task_copy_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 49 | `hooks()->apply_filters('copy_task_default_status', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/admin/tasks/view_task_template.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 381 | `hooks()->apply_filters('show_more_link_task_attachments', …)` | — (frontend Next.js) | SKIP |
| 593 | `hooks()->apply_filters('task_copy_statuses', …)` | Pipeline / Eloquent model events | ⏳ |
| 595 | `hooks()->apply_filters('copy_task_default_status', …)` | Pipeline / Eloquent model events | ⏳ |
| 649 | `hooks()->apply_filters('task_single_mark_as_statuses', …)` | Pipeline / Eloquent model events | ⏳ |

### `application/views/forms/ticket.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 8 | `hooks()->apply_filters('ticket_form_title', …)` | — (frontend Next.js) | SKIP |
| 56 | `hooks()->apply_filters('new_ticket_priority_selected', …)` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/template_parts/projects/edit_task.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 22 | `hooks()->apply_filters('task_priorities_select', …)` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/template_parts/projects/new_task.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 21 | `hooks()->apply_filters('task_priorities_select', …)` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/template_parts/projects/project_task.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 123 | `hooks()->apply_filters('show_more_link_task_attachments_customers_area', …)` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/consent.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 10 | `hooks()->apply_filters('consent_public_page_heading', …)` | — (frontend Next.js) | SKIP |

### `application/views/themes/perfex/views/credit_note_pdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 41 | `hooks()->apply_filters('credit_note_pdf_header_after_shipping_info', …)` | — (frontend Next.js) | SKIP |
| 45 | `hooks()->apply_filters('credit_note_pdf_header_after_date', …)` | — (frontend Next.js) | SKIP |
| 49 | `hooks()->apply_filters('credit_note_pdf_header_after_reference_no', …)` | — (frontend Next.js) | SKIP |
| 54 | `hooks()->apply_filters('credit_note_pdf_header_after_project', …)` | — (frontend Next.js) | SKIP |
| 57 | `hooks()->apply_filters('credit_note_pdf_header_before_custom_fields', …)` | — (frontend Next.js) | SKIP |
| 67 | `hooks()->apply_filters('credit_note_pdf_header_after_custom_fields', …)` | — (frontend Next.js) | SKIP |
| 75 | `hooks()->apply_filters('pdf_info_and_table_separator', …)` | — (PdfService) | ⏳ Spine |

### `application/views/themes/perfex/views/estimatepdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 74 | `hooks()->apply_filters('pdf_info_and_table_separator', …)` | — (PdfService) | ⏳ Spine |

### `application/views/themes/perfex/views/invoicepdf.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 52 | `hooks()->apply_filters('invoice_pdf_header_after_date', …)` | — (frontend Next.js) | SKIP |
| 56 | `hooks()->apply_filters('invoice_pdf_header_after_due_date', …)` | — (frontend Next.js) | SKIP |
| 61 | `hooks()->apply_filters('invoice_pdf_header_after_sale_agent', …)` | — (frontend Next.js) | SKIP |
| 66 | `hooks()->apply_filters('invoice_pdf_header_after_project_name', …)` | — (frontend Next.js) | SKIP |
| 69 | `hooks()->apply_filters('invoice_pdf_header_before_custom_fields', …)` | — (frontend Next.js) | SKIP |
| 79 | `hooks()->apply_filters('invoice_pdf_header_after_custom_fields', …)` | — (frontend Next.js) | SKIP |
| 87 | `hooks()->apply_filters('pdf_info_and_table_separator', …)` | — (PdfService) | ⏳ Spine |

### `application/views/themes/perfex/views/open_ticket.php`
| Line | Filter (BEFORE) | AFTER (Laravel) | Status |
|---|---|---|---|
| 52 | `hooks()->apply_filters('new_ticket_priority_selected', …)` | — (frontend Next.js) | SKIP |
