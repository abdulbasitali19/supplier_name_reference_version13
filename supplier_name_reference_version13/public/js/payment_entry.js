frappe.ui.form.on('Payment Entry',{
    validate: function(frm) {
        frappe.call({
            method: "supplier_name_reference_version13.overrides.payment_entry.updating_supplier_number_in_references",
            args:{
                "party":frm.doc.party 
            },
            callback: function(r, rt) {
                if (r.message) {
                    console.log(r.message)
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










