from odoo import fields,models,api
from datetime import date


class HealthcareAppointment(models.Model):
    _name="healthcare.appointment"
    _description="Healtcare Appointment"
# Patient Fields
    name=fields.Char(string="Name",required=True)
    age=fields.Integer(string="Age" ,compute="_patient_age")
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
    price=fields.Float(string="Price", compute="_patient_price")
    prescription=fields.Text(string="Prescription")
    prescription_ids=fields.Many2many("healthcare.medicine",string="Prescription")
    

    state=fields.Selection(
        string='state',
        selection=[('draft','Draft'),('requested','Requested'),('outcome','Outcome'),('invoice','Invoice')],copy=True,default='draft')

    @api.depends("prescription_ids.price")
    def _patient_price(self):
        if self and (self.mapped("prescription_ids.price")):
            self.price=sum(self.mapped("prescription_ids.price"))
            
            print(self.price)
            
        else:
            self.price=0

    @api.depends("date_of_birth")
    def _patient_age(self):
        if self and self.date_of_birth:
            # self.age=today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            self.age=((date.today()-self.date_of_birth).days)//365
        else:
            self.age=0

    
        