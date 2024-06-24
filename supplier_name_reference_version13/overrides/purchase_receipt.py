import frappe
from frappe import _, throw
from frappe.utils import get_link_to_form
from erpnext.stock.doctype.purchase_receipt.purchase_receipt import PurchaseReceipt



class CustomPurchaseReceipt(PurchaseReceipt):
    def validate(self):
        self.po_required()
    
    def po_required(self):
            if frappe.db.get_value("Buying Settings", None, "po_required") == "Yes":

                if frappe.get_value(
                    "Supplier", self.supplier, "allow_purchase_invoice_creation_without_purchase_order"
                ):
                    return

                for d in self.get("items"):
                    if not d.purchase_order:
                        msg = _("Purchase Order Required for item {}").format(frappe.bold(d.item_code))
                        msg += "<br><br>"
                        msg += _("To submit the invoice without purchase order please set {0} as {1} in {2}").format(
                            frappe.bold(_("Purchase Order Required")),
                            frappe.bold("No"),
                            get_link_to_form("Buying Settings", "Buying Settings", "Buying Settings"),
                        )
                        throw(msg, title=_("Mandatory Purchase Order"))