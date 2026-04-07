import frappe

SWISS_COA_TEMPLATES = ("CH_PME_avec numéro", "CH_SME_with number")

# account_number -> Company fieldname
DEFAULTS = {
	"1000": "default_cash_account",
	"1020": "default_bank_account",
	"1100": "default_receivable_account",
	"2000": "default_payable_account",
}


def set_swiss_defaults(doc, method):
	"""After a Company is inserted with a Swiss COA, set default accounts."""
	if doc.chart_of_accounts not in SWISS_COA_TEMPLATES:
		return

	updates = {}
	for account_number, fieldname in DEFAULTS.items():
		account = frappe.db.get_value(
			"Account",
			{"company": doc.name, "account_number": account_number},
			"name",
		)
		if account:
			updates[fieldname] = account

	if updates:
		frappe.db.set_value("Company", doc.name, updates)
