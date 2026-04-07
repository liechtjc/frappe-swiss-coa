app_name = "swiss_coa"
app_title = "Swiss COA"
app_publisher = "Jean-Christophe Liechti"
app_description = "Swiss SME Chart of Accounts templates for ERPNext (EN + FR)"
app_version = "0.0.1"
app_email = "liechtjc@gmail.com"
app_license = "MIT"

doc_events = {
	"Company": {
		"after_insert": "swiss_coa.company_defaults.set_swiss_defaults",
	}
}
