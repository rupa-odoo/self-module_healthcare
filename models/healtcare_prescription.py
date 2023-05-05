from odoo import models,fields,api
from datetime import date,datetime
class HealthcarePrescription(models.Model):
    _name="healtcare.prescription"
    _description="Healtcare Prescription"

    medicine=fields.Char(string="Medicine")
    dose=fields.Char(string="Dose")
    duration=fields.Date(string="Duration")
    status=fields.Selection(
        selection=[('accepted','Accepted'),('refused','Refused')],copy=False
    )

    





