from odoo import fields,models,api
from datetime import date
from odoo.exceptions import UserError,ValidationError


class HealthcareAppointment(models.Model):
    _name="healthcare.appointment"
    _description="Healtcare Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

# Patient Fields
    name=fields.Char(string="Name",required=True)
    image=fields.Binary(string = "Image")
    # sequence = fields.Integer(string = "Sequence")
    age=fields.Integer(string="Age" ,compute="_patient_age")
    gender=fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')],copy=True)
    date_of_birth=fields.Date(string="Date of Birth")
    mobile=fields.Char(string="Mobile")
    appointment_date=fields.Date(string="Appoinment Date")
    address=fields.Text(string="Address")
    email=fields.Char(string="Email")
    bloodgroup=fields.Char(string="Blood Group")
    color=fields.Integer(string="color")

# Appointment fields
    urgency_level=fields.Char(string="Urgency Level")
    docter=fields.Many2one("res.users",string="Docter")
    healthcare_tagIds=fields.Many2many("healthcare.tag",string="Healthcare_Tag")
    healthcare_typeIds=fields.Many2one("healthcare.type",string="Healthcare_Type")
    price=fields.Float(string="Price", compute="_patient_price")
    prescription=fields.Text(string="Prescription")
    prescription_ids=fields.Many2many("healthcare.medicine",string="Prescription")
    bed_manage_ids=fields.Many2one("healthcare.bedmanage",string="Bed Manage",domain="[('bed_status','not in',['reserved','occuiped'])]")
    # bed_ids=fields.Many2one("healthcare.bedmanage",string="Bed Manage")
    
    # related feilds 
    bed_name=fields.Char(related="bed_manage_ids.name",string="Name",tracking=True)
    bed_charge=fields.Float(related="bed_manage_ids.reservation_charge",string="Charge")
    
    
    
    state=fields.Selection(
        string='state',
        selection=[('draft','Draft'),('active','Active'),('cancle','Cancle'),('invoice','Invoice')],copy=True,default='draft',tracking=True)

    _sql_constraints=[('check_age','CHECK(date_of_birth<current_date)','Age must be postive')]
    _sql_constraints=[('check_appointment_date','CHECK(appointment_date>=current_date)','Date of Appoinment must be today of other day')]


    


    @api.depends("prescription_ids.price")
    def _patient_price(self):
        if self and (self.mapped("prescription_ids.price"),self.mapped("bed_manage_ids.reservation_charge")):
            self.price=sum(self.mapped("prescription_ids.price")+self.mapped("bed_manage_ids.reservation_charge")) 
        else:
            self.price=0

    @api.depends("date_of_birth")
    def _patient_age(self):
        if self and self.date_of_birth:
            # self.age=today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            self.age=((date.today()-self.date_of_birth).days)//365
        else:
            self.age=0

    def action_active(self):
        if self.state=="cancle":
            raise UserError("Cancle state should not be active")
        else:
            self.state="active"
        return True

    def action_cancled(self):
        if self.state=="active":
            raise UserError("Active state should not be Cancle")
        else:
            self.state="cancle"
        return True
    
    def action_invoice(self):
        self.state="invoice"
    
        