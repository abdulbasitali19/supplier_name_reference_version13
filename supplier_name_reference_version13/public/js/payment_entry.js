frappe.ui.form.on('Payment Entry',{
    validate: function(frm) {
        debugger;
        frappe.call({
            method: "supplier_name_reference_version13.overrides.payment_entry.updating_supllier_number_in_references",
            callback: function(r, rt) {
                if (r.message) {
                    frm.doc.references.forEach(function(reference) {
                        if (reference.reference_name in r.message) {
                            reference.custom_supplier_number = r.message[reference.reference_name];
                            frappe.model.set_value(reference.doctype, reference.name, "supplier_number", r.message[reference.reference_name]);
                        }
                    });
                }
            }
        });
    }
    


})




    // frappe.ui.form.on('Payment Entry Reference', {
    //     reference_name(doc, cdt, cdn) {
    //         debugger;
    //         var d = frappe.get_doc(cdt, cdn);
    //         if (d.reference_doctype == "Journal Entry") {
    //             let spno = frappe.db.get_all("Journal Entry Account", filters = { "reference_type": d.reference_doctype, "reference_name": d.reference_name, "docstatus": 1 }, fields = ["custom_supplier_number"])
    //             d.custom_supplier_number = spno

    //         }

    //     }
    // })





