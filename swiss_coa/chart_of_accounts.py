import json
import os

import frappe

# Path to our own verified COA templates
VERIFIED_PATH = os.path.join(
	os.path.dirname(__file__),
	"accounts", "doctype", "account", "chart_of_accounts", "verified",
)


@frappe.whitelist()
def get_charts_for_country(country, with_standard=False):
	"""Extends ERPNext's get_charts_for_country to also include swiss_coa templates."""
	from erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts import (
		get_charts_for_country as _original,
	)

	charts = _original(country, with_standard)

	country_code = frappe.get_cached_value("Country", country, "code")
	if country_code and os.path.exists(VERIFIED_PATH):
		for fname in os.listdir(VERIFIED_PATH):
			fname = frappe.as_unicode(fname)
			if not fname.endswith(".json"):
				continue
			with open(os.path.join(VERIFIED_PATH, fname)) as f:
				content = json.loads(f.read())
			if (
				content
				and content.get("country_code") == country_code
				and content.get("disabled", "No") == "No"
			):
				name = content["name"]
				if name not in charts:
					charts.insert(0, name)

	return charts


@frappe.whitelist()
def get_chart(chart_template, existing_company=None):
	"""Extends ERPNext's get_chart to also load templates from swiss_coa."""
	from erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts import (
		get_chart as _original,
	)

	# Try ERPNext's built-in templates first
	result = _original(chart_template, existing_company)
	if result:
		return result

	# Fall back to our own verified folder
	if os.path.exists(VERIFIED_PATH):
		for fname in os.listdir(VERIFIED_PATH):
			fname = frappe.as_unicode(fname)
			if not fname.endswith(".json"):
				continue
			with open(os.path.join(VERIFIED_PATH, fname)) as f:
				chart = json.loads(f.read())
			if chart.get("name") == chart_template:
				return chart.get("tree")

	return None
