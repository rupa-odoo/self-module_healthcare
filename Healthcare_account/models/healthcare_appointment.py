from odoo import models,Command
class healthcareappointment(models.Model):
    _inherit="healthcare.appointment"


    def action_invoice(self):
        self.env['account.move'].create({
            "partner_id":self.id,
            "move_type":"out_invoice",
            "invoice_line_ids":[
                Command.create({
                    # "product_id":self.prescription_ids.id,
                    "name":self.name,
                    "price_unit":self.price,
                }),
            ]

        })
        print("............ok")
        return super().action_invoice()