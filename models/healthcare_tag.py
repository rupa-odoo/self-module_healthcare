from odoo import models,fields
class HealthcareTag(models.Model):
    _name="healthcare.tag"
    _description="Healthcare Tags"

    name=fields.Char("Name",required=True)
    color=fields.Integer(string="Color")