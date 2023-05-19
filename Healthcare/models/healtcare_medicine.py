from odoo import models,fields
class Healthcare_medicine(models.Model):
    _name="healthcare.medicine"
    _description="Healthcare medicine"

    name=fields.Char("name",required=True)
    price=fields.Float(string="Price")

    _sql_constraints=[('check_medicine_price','CHECK(price>0)','Medicine Charge must be positive')]
    