import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


def execute():
    frappe.reload_doc("Setup", "doctype", "project")
    create_custom_field("project",
	    dict(fieldname="phamos_section_break", label="phamos",
		fieldtype="Section Break", insert_before="naming_series"))

    create_custom_field("project",
		dict(fieldname="planned_hours", label="Planned Hours",
		fieldtype="Data",
		insert_after="phamos_section_break"))
    
    
    create_custom_field("project",
	    dict(fieldname="phamos_section_break_end", label="",
		fieldtype="Section Break", insert_after="planned_hours"))
    