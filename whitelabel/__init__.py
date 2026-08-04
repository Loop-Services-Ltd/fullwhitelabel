# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.0.1'
__logo__ = '/assets/whitelabel/images/whitelabel_logo.jpg'

try:
	import frappe
except ImportError:
	frappe = None

if frappe is not None and getattr(frappe, "conf", None) and frappe.conf.get("app_logo_url"):
	__logo__ = frappe.conf.get("app_logo_url") or __logo__
