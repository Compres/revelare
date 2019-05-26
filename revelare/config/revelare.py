# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Cash Flow"),
			"items": [
				{
					"type": "doctype",
					"name": "Budgeted Cash Flow",
					"description": _("Entries budgeted cash flow.")
				},
				{
					"type": "report",
					"name": "Budgeted Cash Flow Report",
					"doctype": "Revelare",
					"is_query_report": True
				},
				{
					"type": "doctype",
					"label": _("Category Cash Flow Group"),
					"name": "Category Cash Flow Group",
					"link": "Tree/Category Cash Flow Group",
					"description": _("Manage Categories Group Tree."),
				}
			]
		},
		{
			"label": _("Setup Revelare"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Configuration Revelare",
					"description": _("General Configuration to Revelare.")
				}
			]
		},
		{
			"label": _("Analytics"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "page",
					"name": "sales-analytics-2",
					"label": _("Sales Analytics 2"),
					"icon": "fa fa-bar-chart",
				}
			]
		},
		{
			"label": _("Delivery Note by Item with 4 Item Column Totalization"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "report",
					"name": "Delivery Note By Item",
					"doctype": "Revelare",
					"is_query_report": True
				}
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"name": "Purchase Ledger",
					"label": _("Purchase Ledger"),
					"doctype": "Revelare",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Sales Ledger",
					"label": _("Sales Ledger"),
					"doctype": "Revelare",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "General Ledger Report",
					"label": _("General Ledger Report"),
					"doctype": "Revelare",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Daily Book Report",
					"label": _("Daily Book Report"),
					"doctype": "Revelare",
					"is_query_report": True
				}
			]
		},
		{
			"label": _("Agriculture Reports"),
			"items": [
				{
					"type": "report",
					"name": "Production Report",
					"label": _("Production Report"),
					"doctype": "Revelare",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Production Per Day Report",
					"label": _("Production Per Day Report"),
					"doctype": "Revelare",
					"is_query_report": True
				}
			]
		}
	]
