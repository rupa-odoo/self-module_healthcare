from odoo import models,fields
class resusers(models.Model):
    _inherit="res.users"

    res_docters=fields.One2many('healthcare.appointment',"docter", string="Appointment")

    