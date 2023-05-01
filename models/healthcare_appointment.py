from odoo import fields,models
from datetime import date


class HealthcareAppointment(models.Model):
    _name="healthcare.appointment"
    _description="Healtcare Appointment"
# Patient Fields
    name=fields.Char(string="Name",required=True)
    age=fields.Integer(string="Age")
    gender=fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')],copy=True,default='new')
    date_of_birth=fields.Date(string="Date of Birth")
    mobile=fields.Char(string="Mobile")
    appointment_date=fields.Date(string="Appoinment Date")
    address=fields.Text(string="Address")
    email=fields.Char(string="Email")
    bloodgroup=fields.Char(string="Blood Group")

# Appointment fields
    urgency_level=fields.Char(string="Urgency Level")
    docter=fields.Many2one("res.users",string="Docter")
    healthcare_tagIds=fields.Many2many("healthcare.tag",string="Healthcare_Tag")
    healthcare_typeIds=fields.Many2one("healthcare.type",string="Healthcare_Type")
    price=fields.Float(string="Price")
    prescription=fields.Text(string="Prescription")

    state=fields.Selection(
        string='state',
        selection=[('draft','Draft'),('requested','Requested'),('outcome','Outcome'),('invoice','Invoice')],copy=True,default='draft')