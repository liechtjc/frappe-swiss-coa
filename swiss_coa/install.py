import os
import shutil
import frappe


def _erpnext_verified_path():
	return os.path.join(
		frappe.get_app_path("erpnext"),
		"accounts", "doctype", "account", "chart_of_accounts", "verified",
	)


def _our_verified_path():
	return os.path.join(
		os.path.dirname(__file__),
		"accounts", "doctype", "account", "chart_of_accounts", "verified",
	)


def after_install():
	"""Copy Swiss COA JSON templates into ERPNext's verified/ directory."""
	src = _our_verified_path()
	dst = _erpnext_verified_path()
	for fname in os.listdir(src):
		if fname.endswith(".json"):
			shutil.copy2(os.path.join(src, fname), os.path.join(dst, fname))
			frappe.logger().info(f"swiss_coa: installed {fname} → {dst}")


def before_uninstall():
	"""Remove Swiss COA JSON templates from ERPNext's verified/ directory."""
	src = _our_verified_path()
	dst = _erpnext_verified_path()
	for fname in os.listdir(src):
		target = os.path.join(dst, fname)
		if os.path.exists(target):
			os.remove(target)
			frappe.logger().info(f"swiss_coa: removed {target}")
