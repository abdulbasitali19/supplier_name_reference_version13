import frappe

@frappe.whitelist()
def updating_supllier_number_in_references():
    query = """
            SELECT 
                jea.supplier_number,
                je.name
            FROM                
                `tabJournal Entry Account` jea
            INNER JOIN 
                `tabJournal Entry` je ON je.name = jea.parent
            WHERE
                jea.party_type = 'Supplier'
                AND je.docstatus = 1
        """
    spno = frappe.db.sql(query, as_dict=1)
    spno_dict = {item['name']: item['supplier_number'] for item in spno}
    return spno_dict