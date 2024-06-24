from . import __version__ as app_version

app_name = "supplier_name_reference_version13"
app_title = "Supplier Name Reference Version13"
app_publisher = "Abdul Basit"
app_description = "supplier_reference_version13"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "basit@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/supplier_name_reference_version13/css/supplier_name_reference_version13.css"
# app_include_js = "/assets/supplier_name_reference_version13/js/supplier_name_reference_version13.js"

# include js, css files in header of web template
# web_include_css = "/assets/supplier_name_reference_version13/css/supplier_name_reference_version13.css"
# web_include_js = "/assets/supplier_name_reference_version13/js/supplier_name_reference_version13.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "supplier_name_reference_version13/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Payment Entry" : "public/js/payment_entry.js"
    }


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "supplier_name_reference_version13.install.before_install"
# after_install = "supplier_name_reference_version13.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "supplier_name_reference_version13.uninstall.before_uninstall"
# after_uninstall = "supplier_name_reference_version13.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "supplier_name_reference_version13.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "Purchase Receipt": "supplier_name_reference_version13.overrides.purchase_receipt.CustomPurchaseReceipt"
	# "ToDo": "custom_app.overrides.CustomToDo"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"supplier_name_reference_version13.tasks.all"
#	],
#	"daily": [
#		"supplier_name_reference_version13.tasks.daily"
#	],
#	"hourly": [
#		"supplier_name_reference_version13.tasks.hourly"
#	],
#	"weekly": [
#		"supplier_name_reference_version13.tasks.weekly"
#	]
#	"monthly": [
#		"supplier_name_reference_version13.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "supplier_name_reference_version13.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "supplier_name_reference_version13.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "supplier_name_reference_version13.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["supplier_name_reference_version13.utils.before_request"]
# after_request = ["supplier_name_reference_version13.utils.after_request"]

# Job Events
# ----------
# before_job = ["supplier_name_reference_version13.utils.before_job"]
# after_job = ["supplier_name_reference_version13.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"supplier_name_reference_version13.auth.validate"
# ]

