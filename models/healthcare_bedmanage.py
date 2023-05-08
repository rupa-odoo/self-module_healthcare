from odoo import models,fields
class Healthcare_bedmanage(models.Model):
    _name="healthcare.bedmanage"
    _description="Healthcare bedmanage"

    name=fields.Char("name",required=True)
    reservation_charge=fields.Integer(string="Reservation Charge")
    bed_type=fields.Selection(
        string="Bed Type",
        selection=[('common','Common'),('private','Private')]
    )
    bed_status=fields.Selection(
        string="Bed status",
        selection=[('available','Available'),('reserved','Reserved'),('occuiped','Occuiped'),('notavailable','Not Available')],default='free'
    )

    _sql_constraints=[('check_reservation_charge','CHECK(reservation_charge>0)','Reservation Charge must be positive')]

