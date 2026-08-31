# Daftar Lengkap Hook & Filter — aplikasi legacy

*Ground truth 30 Agu 2026: **528 hook unik** (`do_action`) + **539 filter unik** (`apply_filters`) dari `application/` + `modules/`.*

## A. BACKEND — do_action (wajib ada di backend)

## ### A.1 Sudah di-port ke Spine (28) ✅

| Hook | Frekuensi | AFTER | Status |
|---|---|---|---|
| `before_remove_iso_logo` | 2 | `Spine\Events\FileDeleting` | ✅ ported |
| `before_remove_contact_profile_image` | 2 | `Spine\Events\FileDeleting` | ✅ ported |
| `sms_trigger_triggered` | 1 | `Spine\Events\SmsSent` | ✅ ported |
| `pdf_construct` | 1 | `Spine\Events\PdfCreating` | ✅ ported |
| `pdf_close` | 1 | `Spine\Events\PdfCreated` | ✅ ported |
| `notification_created` | 1 | `Spine\Events\NotificationSent` | ✅ ported |
| `module_uninstalled` | 1 | `Spine\Events\ModuleUninstalled` | ✅ ported |
| `module_installed` | 1 | `Spine\Events\ModuleInstalled` | ✅ ported |
| `module_deactivated` | 1 | `Spine\Events\ModuleDeactivated` | ✅ ported |
| `module_activated` | 1 | `Spine\Events\ModuleActivated` | ✅ ported |
| `before_upload_ticket_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_staff_profile_image` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_signature_image_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_project_discussion_comment_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_project_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_newsfeed_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_iso_logo_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_favicon_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_expense_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_estimate_request_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_contract_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_contact_profile_image` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_company_logo_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_upload_client_attachment` | 1 | `Spine\Events\FileUploading` | ✅ ported |
| `before_remove_staff_profile_image` | 1 | `Spine\Events\FileDeleting` | ✅ ported |
| `before_remove_project_file` | 1 | `Spine\Events\FileDeleting` | ✅ ported |
| `before_remove_favicon` | 1 | `Spine\Events\FileDeleting` | ✅ ported |
| `before_remove_company_logo` | 1 | `Spine\Events\FileDeleting` | ✅ ported |

## ### A.2 Native Laravel (16) ✅

| Hook | Frekuensi | AFTER | Status |
|---|---|---|---|
| `email_template_sent` | 4 | `Illuminate\Mail\Events\MessageSent` | ✅ native |
| `failed_to_send_email_template` | 3 | `Illuminate\Mail\Events\MessageSending` | ✅ native |
| `after_staff_login` | 3 | `Illuminate\Auth\Events\Login` | ✅ native |
| `before_user_reset_password` | 2 | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| `before_staff_login` | 2 | `Illuminate\Auth\Events\Login` | ✅ native |
| `after_user_reset_password` | 2 | `Illuminate\Auth\Events\PasswordReset` | ✅ native |
| `after_contact_login` | 2 | `Illuminate\Auth\Events\Login` | ✅ native |
| `set_password_email_sent` | 1 | `PasswordBroker (native)` | ✅ native |
| `modules_loaded` | 1 | `ServiceProvider::boot()` | ✅ native |
| `forgot_password_email_sent` | 1 | `PasswordBroker (native)` | ✅ native |
| `before_staff_logout` | 1 | `Illuminate\Auth\Events\Logout` | ✅ native |
| `before_contact_logout` | 1 | `Illuminate\Auth\Events\Logout` | ✅ native |
| `before_client_login` | 1 | `Illuminate\Auth\Events\Login` | ✅ native |
| `after_user_logout` | 1 | `Illuminate\Auth\Events\Logout` | ✅ native |
| `after_client_logout` | 1 | `Illuminate\Auth\Events\Logout` | ✅ native |
| `admin_init` | 1 | `ServiceProvider::boot()` | ✅ native |

## ### A.3 Deferred di Spine (14) ⏳

| Hook | Frekuensi | AFTER | Status |
|---|---|---|---|
| `before_cron_run` | 2 | — (cron Spine) | ⏳ Spine |
| `staff_profile_access` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `staff_member_updated` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `staff_member_profile_updated` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `staff_member_deleted` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `staff_member_created` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `smtp_test_email_success` | 1 | — (MailService::testSmtp (belum ada)) | ⏳ Spine |
| `smtp_test_email_failed` | 1 | — (MailService::testSmtp (belum ada)) | ⏳ Spine |
| `edit_logged_in_staff_profile` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `before_update_backup_options` | 1 | — (SettingUpdated saat settings-save) | ⏳ Spine |
| `before_staff_change_language` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `before_send_test_smtp_email` | 1 | — (MailService::testSmtp (belum ada)) | ⏳ Spine |
| `before_delete_staff_member` | 1 | — (CRUD staff (app konsumen)) | ⏳ Spine |
| `after_cron_run` | 1 | — (cron Spine) | ⏳ Spine |

## ### A.4 Domain → modul (258) ⏳

| Hook | Frekuensi |
|---|---|
| `after_update_task` | 5 |
| `lead_created` | 4 |
| `after_add_task` | 4 |
| `after_ticket_status_changed` | 3 |
| `task_status_changed` | 2 |
| `project_status_changed` | 2 |
| `lead_status_changed` | 2 |
| `contact_created` | 2 |
| `after_payment_added` | 2 |
| `after_gondola_added` | 2 |
| `after_bucket_added` | 2 |
| `web_to_lead_form_submitted` | 1 |
| `ticket_settings_updated` | 1 |
| `ticket_form_submitted` | 1 |
| `ticket_form_after_submit_button` | 1 |
| `ticket_form_after_subject` | 1 |
| `ticket_form_after_service` | 1 |
| `ticket_form_after_priority` | 1 |
| `ticket_form_after_name` | 1 |
| `ticket_form_after_message` | 1 |
| `ticket_form_after_email` | 1 |
| `ticket_form_after_department` | 1 |
| `ticket_form_after_custom_fields` | 1 |
| `ticket_form_after_attachments` | 1 |
| `ticket_created` | 1 |
| `task_timer_started` | 1 |
| `task_timer_deleted` | 1 |
| `task_follower_added` | 1 |
| `task_deleted` | 1 |
| `task_comment_updated` | 1 |
| `task_comment_deleted` | 1 |
| `task_comment_added` | 1 |
| `task_checklist_item_finished` | 1 |
| `task_checklist_item_created` | 1 |
| `task_assignee_added` | 1 |
| `schedule_status_changed` | 1 |
| `schedule_sent` | 1 |
| `schedule_send_to_customer_already_sent` | 1 |
| `schedule_declined` | 1 |
| `schedule_accepted` | 1 |
| `quotation_status_changed` | 1 |
| `quotation_sent` | 1 |
| `quotation_declined` | 1 |
| `quotation_created` | 1 |
| `quotation_converted_to_quotation` | 1 |
| `quotation_converted_to_invoice` | 1 |
| `quotation_accepted` | 1 |
| `public_ticket_start` | 1 |
| `public_ticket_end` | 1 |
| `proposal_sent` | 1 |
| `proposal_declined` | 1 |
| `proposal_created` | 1 |
| `proposal_converted_to_invoice` | 1 |
| `proposal_converted_to_estimate` | 1 |
| `proposal_accepted` | 1 |
| `project_copied` | 1 |
| `office_status_changed` | 1 |
| `office_sent` | 1 |
| `office_send_to_customer_already_sent` | 1 |
| `office_declined` | 1 |
| `office_accepted` | 1 |
| `note_updated` | 1 |
| `note_deleted` | 1 |
| `note_created` | 1 |
| `non_existent_user_login_attempt` | 1 |
| `new_template_added` | 1 |
| `new_tag_created` | 1 |
| `module_` | 1 |
| `licence_status_changed` | 1 |
| `licence_sent` | 1 |
| `licence_send_to_customer_already_sent` | 1 |
| `licence_remove_proposed_item` | 1 |
| `licence_released_already_sent` | 1 |
| `licence_declined` | 1 |
| `licence_accepted` | 1 |
| `lead_marked_as_lost` | 1 |
| `lead_marked_as_junk` | 1 |
| `lead_created_from_email_integration` | 1 |
| `lead_converted_to_customer` | 1 |
| `jobreport_status_changed` | 1 |
| `jobreport_sent` | 1 |
| `jobreport_send_to_customer_already_sent` | 1 |
| `jobreport_remove_proposed_item` | 1 |
| `jobreport_declined` | 1 |
| `jobreport_accepted` | 1 |
| `item_updated` | 1 |
| `item_deleted` | 1 |
| `item_created` | 1 |
| `item_coppied` | 1 |
| `invoice_unmarked_as_cancelled` | 1 |
| `invoice_status_changed` | 1 |
| `invoice_sent` | 1 |
| `invoice_overdue_reminder_sent` | 1 |
| `invoice_marked_as_cancelled` | 1 |
| `invoice_due_reminder_sent` | 1 |
| `invoice_copied` | 1 |
| `inspection_status_changed` | 1 |
| `inspection_sent` | 1 |
| `inspection_send_to_customer_already_sent` | 1 |
| `inspection_remove_inspection_item` | 1 |
| `inspection_declined` | 1 |
| `inspection_accepted` | 1 |
| `inactive_user_login_attempt` | 1 |
| `failed_login_attempt` | 1 |
| `expense_converted_to_invoice` | 1 |
| `existing_lead_email_inserted_from_email_integration` | 1 |
| `estimate_sent` | 1 |
| `estimate_requests_created` | 1 |
| `estimate_request_status_changed` | 1 |
| `estimate_request_form_submitted` | 1 |
| `estimate_request_assigned_changed` | 1 |
| `estimate_declined` | 1 |
| `estimate_converted_to_invoice` | 1 |
| `estimate_accepted` | 1 |
| `deprecated_hook_run` | 1 |
| `deprecated_function_run` | 1 |
| `customer_vault_entry_deleted` | 1 |
| `customer_updated_company_info` | 1 |
| `customer_subscribed_to_subscription` | 1 |
| `customer_group_deleted` | 1 |
| `credits_applied` | 1 |
| `credit_note_status_changed` | 1 |
| `credit_note_sent` | 1 |
| `credit_note_refund_updated` | 1 |
| `credit_note_refund_deleted` | 1 |
| `credit_note_refund_created` | 1 |
| `created_credit_note_from_invoice` | 1 |
| `contact_updated` | 1 |
| `contact_status_changed` | 1 |
| `contact_email_verified_but_requires_admin_confirmation` | 1 |
| `contact_email_verified` | 1 |
| `contact_deleted` | 1 |
| `client_status_changed` | 1 |
| `billing_status_changed` | 1 |
| `billing_sent` | 1 |
| `billing_declined` | 1 |
| `billing_created` | 1 |
| `billing_converted_to_invoice` | 1 |
| `billing_converted_to_billing` | 1 |
| `billing_accepted` | 1 |
| `before_update_note` | 1 |
| `before_unpin_post` | 1 |
| `before_ticket_deleted` | 1 |
| `before_template_deleted` | 1 |
| `before_schedule_deleted` | 1 |
| `before_pin_post` | 1 |
| `before_payment_deleted` | 1 |
| `before_office_deleted` | 1 |
| `before_make_backup` | 1 |
| `before_licence_deleted` | 1 |
| `before_leads_settings` | 1 |
| `before_leads_email_integration_form` | 1 |
| `before_lead_email_activity` | 1 |
| `before_lead_deleted` | 1 |
| `before_invoice_deleted` | 1 |
| `before_inspection_deleted` | 1 |
| `before_get_payment_gateways` | 1 |
| `before_expense_form_name` | 1 |
| `before_estimate_request_deleted` | 1 |
| `before_estimate_deleted` | 1 |
| `before_delete_ticket_reply` | 1 |
| `before_delete_post` | 1 |
| `before_delete_note` | 1 |
| `before_delete_department` | 1 |
| `before_delete_contact` | 1 |
| `before_delete_announcement` | 1 |
| `before_credit_note_deleted` | 1 |
| `before_contract_deleted` | 1 |
| `before_confirmation_identity_fields` | 1 |
| `before_compile_scripts_assets` | 1 |
| `before_client_deleted` | 1 |
| `before_check_recurring_tasks` | 1 |
| `before_change_maximum_number_of_digits_to_decimal_fields` | 1 |
| `before_change_decimal_places` | 1 |
| `app_client_assets_added` | 1 |
| `app_client_assets` | 1 |
| `app_admin_assets_added` | 1 |
| `app_admin_assets` | 1 |
| `announcement_updated` | 1 |
| `announcement_deleted` | 1 |
| `announcement_created` | 1 |
| `after_wheel_loader_added` | 1 |
| `after_vibro_added` | 1 |
| `after_update_project` | 1 |
| `after_update_credit_note` | 1 |
| `after_trucktor_added` | 1 |
| `after_towing_added` | 1 |
| `after_ticket_reply_added` | 1 |
| `after_template_updated` | 1 |
| `after_template_deleted` | 1 |
| `after_tanur_added` | 1 |
| `after_tangki_added` | 1 |
| `after_sterilizer_added` | 1 |
| `after_sky_lift_added` | 1 |
| `after_scissor_lift_added` | 1 |
| `after_schedule_updated` | 1 |
| `after_schedule_added` | 1 |
| `after_quotation_updated` | 1 |
| `after_proposal_updated` | 1 |
| `after_petir_added` | 1 |
| `after_pesawat_tenaga_added` | 1 |
| `after_overhead_crane_added` | 1 |
| `after_office_updated` | 1 |
| `after_office_added` | 1 |
| `after_motor_diesel_added` | 1 |
| `after_mobil_crane_added` | 1 |
| `after_misc_settings` | 1 |
| `after_mesin_produksi_added` | 1 |
| `after_mesin_press_added` | 1 |
| `after_mesin_bubut_added` | 1 |
| `after_lifting_frame_added` | 1 |
| `after_lift_barang_added` | 1 |
| `after_licence_updated` | 1 |
| `after_licence_item_added` | 1 |
| `after_licence_copied` | 1 |
| `after_licence_added` | 1 |
| `after_leads_settings` | 1 |
| `after_lead_email_activity` | 1 |
| `after_jib_crane_added` | 1 |
| `after_invoice_updated` | 1 |
| `after_invoice_added` | 1 |
| `after_inspection_updated` | 1 |
| `after_inspection_added` | 1 |
| `after_hydrant_added` | 1 |
| `after_hoist_crane_added` | 1 |
| `after_hanger_added` | 1 |
| `after_gantry_added` | 1 |
| `after_forklift_added` | 1 |
| `after_expense_updated` | 1 |
| `after_expense_added` | 1 |
| `after_excavator_added` | 1 |
| `after_estimate_updated` | 1 |
| `after_estimate_added` | 1 |
| `after_elevator_added` | 1 |
| `after_department_added` | 1 |
| `after_customer_billing_and_shipping_tab` | 1 |
| `after_customer_admins_tab` | 1 |
| `after_credit_note_deleted` | 1 |
| `after_create_credit_note` | 1 |
| `after_conveyor_added` | 1 |
| `after_contract_updated` | 1 |
| `after_contract_added` | 1 |
| `after_confirmation_identity_fields` | 1 |
| `after_compressor_added` | 1 |
| `after_client_updated` | 1 |
| `after_client_deleted` | 1 |
| `after_client_added` | 1 |
| `after_check_recurring_tasks` | 1 |
| `after_chain_hoist_added` | 1 |
| `after_bpv_added` | 1 |
| `after_boiler_added` | 1 |
| `after_billing_updated` | 1 |
| `after_bejana_uap_added` | 1 |
| `after_bejana_tekan_added` | 1 |
| `after_backhoe_loader_added` | 1 |
| `after_alarm_kebakaran_added` | 1 |
| `after_add_project` | 1 |
| `after_add_discussion_comment` | 1 |

## ## B. FRONTEND / VIEW — SKIP (190)

| Hook | Frekuensi |
|---|---|
| `load_pdf_language` | 10 |
| `inspection_html_viewed` | 3 |
| `after_licence_view_as_client_link` | 3 |
| `schedule_html_viewed` | 2 |
| `licence_html_viewed` | 2 |
| `forms_table_start` | 2 |
| `before_start_render_dashboard_content` | 2 |
| `before_calendar_filters` | 2 |
| `after_user_data_widget_tabs` | 2 |
| `after_user_data_widge_tabs_content` | 2 |
| `after_inspection_view_as_client_link` | 2 |
| `after_clients_area_init` | 2 |
| `after_calendar_filters` | 2 |
| `web_to_lead_form_start` | 1 |
| `web_to_lead_form_end` | 1 |
| `ticket_form_start` | 1 |
| `ticket_form_end` | 1 |
| `ticket_admin_single_page_loaded` | 1 |
| `tasks_filters_hidden_html` | 1 |
| `task_priorities_select` | 1 |
| `task_modal_rel_type_select` | 1 |
| `staff_render_permissions` | 1 |
| `staff_member_edit_view_profile` | 1 |
| `setup_menu_resetted` | 1 |
| `settings_group_end` | 1 |
| `quotation_html_viewed` | 1 |
| `proposal_html_viewed` | 1 |
| `pre_upload_module` | 1 |
| `pdf_header` | 1 |
| `pdf_footer` | 1 |
| `office_html_viewed` | 1 |
| `new_ticket_admin_page_loaded` | 1 |
| `lead_modal_profile_bottom` | 1 |
| `jobreport_html_viewed` | 1 |
| `invoice_html_viewed` | 1 |
| `estimate_request_form_start` | 1 |
| `estimate_request_form_end` | 1 |
| `estimate_html_viewed` | 1 |
| `elfinder_tinymce_head` | 1 |
| `customers_navigation_start` | 1 |
| `customers_navigation_end` | 1 |
| `customers_navigation_after_profile` | 1 |
| `customers_content_container_start` | 1 |
| `customers_area_knowledge_base_construct` | 1 |
| `customers_after_js_scripts_load` | 1 |
| `customers_after_body_start` | 1 |
| `credit_note_menu_links_start` | 1 |
| `contract_html_viewed` | 1 |
| `clients_login_form_start` | 1 |
| `clients_login_form_end` | 1 |
| `clients_authentication_constructor` | 1 |
| `client_area_after_project_overview` | 1 |
| `billing_html_viewed` | 1 |
| `before_update_setup_menu` | 1 |
| `before_update_aside_menu` | 1 |
| `before_tickets_email_templates` | 1 |
| `before_tasks_email_templates` | 1 |
| `before_task_description_section` | 1 |
| `before_system_info` | 1 |
| `before_subscriptions_table` | 1 |
| `before_subscriptions_email_templates` | 1 |
| `before_start_render_content` | 1 |
| `before_staff_myprofile` | 1 |
| `before_staff_email_templates` | 1 |
| `before_sms_gateways_settings` | 1 |
| `before_settings_group_view` | 1 |
| `before_save_theme_style` | 1 |
| `before_save_hidden_table_columns` | 1 |
| `before_save_dashboard_widgets_visibility` | 1 |
| `before_save_dashboard_widgets_order` | 1 |
| `before_save_completed_checklist_visibility` | 1 |
| `before_render_tickets_list_table` | 1 |
| `before_render_project_view` | 1 |
| `before_render_payment_gateway_settings` | 1 |
| `before_render_invoice_template` | 1 |
| `before_render_aside_menu` | 1 |
| `before_proposals_email_templates` | 1 |
| `before_projects_email_templates` | 1 |
| `before_output_preview_video` | 1 |
| `before_output_preview_image` | 1 |
| `before_notifications_email_templates` | 1 |
| `before_leads_kanban_card_icons` | 1 |
| `before_leads_email_templates` | 1 |
| `before_js_scripts_render` | 1 |
| `before_items_page_content` | 1 |
| `before_invoices_email_templates` | 1 |
| `before_insert_views_tracking` | 1 |
| `before_get_tabs` | 1 |
| `before_generate_short_link` | 1 |
| `before_gdpr_email_templates` | 1 |
| `before_expense_form_template_close` | 1 |
| `before_estimates_email_templates` | 1 |
| `before_estimate_request_email_templates` | 1 |
| `before_do_bulk_action_for_tickets` | 1 |
| `before_do_bulk_action_for_tasks` | 1 |
| `before_do_bulk_action_for_project_files` | 1 |
| `before_do_bulk_action_for_leads` | 1 |
| `before_do_bulk_action_for_items` | 1 |
| `before_do_bulk_action_for_expenses` | 1 |
| `before_do_bulk_action_for_customers` | 1 |
| `before_customers_email_templates` | 1 |
| `before_customers_area_sub_menu_start` | 1 |
| `before_customer_pdf_signature` | 1 |
| `before_credit_notes_email_templates` | 1 |
| `before_contracts_email_templates` | 1 |
| `before_compile_css_assets` | 1 |
| `before_client_profile_form_loaded` | 1 |
| `before_client_open_ticket_form_start` | 1 |
| `before_archive_short_link` | 1 |
| `before_admin_login_form_close` | 1 |
| `aside_menu_resetted` | 1 |
| `app_web_to_lead_form_head` | 1 |
| `app_web_to_lead_form_footer` | 1 |
| `app_ticket_form_head` | 1 |
| `app_ticket_form_footer` | 1 |
| `app_external_form_head` | 1 |
| `app_estimate_request_form_head` | 1 |
| `app_estimate_request_form_footer` | 1 |
| `app_customers_head` | 1 |
| `app_customers_footer` | 1 |
| `app_base_after_construct_action` | 1 |
| `app_admin_head` | 1 |
| `app_admin_footer` | 1 |
| `app_admin_authentication_head` | 1 |
| `after_telegrams_tabs_content` | 1 |
| `after_system_last_info_row` | 1 |
| `after_system_info_files_permissions` | 1 |
| `after_sms_trigger_textarea_content` | 1 |
| `after_single_knowledge_base_article_customers_area` | 1 |
| `after_settings_group_view` | 1 |
| `after_settings_e_sign_fields` | 1 |
| `after_scorecards_tabs_content` | 1 |
| `after_schedules_tabs_content` | 1 |
| `after_schedule_view_as_client_link` | 1 |
| `after_render_top_search` | 1 |
| `after_render_single_setup_menu` | 1 |
| `after_render_single_aside_menu` | 1 |
| `after_render_invoice_template` | 1 |
| `after_render_aside_menu` | 1 |
| `after_quotations_tabs_content` | 1 |
| `after_quotation_view_as_client_link` | 1 |
| `after_pusher_cluster_option` | 1 |
| `after_proposal_view_as_client_link` | 1 |
| `after_pdf_signature_settings_fields` | 1 |
| `after_pdf_document_formats` | 1 |
| `after_offices_tabs_content` | 1 |
| `after_office_view_as_client_link` | 1 |
| `after_load_client_language` | 1 |
| `after_load_admin_language` | 1 |
| `after_listrik_added` | 1 |
| `after_licences_tabs_content` | 1 |
| `after_leads_kanban_card_icons` | 1 |
| `after_lead_tabs_content` | 1 |
| `after_lead_lead_tabs` | 1 |
| `after_kb_groups_customers_area` | 1 |
| `after_js_scripts_render` | 1 |
| `after_jobreports_tabs_content` | 1 |
| `after_jobreport_view_as_client_link` | 1 |
| `after_invoice_view_as_client_link` | 1 |
| `after_invoice_preview_more_menu` | 1 |
| `after_inspections_tabs_content` | 1 |
| `after_finance_settings_tabs_content` | 1 |
| `after_finance_settings_last_tab` | 1 |
| `after_estimate_view_as_client_link` | 1 |
| `after_email_templates` | 1 |
| `after_dashboard_top_container` | 1 |
| `after_dashboard_half_container` | 1 |
| `after_dashboard` | 1 |
| `after_customers_area_sub_menu_end` | 1 |
| `after_customers_area_files_heading` | 1 |
| `after_customers_area_files_dropzone` | 1 |
| `after_customers_area_files` | 1 |
| `after_customer_pdf_signature` | 1 |
| `after_custom_profile_tab_content` | 1 |
| `after_custom_fields_select_options` | 1 |
| `after_cron_settings_last_tab_content` | 1 |
| `after_cron_settings_last_tab` | 1 |
| `after_contract_view_as_client_link` | 1 |
| `after_contact_modal_content_loaded` | 1 |
| `after_client_profile_password_form_loaded` | 1 |
| `after_client_profile_form_loaded` | 1 |
| `after_calendar_loaded` | 1 |
| `after_bulk_pdf_export_options` | 1 |
| `after_body_start` | 1 |
| `after_billings_tabs_content` | 1 |
| `after_billing_view_as_client_link` | 1 |
| `after_admin_login_form_start` | 1 |
| `admin_area_after_project_progress` | 1 |
| `add_single_ticket_tab_menu_item` | 1 |
| `add_single_ticket_tab_menu_content` | 1 |

## ## C. INFRA / bootstrap — NATIVE (22)

| Hook | Frekuensi |
|---|---|
| `schedule_converted_to_jobreport` | 1 |
| `pre_upgrade_database` | 1 |
| `pre_uninstall_module` | 1 |
| `pre_deactivate_module` | 1 |
| `pre_admin_init` | 1 |
| `pre_activate_module` | 1 |
| `model_init` | 1 |
| `inspection_converted_to_jobreport` | 1 |
| `database_updated` | 1 |
| `clients_init` | 1 |
| `before_update_database` | 1 |
| `before_perform_update` | 1 |
| `before_jobreport_deleted` | 1 |
| `before_admin_gdpr_settings` | 1 |
| `auto_upgrade_failed_to_extract_zip_file` | 1 |
| `app_init` | 1 |
| `after_jobreport_updated` | 1 |
| `after_jobreport_copy` | 1 |
| `after_jobreport_added` | 1 |
| `after_client_register_logged_in` | 1 |
| `after_client_register` | 1 |
| `admin_auth_init` | 1 |

## ## D. apply_filters() — Pipeline/Eloquent events (539)

| Hook | Frekuensi | AFTER | Status |
|---|---|---|---|
| `pdf_info_and_table_separator` | 23 | `Spine\Events\PdfCreating` (mutasi payload) | ✅ ported |
| `scorecards_table_additional_columns_sql` | 12 | — (frontend Next.js) | SKIP |
| `pdf_logo_url` | 12 | — (frontend Next.js) | SKIP |
| `pdf_format_array` | 10 | `Spine\Events\PdfCreating` (mutasi payload) | ✅ ported |
| `pdf_fonts_list` | 10 | — (frontend Next.js) | SKIP |
| `show_more_link_task_attachments` | 9 | — (frontend Next.js) | SKIP |
| `get_upload_path_by_type` | 9 | — (frontend Next.js) | SKIP |
| `items_table_class` | 7 | — (frontend Next.js) | SKIP |
| `item_description_td_width` | 7 | Pipeline / Eloquent model events | ⏳ |
| `inspection_html_pdf_data` | 7 | — (frontend Next.js) | SKIP |
| `billing_html_pdf_data` | 5 | — (frontend Next.js) | SKIP |
| `before_update_task` | 5 | Pipeline / Eloquent model events | ⏳ |
| `send_email_template_to` | 4 | `Mailable (native)` | ✅ native |
| `scorecard_html_pdf_data` | 4 | — (frontend Next.js) | SKIP |
| `schedule_html_pdf_data` | 4 | — (frontend Next.js) | SKIP |
| `item_tax_table_row` | 4 | — (frontend Next.js) | SKIP |
| `inspection_file_name_admin_area` | 4 | — (frontend Next.js) | SKIP |
| `format_inspection_number` | 4 | Pipeline / Eloquent model events | ⏳ |
| `email_template_language` | 4 | — (frontend Next.js) | SKIP |
| `before_parse_email_template_message` | 4 | Pipeline / Eloquent model events | ⏳ |
| `before_email_template_send` | 4 | Pipeline / Eloquent model events | ⏳ |
| `before_add_task` | 4 | Pipeline / Eloquent model events | ⏳ |
| `after_parse_email_template_message` | 4 | Pipeline / Eloquent model events | ⏳ |
| `use_deprecated_from_email_header_template_field` | 3 | — (frontend Next.js) | SKIP |
| `staff_can` | 3 | `Gate/permission (native)` | ✅ native |
| `quotations_table_columns` | 3 | — (frontend Next.js) | SKIP |
| `quotation_html_pdf_data` | 3 | — (frontend Next.js) | SKIP |
| `new_ticket_priority_selected` | 3 | — (frontend Next.js) | SKIP |
| `licence_html_pdf_data` | 3 | — (frontend Next.js) | SKIP |
| `licence_file_name_admin_area` | 3 | — (frontend Next.js) | SKIP |
| `jobreport_html_pdf_data` | 3 | — (frontend Next.js) | SKIP |
| `email_template_from_headers` | 3 | — (frontend Next.js) | SKIP |
| `before_set_inspection_statuses` | 3 | Pipeline / Eloquent model events | ⏳ |
| `to_sql_date_formatted` | 2 | `Spine\Events\DateFormatting` (mutasi payload) | ✅ ported |
| `ticket_message_without_html_for_non_admin` | 2 | Pipeline / Eloquent model events | ⏳ |
| `task_priorities_select` | 2 | — (frontend Next.js) | SKIP |
| `task_copy_statuses` | 2 | Pipeline / Eloquent model events | ⏳ |
| `scorecard_status_pdf_color` | 2 | — (frontend Next.js) | SKIP |
| `scorecard_status_label` | 2 | — (frontend Next.js) | SKIP |
| `scorecard_status_color_class` | 2 | — (frontend Next.js) | SKIP |
| `scorecard_number_format` | 2 | Pipeline / Eloquent model events | ⏳ |
| `schedule_file_name_admin_area` | 2 | — (frontend Next.js) | SKIP |
| `quotations_table_sql_columns` | 2 | — (frontend Next.js) | SKIP |
| `quotations_table_row_data` | 2 | — (frontend Next.js) | SKIP |
| `quotation_number_format` | 2 | Pipeline / Eloquent model events | ⏳ |
| `pusher_options` | 2 | — (frontend Next.js) | SKIP |
| `proposals_relation_table_columns` | 2 | — (frontend Next.js) | SKIP |
| `proposal_html_pdf_data` | 2 | `Spine\Events\PdfCreating` (mutasi payload) | ✅ ported |
| `projects_table_default_order` | 2 | — (frontend Next.js) | SKIP |
| `projects_activity_dashboard_limit` | 2 | — (frontend Next.js) | SKIP |
| `pdf_signature_break_lines` | 2 | `Spine\Events\PdfCreating` (mutasi payload) | ✅ ported |
| `old_filter_name` | 2 | — (frontend Next.js) | SKIP |
| `office_html_pdf_data` | 2 | — (frontend Next.js) | SKIP |
| `jobreports_table_additional_columns_sql` | 2 | — (frontend Next.js) | SKIP |
| `jobreport_file_name_admin_area` | 2 | — (frontend Next.js) | SKIP |
| `item_preview_rate` | 2 | — (frontend Next.js) | SKIP |
| `item_preview_amount_with_currency` | 2 | — (frontend Next.js) | SKIP |
| `invoice_html_pdf_data` | 2 | — (frontend Next.js) | SKIP |
| `get_task_durations` | 2 | Pipeline / Eloquent model events | ⏳ |
| `format_scorecard_number` | 2 | Pipeline / Eloquent model events | ⏳ |
| `format_licence_number` | 2 | Pipeline / Eloquent model events | ⏳ |
| `event_notifications` | 2 | — (frontend Next.js) | SKIP |
| `estimate_html_pdf_data` | 2 | — (frontend Next.js) | SKIP |
| `default_tickets_list_statuses` | 2 | — (frontend Next.js) | SKIP |
| `customers_area_download_schedule_filename` | 2 | — (frontend Next.js) | SKIP |
| `copy_task_default_status` | 2 | Pipeline / Eloquent model events | ⏳ |
| `contract_html_pdf_data` | 2 | — (frontend Next.js) | SKIP |
| `contact_email_unique` | 2 | Pipeline / Eloquent model events | ⏳ |
| `contact_email_required` | 2 | Pipeline / Eloquent model events | ⏳ |
| `calendar_data` | 2 | — (frontend Next.js) | SKIP |
| `billings_table_sql_columns` | 2 | — (frontend Next.js) | SKIP |
| `billings_table_row_data` | 2 | — (frontend Next.js) | SKIP |
| `billing_number_format` | 2 | Pipeline / Eloquent model events | ⏳ |
| `before_payment_recorded` | 2 | Pipeline / Eloquent model events | ⏳ |
| `before_number_format_render_languge_currencies` | 2 | — (frontend Next.js) | SKIP |
| `before_lead_added` | 2 | Pipeline / Eloquent model events | ⏳ |
| `before_get_task_statuses` | 2 | Pipeline / Eloquent model events | ⏳ |
| `before_get_project_statuses` | 2 | Pipeline / Eloquent model events | ⏳ |
| `before_fetch_events` | 2 | Pipeline / Eloquent model events | ⏳ |
| `before_dashboard_render` | 2 | — (frontend Next.js) | SKIP |
| `before_create_contact` | 2 | Pipeline / Eloquent model events | ⏳ |
| `add_task_attachment_as_comment` | 2 | Pipeline / Eloquent model events | ⏳ |
| `used_cron_features` | 1 | ServiceProvider/config (native) | NATIVE |
| `use_match_for_custom_fields_table_search` | 1 | — (frontend Next.js) | SKIP |
| `total_related_articles` | 1 | Pipeline / Eloquent model events | ⏳ |
| `total_recent_searches` | 1 | — (frontend Next.js) | SKIP |
| `total_pages_newsfeed` | 1 | — (frontend Next.js) | SKIP |
| `todos_limit` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_reply_status` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_replies_order` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_form_title` | 1 | — (frontend Next.js) | SKIP |
| `ticket_form_settings` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_form_file_location_settings` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_external_form_insert_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ticket_add_response_and_back_to_list_default` | 1 | — (frontend Next.js) | SKIP |
| `terms_and_condition_url` | 1 | Pipeline / Eloquent model events | ⏳ |
| `tasks_table_sql_where` | 1 | — (frontend Next.js) | SKIP |
| `tasks_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `tasks_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `tasks_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `tasks_related_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `tasks_related_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `tasks_related_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `tasks_priorities` | 1 | Pipeline / Eloquent model events | ⏳ |
| `task_status_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `task_single_mark_as_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `task_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `task_comments_order` | 1 | Pipeline / Eloquent model events | ⏳ |
| `tables_with_currency` | 1 | — (frontend Next.js) | SKIP |
| `table_params` | 1 | — (frontend Next.js) | SKIP |
| `system_info_files_permissions_issue` | 1 | Gate/permission (native) | ✅ native |
| `system_favourite_colors` | 1 | — (frontend Next.js) | SKIP |
| `survey_success_message` | 1 | Pipeline / Eloquent model events | ⏳ |
| `survey_default_redirect` | 1 | — (frontend Next.js) | SKIP |
| `suket_html_pdf_data` | 1 | — (frontend Next.js) | SKIP |
| `subscriptions_table_default_order` | 1 | — (frontend Next.js) | SKIP |
| `subscription_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `subscription_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `subscription_invoice_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `stripe_webhook_events` | 1 | ServiceProvider/config (native) | NATIVE |
| `statement` | 1 | Pipeline / Eloquent model events | ⏳ |
| `staff_table_sql_where` | 1 | — (frontend Next.js) | SKIP |
| `staff_table_row` | 1 | — (frontend Next.js) | SKIP |
| `staff_reminder_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `staff_profile_image_upload_allowed_extensions` | 1 | — (frontend Next.js) | SKIP |
| `staff_profile_image_thumb_width` | 1 | — (frontend Next.js) | SKIP |
| `staff_profile_image_thumb_height` | 1 | — (frontend Next.js) | SKIP |
| `staff_profile_image_small_width` | 1 | — (frontend Next.js) | SKIP |
| `staff_profile_image_small_height` | 1 | — (frontend Next.js) | SKIP |
| `staff_permissions_conditions` | 1 | Gate/permission (native) | ✅ native |
| `staff_permissions` | 1 | Gate/permission (native) | ✅ native |
| `staff_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `staff_email_templates` | 1 | — (frontend Next.js) | SKIP |
| `sms_triggers` | 1 | — (frontend Next.js) | SKIP |
| `sms_gateways` | 1 | Pipeline / Eloquent model events | ⏳ |
| `sms_gateway_available_triggers` | 1 | — (frontend Next.js) | SKIP |
| `show_ticket_submitter_on_clients_area_table` | 1 | — (frontend Next.js) | SKIP |
| `show_tax_per_item` | 1 | Pipeline / Eloquent model events | ⏳ |
| `show_setup_menu` | 1 | — (frontend Next.js) | SKIP |
| `show_more_link_task_attachments_customers_area` | 1 | — (frontend Next.js) | SKIP |
| `show_deprecated_from_email_header_template_field` | 1 | — (frontend Next.js) | SKIP |
| `show_custom_fields_edit_link_on_clients_area` | 1 | — (frontend Next.js) | SKIP |
| `should_staff_receive_task_notification` | 1 | — (frontend Next.js) | SKIP |
| `setup_menu_no_disable_items` | 1 | — (frontend Next.js) | SKIP |
| `settings_language_subtext` | 1 | — (frontend Next.js) | SKIP |
| `send_schedule_to_customer_file_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `send_recurring_system_expenses_email` | 1 | Pipeline / Eloquent model events | ⏳ |
| `send_recurring_invoices_system_email` | 1 | Pipeline / Eloquent model events | ⏳ |
| `send_office_to_customer_file_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `send_licence_to_customer_file_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `send_jobreport_to_customer_file_name` | 1 | ServiceProvider/config (native) | NATIVE |
| `send_inspection_to_customer_file_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `send_estimate_to_customer_file_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `sec2qty_formatted` | 1 | Pipeline / Eloquent model events | ⏳ |
| `schedules_table_additional_columns_sql` | 1 | — (frontend Next.js) | SKIP |
| `scheduled_email_default_date` | 1 | Pipeline / Eloquent model events | ⏳ |
| `schedule_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `schedule_status_label` | 1 | — (frontend Next.js) | SKIP |
| `schedule_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `schedule_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `sales_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `relation_values` | 1 | `Spine\Events\RelationResolving` (mutasi payload) | ✅ ported |
| `register_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `recurring_task_status` | 1 | Pipeline / Eloquent model events | ⏳ |
| `quotations_relation_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `quotation_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `quotation_info_text` | 1 | Pipeline / Eloquent model events | ⏳ |
| `quotation_customers_area_view_data` | 1 | — (frontend Next.js) | SKIP |
| `quotation_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `quotation_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `quick_actions_links` | 1 | — (frontend Next.js) | SKIP |
| `proposals_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `proposals_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `proposals_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `proposals_relation_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `proposal_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `proposal_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `proposal_info_text` | 1 | Pipeline / Eloquent model events | ⏳ |
| `proposal_customers_area_view_data` | 1 | — (frontend Next.js) | SKIP |
| `proposal_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `proposal_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `projects_timesheets_table_sql_join` | 1 | — (frontend Next.js) | SKIP |
| `projects_timesheets_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `projects_timesheets_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `projects_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `projects_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `projects_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `project_tasks_array_default_order` | 1 | Pipeline / Eloquent model events | ⏳ |
| `project_status_label` | 1 | — (frontend Next.js) | SKIP |
| `project_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `project_settings` | 1 | Pipeline / Eloquent model events | ⏳ |
| `project_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `project_get` | 1 | Pipeline / Eloquent model events | ⏳ |
| `project_filtered_visible_tabs` | 1 | — (frontend Next.js) | SKIP |
| `process_pdf_signature_on_close` | 1 | — (frontend Next.js) | SKIP |
| `privacy_policy_url` | 1 | Pipeline / Eloquent model events | ⏳ |
| `piped_ticket_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `pdf_customer_signature_image_path` | 1 | — (frontend Next.js) | SKIP |
| `paypal_logo_url` | 1 | — (frontend Next.js) | SKIP |
| `paypal_checkout_payer_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `paypal_checkout_order_create_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `paypal_checkout_button_style_params` | 1 | Pipeline / Eloquent model events | ⏳ |
| `payments_table_default_order` | 1 | — (frontend Next.js) | SKIP |
| `payment_gateway_scripts` | 1 | Pipeline / Eloquent model events | ⏳ |
| `payment_gateway_logo_width` | 1 | — (frontend Next.js) | SKIP |
| `payment_gateway_logo_url` | 1 | — (frontend Next.js) | SKIP |
| `payment_gateway_logo_height` | 1 | — (frontend Next.js) | SKIP |
| `payment_gateway_head` | 1 | — (frontend Next.js) | SKIP |
| `payment_gateway_footer` | 1 | — (frontend Next.js) | SKIP |
| `other_merge_fields_available_for` | 1 | Pipeline / Eloquent model events | ⏳ |
| `other_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `organization_info_text` | 1 | Pipeline / Eloquent model events | ⏳ |
| `offices_table_additional_columns_sql` | 1 | — (frontend Next.js) | SKIP |
| `office_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `office_status_label` | 1 | — (frontend Next.js) | SKIP |
| `office_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `office_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `office_info_text` | 1 | Pipeline / Eloquent model events | ⏳ |
| `office_info_format_company_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `office_file_name_admin_area` | 1 | — (frontend Next.js) | SKIP |
| `numbers_of_features_using_cron_job` | 1 | ServiceProvider/config (native) | NATIVE |
| `number_after_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `null_columns_sort_as_last` | 1 | — (frontend Next.js) | SKIP |
| `notifications_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `notifications_limit` | 1 | Pipeline / Eloquent model events | ⏳ |
| `notification_data` | 1 | `Spine\Events\NotificationCreating` (mutasi payload) | ✅ ported |
| `not_importable_leads_fields` | 1 | — (frontend Next.js) | SKIP |
| `not_importable_clients_fields` | 1 | — (frontend Next.js) | SKIP |
| `new_contract_default_content` | 1 | — (frontend Next.js) | SKIP |
| `nav_user_menu_items` | 1 | — (frontend Next.js) | SKIP |
| `msg91_common_options` | 1 | — (frontend Next.js) | SKIP |
| `money_after_format_with_currency` | 1 | Pipeline / Eloquent model events | ⏳ |
| `migration_tables_to_replace_old_links` | 1 | — (frontend Next.js) | SKIP |
| `merge_field_logo_img_width` | 1 | — (frontend Next.js) | SKIP |
| `markdown_extensions` | 1 | Pipeline / Eloquent model events | ⏳ |
| `mark_down_safe_mode` | 1 | Pipeline / Eloquent model events | ⏳ |
| `logo_href` | 1 | Pipeline / Eloquent model events | ⏳ |
| `licences_table_additional_columns_sql` | 1 | — (frontend Next.js) | SKIP |
| `licence_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `licence_status_label` | 1 | — (frontend Next.js) | SKIP |
| `licence_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `licence_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `leads_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `leads_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `leads_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `leads_table_additional_columns_sql` | 1 | — (frontend Next.js) | SKIP |
| `leads_email_integration_lead_check` | 1 | Pipeline / Eloquent model events | ⏳ |
| `leads_email_integration_email_body_for_database` | 1 | — (frontend Next.js) | SKIP |
| `leads_email_integration_check_every` | 1 | Pipeline / Eloquent model events | ⏳ |
| `lead_view_data` | 1 | — (frontend Next.js) | SKIP |
| `lead_tab_badge_count` | 1 | — (frontend Next.js) | SKIP |
| `lead_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `lead_form_available_database_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `lead_email_activity_subject` | 1 | ServiceProvider/config (native) | NATIVE |
| `lead_available_dupicate_validation_fields_option` | 1 | — (frontend Next.js) | SKIP |
| `lead_activity_log_default_sort` | 1 | — (frontend Next.js) | SKIP |
| `jobreport_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `jobreport_status_label` | 1 | — (frontend Next.js) | SKIP |
| `jobreport_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `jobreport_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `items_table_amounts_exclude_currency_symbol` | 1 | — (frontend Next.js) | SKIP |
| `items_custom_fields_for_table_sql` | 1 | — (frontend Next.js) | SKIP |
| `iso_logo_upload_allowed_extensions` | 1 | — (frontend Next.js) | SKIP |
| `is_client_using_multiple_currencies` | 1 | Pipeline / Eloquent model events | ⏳ |
| `is_client_id_used` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoices_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `invoices_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `invoices_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `invoices_statuses_available_for_credits` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoices_ids_available_for_merging` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoice_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `invoice_pdf_header_before_custom_fields` | 1 | — (frontend Next.js) | SKIP |
| `invoice_pdf_header_after_sale_agent` | 1 | — (frontend Next.js) | SKIP |
| `invoice_pdf_header_after_project_name` | 1 | — (frontend Next.js) | SKIP |
| `invoice_pdf_header_after_due_date` | 1 | — (frontend Next.js) | SKIP |
| `invoice_pdf_header_after_date` | 1 | — (frontend Next.js) | SKIP |
| `invoice_pdf_header_after_custom_fields` | 1 | — (frontend Next.js) | SKIP |
| `invoice_overdue_notice_attach_pdf` | 1 | `Spine\Events\PdfCreating` (mutasi payload) | ✅ ported |
| `invoice_object_before_send_to_client` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoice_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoice_due_notice_attach_pdf` | 1 | `Spine\Events\PdfCreating` (mutasi payload) | ✅ ported |
| `invoice_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoice_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `invoice_batch_payments_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `inspections_table_additional_columns_sql` | 1 | — (frontend Next.js) | SKIP |
| `inspection_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `inspection_status_label` | 1 | — (frontend Next.js) | SKIP |
| `inspection_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `inspection_number_format` | 1 | Pipeline / Eloquent model events | ⏳ |
| `init_relation_options` | 1 | — (frontend Next.js) | SKIP |
| `info_format_custom_field` | 1 | Pipeline / Eloquent model events | ⏳ |
| `imap_fetch_from_email_by_reply_to_header` | 1 | — (frontend Next.js) | SKIP |
| `imap_auto_import_ticket_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `html_purify_safe_iframe_regexp` | 1 | Pipeline / Eloquent model events | ⏳ |
| `html_purify_content` | 1 | — (frontend Next.js) | SKIP |
| `html_purifier_config` | 1 | Pipeline / Eloquent model events | ⏳ |
| `html5_video_extensions` | 1 | Pipeline / Eloquent model events | ⏳ |
| `help_menu_item_text` | 1 | — (frontend Next.js) | SKIP |
| `help_menu_item_link` | 1 | — (frontend Next.js) | SKIP |
| `global_search_result_query` | 1 | — (frontend Next.js) | SKIP |
| `global_search_result_output` | 1 | — (frontend Next.js) | SKIP |
| `get_task` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_styling_areas` | 1 | — (frontend Next.js) | SKIP |
| `get_sms_gateways` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_relation_data` | 1 | `Spine\Events\RelationResolving` (mutasi payload) | ✅ ported |
| `get_projects_tasks` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_option` | 1 | — (frontend Next.js) | SKIP |
| `get_notes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_media_folder` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_invoice` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_goal_types` | 1 | Pipeline / Eloquent model events | ⏳ |
| `get_dashboard_widgets` | 1 | — (frontend Next.js) | SKIP |
| `get_current_date_format` | 1 | `Spine\Events\DateFormatting` (mutasi payload) | ✅ ported |
| `get_contact_permissions` | 1 | Gate/permission (native) | ✅ native |
| `format_schedule_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `format_quotation_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `format_office_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `format_jobreport_number` | 1 | ServiceProvider/config (native) | NATIVE |
| `format_invoice_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `format_estimate_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `format_credit_note_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `format_billing_number` | 1 | Pipeline / Eloquent model events | ⏳ |
| `forbidden_ticket_statuses_to_change_in_clients_area` | 1 | — (frontend Next.js) | SKIP |
| `expenses_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `expenses_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `expenses_table_default_order` | 1 | — (frontend Next.js) | SKIP |
| `expenses_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `expense_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `expense_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `event_update_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `event_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `event_create_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `estimates_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `estimates_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `estimates_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `estimate_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `estimate_status_label` | 1 | — (frontend Next.js) | SKIP |
| `estimate_status_color_class` | 1 | — (frontend Next.js) | SKIP |
| `estimate_request_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `estimate_request_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `estimate_request_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `estimate_request_table_additional_columns_sql` | 1 | — (frontend Next.js) | SKIP |
| `estimate_request_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `estimate_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `estimate_file_name_admin_area` | 1 | — (frontend Next.js) | SKIP |
| `estimate_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `estimate_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `email_template_parsed` | 1 | `Spine\Events\MailSending` (mutasi payload) | ✅ ported |
| `download_file_path` | 1 | Pipeline / Eloquent model events | ⏳ |
| `disable_navigation_on_public_ticket_view` | 1 | — (frontend Next.js) | SKIP |
| `deprecated_hook_trigger_error` | 1 | — (frontend Next.js) | SKIP |
| `deprecated_function_trigger_error` | 1 | — (frontend Next.js) | SKIP |
| `delete_two_checkout_log_older_than_days` | 1 | ServiceProvider/config (native) | NATIVE |
| `delete_old_temporary_files_older_than` | 1 | Pipeline / Eloquent model events | ⏳ |
| `default_lead_status_color` | 1 | — (frontend Next.js) | SKIP |
| `default_estimate_request_status_color` | 1 | — (frontend Next.js) | SKIP |
| `datatables_sql_query_results` | 1 | — (frontend Next.js) | SKIP |
| `datatables_query_order_column` | 1 | — (frontend Next.js) | SKIP |
| `datatables_language_array` | 1 | — (frontend Next.js) | SKIP |
| `customers_theme_assets_url` | 1 | — (frontend Next.js) | SKIP |
| `customers_theme_assets_path` | 1 | — (frontend Next.js) | SKIP |
| `customers_table_sql_join` | 1 | — (frontend Next.js) | SKIP |
| `customers_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `customers_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `customers_table_default_order` | 1 | — (frontend Next.js) | SKIP |
| `customers_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `customers_profile_tab_badge` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_list_default_ticket_statuses` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_files_where` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_estimate_request_link` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_download_office_filename` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_download_licence_filename` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_download_jobreport_filename` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_download_estimate_filename` | 1 | — (frontend Next.js) | SKIP |
| `customers_area_autoloaded_vars` | 1 | — (frontend Next.js) | SKIP |
| `customer_update_company_info` | 1 | Pipeline / Eloquent model events | ⏳ |
| `customer_profile_tab_custom_fields_text` | 1 | — (frontend Next.js) | SKIP |
| `customer_info_text` | 1 | Pipeline / Eloquent model events | ⏳ |
| `customer_info_format_company_name` | 1 | Pipeline / Eloquent model events | ⏳ |
| `customer_have_transactions` | 1 | Pipeline / Eloquent model events | ⏳ |
| `customer_has_subscriptions` | 1 | Pipeline / Eloquent model events | ⏳ |
| `custom_fields_where_items_table_add_edit_preview` | 1 | — (frontend Next.js) | SKIP |
| `csrf_exclude_uris` | 1 | Pipeline / Eloquent model events | ⏳ |
| `cron_retry_email_queue_seconds` | 1 | ServiceProvider/config (native) | NATIVE |
| `cron_functions_execute_seconds` | 1 | Pipeline / Eloquent model events | ⏳ |
| `credit_note_pdf_header_before_custom_fields` | 1 | — (frontend Next.js) | SKIP |
| `credit_note_pdf_header_after_shipping_info` | 1 | — (frontend Next.js) | SKIP |
| `credit_note_pdf_header_after_reference_no` | 1 | — (frontend Next.js) | SKIP |
| `credit_note_pdf_header_after_project` | 1 | — (frontend Next.js) | SKIP |
| `credit_note_pdf_header_after_date` | 1 | — (frontend Next.js) | SKIP |
| `credit_note_pdf_header_after_custom_fields` | 1 | — (frontend Next.js) | SKIP |
| `credit_note_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `credit_note_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `credit_note_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `create_note_data` | 1 | Pipeline / Eloquent model events | ⏳ |
| `cpanel_tickets_forwarder_path` | 1 | Pipeline / Eloquent model events | ⏳ |
| `contracts_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `contracts_table_row_data` | 1 | — (frontend Next.js) | SKIP |
| `contracts_table_default_order` | 1 | — (frontend Next.js) | SKIP |
| `contracts_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `contract_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `contract_customers_area_view_data` | 1 | — (frontend Next.js) | SKIP |
| `contact_profile_image_upload_allowed_extensions` | 1 | — (frontend Next.js) | SKIP |
| `contact_profile_image_thumb_width` | 1 | — (frontend Next.js) | SKIP |
| `contact_profile_image_thumb_height` | 1 | — (frontend Next.js) | SKIP |
| `contact_profile_image_small_width` | 1 | — (frontend Next.js) | SKIP |
| `contact_profile_image_small_height` | 1 | — (frontend Next.js) | SKIP |
| `contact_columns` | 1 | — (frontend Next.js) | SKIP |
| `consent_public_page_heading` | 1 | — (frontend Next.js) | SKIP |
| `company_logo_upload_allowed_extensions` | 1 | — (frontend Next.js) | SKIP |
| `company_logo` | 1 | — (frontend Next.js) | SKIP |
| `clients_area_tickets_summary` | 1 | — (frontend Next.js) | SKIP |
| `client_statement_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `client_project_total_tasks` | 1 | Pipeline / Eloquent model events | ⏳ |
| `client_project_tasks_not_completed` | 1 | Pipeline / Eloquent model events | ⏳ |
| `client_project_tasks_completed` | 1 | Pipeline / Eloquent model events | ⏳ |
| `client_filtered_visible_tabs` | 1 | — (frontend Next.js) | SKIP |
| `client_email_templates` | 1 | — (frontend Next.js) | SKIP |
| `client_contact_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `check_vault_entries_visibility` | 1 | Pipeline / Eloquent model events | ⏳ |
| `change_contact_status` | 1 | Pipeline / Eloquent model events | ⏳ |
| `certificate_html_pdf_data` | 1 | — (frontend Next.js) | SKIP |
| `calculate_goal_achievement_sql` | 1 | Pipeline / Eloquent model events | ⏳ |
| `bulk_pdf_export_class` | 1 | — (frontend Next.js) | SKIP |
| `bulk_pdf_export_available_features` | 1 | — (frontend Next.js) | SKIP |
| `blank_signature_line` | 1 | — (frontend Next.js) | SKIP |
| `billings_table_columns` | 1 | — (frontend Next.js) | SKIP |
| `billings_relation_table_sql_columns` | 1 | — (frontend Next.js) | SKIP |
| `billing_status_pdf_color` | 1 | — (frontend Next.js) | SKIP |
| `billing_info_text` | 1 | Pipeline / Eloquent model events | ⏳ |
| `billing_file_name_admin_area` | 1 | — (frontend Next.js) | SKIP |
| `billing_customers_area_view_data` | 1 | — (frontend Next.js) | SKIP |
| `billing_currency_disabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `billing_currency_attributes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_update_staff_member` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_update_project` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_update_item` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_update_credit_note` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_update_contact` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_ticket_settings_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_ticket_reply_add` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_ticket_created` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_template_deleted` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_template_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_task_timer_stopped` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_staff_update_profile` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_staff_status_change` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_staff_change_password` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_sql_date_format` | 1 | `Spine\Events\DateFormatting` (mutasi payload) | ✅ ported |
| `before_single_setting_updated_in_loop` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_settings_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_telegram_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_schedule_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_quotation_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_proposal_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_office_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_media_folder` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_licence_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_jobreport_statuses` | 1 | ServiceProvider/config (native) | NATIVE |
| `before_set_estimate_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_set_billing_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_send_simple_email` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_schedule_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_schedule_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_return_table_items_html_and_taxes` | 1 | — (frontend Next.js) | SKIP |
| `before_return_num_word` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_quotation_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_proposal_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_process_gateway_func` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_payment_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_office_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_office_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_log_project_activity` | 1 | ServiceProvider/config (native) | NATIVE |
| `before_licence_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_licence_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_jobreport_updated` | 1 | ServiceProvider/config (native) | NATIVE |
| `before_jobreport_added` | 1 | ServiceProvider/config (native) | NATIVE |
| `before_invoice_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_invoice_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_inspection_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_inspection_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_insert_lead_from_email_integration` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_init_media` | 1 | ServiceProvider/config (native) | NATIVE |
| `before_get_task_timer_round_off_times` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_get_task_timer_round_off_options` | 1 | — (frontend Next.js) | SKIP |
| `before_get_locales` | 1 | — (frontend Next.js) | SKIP |
| `before_get_locale` | 1 | — (frontend Next.js) | SKIP |
| `before_get_languages` | 1 | — (frontend Next.js) | SKIP |
| `before_get_language_text` | 1 | — (frontend Next.js) | SKIP |
| `before_get_credit_notes_statuses` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_expense_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_expense_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_estimate_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_estimate_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_department_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_department_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_create_quotation` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_create_proposal` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_create_credit_note` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_create_billing` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_contract_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_contract_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_client_view_invoice` | 1 | — (frontend Next.js) | SKIP |
| `before_client_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_client_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_billing_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_announcement_updated` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_announcement_added` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_admin_view_invoice_pdf` | 1 | — (frontend Next.js) | SKIP |
| `before_add_project_discussion_comment` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_add_project` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_add_payment_gateways` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_add_online_payment_modes` | 1 | Pipeline / Eloquent model events | ⏳ |
| `before_add_kb_article` | 1 | Pipeline / Eloquent model events | ⏳ |
| `available_tracking_templates` | 1 | Pipeline / Eloquent model events | ⏳ |
| `available_merge_fields` | 1 | Pipeline / Eloquent model events | ⏳ |
| `available_date_formats` | 1 | `Spine\Events\DateFormatting` (mutasi payload) | ✅ ported |
| `automatic_calling_codes_enabled` | 1 | Pipeline / Eloquent model events | ⏳ |
| `app_view_data` | 1 | — (frontend Next.js) | SKIP |
| `app_payment_gateways` | 1 | Pipeline / Eloquent model events | ⏳ |
| `app_happy_text_regex` | 1 | Pipeline / Eloquent model events | ⏳ |
| `app_happy_text_color` | 1 | — (frontend Next.js) | SKIP |
| `app_format_money` | 1 | Pipeline / Eloquent model events | ⏳ |
| `app_decimal_places` | 1 | Pipeline / Eloquent model events | ⏳ |
| `all_countries` | 1 | Pipeline / Eloquent model events | ⏳ |
| `all_contacts_table_row` | 1 | — (frontend Next.js) | SKIP |
| `all_client_attachments` | 1 | Pipeline / Eloquent model events | ⏳ |
| `alert_class` | 1 | Pipeline / Eloquent model events | ⏳ |
| `ajax_on_total_items` | 1 | Pipeline / Eloquent model events | ⏳ |
| `after_invoice_sent_template_statement` | 1 | Pipeline / Eloquent model events | ⏳ |
| `after_get_language_text` | 1 | — (frontend Next.js) | SKIP |
| `after_format_datetime` | 1 | `Spine\Events\DateFormatting` (mutasi payload) | ✅ ported |
| `after_format_date` | 1 | `Spine\Events\DateFormatting` (mutasi payload) | ✅ ported |
| `admin_total_project_tasks_where` | 1 | Pipeline / Eloquent model events | ⏳ |
| `admin_project_progress_color` | 1 | — (frontend Next.js) | SKIP |
| `admin_body_class` | 1 | — (frontend Next.js) | SKIP |
| `admin_area_auto_loaded_vars` | 1 | — (frontend Next.js) | SKIP |
| `acceptance_info_array` | 1 | Pipeline / Eloquent model events | ⏳ |

