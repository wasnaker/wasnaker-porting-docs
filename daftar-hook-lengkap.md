# Daftar Lengkap Hook — app.ciptamasjaya.co.id

*Ground truth: grep `do_action()` di `application/` + `modules/` aplikasi legacy (total **528 hook unik**), 30 Agu 2026. Status port: `✅` sudah, `⏳` ditunda, `SKIP` tidak relevan API-only, `NATIVE` pakai bawaan Laravel.*

## A. BACKEND — wajib ada di backend

### A.1 Sudah di-port ke Spine — event class + dispatch nyata (5) ✅
| Hook | Frekuensi | Event Spine |
|---|---|---|
| `sms_trigger_triggered` | 1 | `Spine\Events\SmsSent` |
| `module_uninstalled` | 1 | `Spine\Events\ModuleUninstalled` |
| `module_installed` | 1 | `Spine\Events\ModuleInstalled` |
| `module_deactivated` | 1 | `Spine\Events\ModuleDeactivated` |
| `module_activated` | 1 | `Spine\Events\ModuleActivated` |
*Catatan: `SettingUpdated` (dispatched di `SettingService::set()`) menutup keluarga hook settings-save; `before_update_backup_options` masuk ke sini saat dipicu.*

### A.2 Dipetakan ke native Laravel — tanpa kode baru (19) ✅
| Hook | Frekuensi | Target native |
|---|---|---|
| `email_template_sent` | 4 | Illuminate\Mail\Events\MessageSent |
| `failed_to_send_email_template` | 3 | Illuminate\Mail\Events\MessageSending |
| `after_staff_login` | 3 | Illuminate\Auth\Events\Login |
| `before_user_reset_password` | 2 | PasswordReset |
| `before_staff_login` | 2 | Illuminate\Auth\Events\Login |
| `after_user_reset_password` | 2 | PasswordReset |
| `after_contact_login` | 2 | Illuminate\Auth\Events\Login |
| `smtp_test_email_success` | 1 | Mail test flow |
| `smtp_test_email_failed` | 1 | Mail test flow |
| `set_password_email_sent` | 1 | PasswordReset |
| `modules_loaded` | 1 | ServiceProvider::boot() |
| `forgot_password_email_sent` | 1 | PasswordReset |
| `before_staff_logout` | 1 | Illuminate\Auth\Events\Logout |
| `before_send_test_smtp_email` | 1 | Mail test flow |
| `before_contact_logout` | 1 | Illuminate\Auth\Events\Logout |
| `before_client_login` | 1 | Illuminate\Auth\Events\Login |
| `after_user_logout` | 1 | Illuminate\Auth\Events\Logout |
| `after_client_logout` | 1 | Illuminate\Auth\Events\Logout |
| `admin_init` | 1 | ServiceProvider::boot() |

### A.3 Deferred di Spine — nyusul saat fitur dibangun (31) ⏳
| Hook | Frekuensi | Catatan |
|---|---|---|
| `before_remove_iso_logo` | 2 | CRUD staff app konsumen |
| `before_remove_contact_profile_image` | 2 | CRUD staff app konsumen |
| `before_cron_run` | 2 | CRUD staff app konsumen |
| `staff_profile_access` | 1 | CRUD staff app konsumen |
| `staff_member_updated` | 1 | CRUD staff app konsumen |
| `staff_member_profile_updated` | 1 | CRUD staff app konsumen |
| `staff_member_deleted` | 1 | CRUD staff app konsumen |
| `staff_member_created` | 1 | CRUD staff app konsumen |
| `edit_logged_in_staff_profile` | 1 | CRUD staff app konsumen |
| `before_upload_ticket_attachment` | 1 | validasi FileService |
| `before_upload_staff_profile_image` | 1 | validasi FileService |
| `before_upload_signature_image_attachment` | 1 | validasi FileService |
| `before_upload_project_discussion_comment_attachment` | 1 | validasi FileService |
| `before_upload_project_attachment` | 1 | validasi FileService |
| `before_upload_newsfeed_attachment` | 1 | validasi FileService |
| `before_upload_iso_logo_attachment` | 1 | validasi FileService |
| `before_upload_favicon_attachment` | 1 | validasi FileService |
| `before_upload_expense_attachment` | 1 | validasi FileService |
| `before_upload_estimate_request_attachment` | 1 | validasi FileService |
| `before_upload_contract_attachment` | 1 | validasi FileService |
| `before_upload_contact_profile_image` | 1 | validasi FileService |
| `before_upload_company_logo_attachment` | 1 | validasi FileService |
| `before_upload_client_attachment` | 1 | validasi FileService |
| `before_update_backup_options` | 1 | → SettingUpdated saat settings-save |
| `before_staff_change_language` | 1 | CRUD staff app konsumen |
| `before_remove_staff_profile_image` | 1 | CRUD staff app konsumen |
| `before_remove_project_file` | 1 | CRUD staff app konsumen |
| `before_remove_favicon` | 1 | CRUD staff app konsumen |
| `before_remove_company_logo` | 1 | CRUD staff app konsumen |
| `before_delete_staff_member` | 1 | CRUD staff app konsumen |
| `after_cron_run` | 1 | CRUD staff app konsumen |

### A.4 Domain → modul bisnis (273) ⏳
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
| `settings_group_end` | 1 |
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
| `pdf_close` | 1 |
| `office_status_changed` | 1 |
| `office_sent` | 1 |
| `office_send_to_customer_already_sent` | 1 |
| `office_declined` | 1 |
| `office_accepted` | 1 |
| `notification_created` | 1 |
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
| `client_area_after_project_overview` | 1 |
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
| `before_start_render_content` | 1 |
| `before_schedule_deleted` | 1 |
| `before_save_completed_checklist_visibility` | 1 |
| `before_render_payment_gateway_settings` | 1 |
| `before_render_invoice_template` | 1 |
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
| `before_expense_form_template_close` | 1 |
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
| `after_single_knowledge_base_article_customers_area` | 1 |
| `after_scissor_lift_added` | 1 |
| `after_schedule_updated` | 1 |
| `after_schedule_added` | 1 |
| `after_render_invoice_template` | 1 |
| `after_quotation_updated` | 1 |
| `after_pusher_cluster_option` | 1 |
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
| `after_kb_groups_customers_area` | 1 |
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
| `after_customers_area_files` | 1 |
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
| `admin_area_after_project_progress` | 1 |
*Event dibuat di `modules/<N>/Providers/EventServiceProvider.php` saat modul di-port — JANGAN masuk package Spine (hard rule).*

## B. FRONTEND / VIEW — SKIP untuk API-only (174)
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
| `customers_after_js_scripts_load` | 1 |
| `customers_after_body_start` | 1 |
| `credit_note_menu_links_start` | 1 |
| `contract_html_viewed` | 1 |
| `clients_login_form_start` | 1 |
| `clients_login_form_end` | 1 |
| `clients_authentication_constructor` | 1 |
| `billing_html_viewed` | 1 |
| `before_update_setup_menu` | 1 |
| `before_update_aside_menu` | 1 |
| `before_tickets_email_templates` | 1 |
| `before_tasks_email_templates` | 1 |
| `before_task_description_section` | 1 |
| `before_system_info` | 1 |
| `before_subscriptions_table` | 1 |
| `before_subscriptions_email_templates` | 1 |
| `before_staff_myprofile` | 1 |
| `before_staff_email_templates` | 1 |
| `before_sms_gateways_settings` | 1 |
| `before_settings_group_view` | 1 |
| `before_save_theme_style` | 1 |
| `before_save_hidden_table_columns` | 1 |
| `before_save_dashboard_widgets_visibility` | 1 |
| `before_save_dashboard_widgets_order` | 1 |
| `before_render_tickets_list_table` | 1 |
| `before_render_project_view` | 1 |
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
| `app_admin_head` | 1 |
| `app_admin_footer` | 1 |
| `app_admin_authentication_head` | 1 |
| `after_telegrams_tabs_content` | 1 |
| `after_system_last_info_row` | 1 |
| `after_system_info_files_permissions` | 1 |
| `after_sms_trigger_textarea_content` | 1 |
| `after_settings_group_view` | 1 |
| `after_settings_e_sign_fields` | 1 |
| `after_scorecards_tabs_content` | 1 |
| `after_schedules_tabs_content` | 1 |
| `after_schedule_view_as_client_link` | 1 |
| `after_render_top_search` | 1 |
| `after_render_single_setup_menu` | 1 |
| `after_render_single_aside_menu` | 1 |
| `after_render_aside_menu` | 1 |
| `after_quotations_tabs_content` | 1 |
| `after_quotation_view_as_client_link` | 1 |
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
| `add_single_ticket_tab_menu_item` | 1 |
| `add_single_ticket_tab_menu_content` | 1 |
*Kategori: html_viewed, tabs, menu, widget, forms, settings views, upload-anchored view hooks — frontend (Next.js) yang menangani, bukan backend.*

## C. INFRA / bootstrap — NATIVE (26)
| Hook | Frekuensi |
|---|---|
| `after_clients_area_init` | 2 |
| `schedule_converted_to_jobreport` | 1 |
| `pre_upgrade_database` | 1 |
| `pre_uninstall_module` | 1 |
| `pre_deactivate_module` | 1 |
| `pre_admin_init` | 1 |
| `pre_activate_module` | 1 |
| `pdf_construct` | 1 |
| `model_init` | 1 |
| `inspection_converted_to_jobreport` | 1 |
| `database_updated` | 1 |
| `customers_area_knowledge_base_construct` | 1 |
| `clients_init` | 1 |
| `before_update_database` | 1 |
| `before_perform_update` | 1 |
| `before_jobreport_deleted` | 1 |
| `before_admin_gdpr_settings` | 1 |
| `auto_upgrade_failed_to_extract_zip_file` | 1 |
| `app_init` | 1 |
| `app_base_after_construct_action` | 1 |
| `after_jobreport_updated` | 1 |
| `after_jobreport_copy` | 1 |
| `after_jobreport_added` | 1 |
| `after_client_register_logged_in` | 1 |
| `after_client_register` | 1 |
| `admin_auth_init` | 1 |
*Digantikan ServiceProvider + Middleware + Composer autoload (keputusan `analisis-hook-perfex.md` Bagian A).*
