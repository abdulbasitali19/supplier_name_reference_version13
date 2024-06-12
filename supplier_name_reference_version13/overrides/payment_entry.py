import frappe

@frappe.whitelist()
def updating_supplier_number_in_references(party):
    query = """
            SELECT 
                jea.supplier_number,
                je.name
            FROM                
                `tabJournal Entry Account` jea
            INNER JOIN 
                `tabJournal Entry` je ON je.name = jea.parent
            WHERE
            jea.party = %s AND je.docstatus = 1   """
    spno = frappe.db.sql(query, party, as_dict=1)
    spno_dict = {item['name']: item['supplier_number'] for item in spno}
    return spno_dict
