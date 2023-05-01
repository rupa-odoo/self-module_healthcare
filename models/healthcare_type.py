from odoo import models,fields
class Healthcare_Types(models.Model):
    _name="healthcare.type"
    _description="Healthcare types"

    name=fields.Char("name",required=True)
    