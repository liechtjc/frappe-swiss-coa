app_name = "swiss_coa"
app_title = "Swiss COA"
app_publisher = "Jean-Christophe Liechti"
app_description = "Swiss SME Chart of Accounts templates for ERPNext (EN + FR)"
app_version = "0.0.1"
app_email = "liechtjc@gmail.com"
app_license = "MIT"

override_whitelisted_methods = {
	"erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.get_charts_for_country": "swiss_coa.chart_of_accounts.get_charts_for_country",
	"erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.get_chart": "swiss_coa.chart_of_accounts.get_chart",
}
