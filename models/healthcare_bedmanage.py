from odoo import models,fields
class Healthcare_bedmanage(models.Model):
    _name="healthcare.bedmanage"
    _description="Healthcare bedmanage"

    name=fields.Char("name",required=True)
    reservation_price=fields.Integer(string="Reservation Price")
    bed_type=fields.Selection(
        string="Bed Type",
        selection=[('common','Common'),('private','Private')]
    )
    bed_status=fields.Selection(
        string="Bed status",
        selection=[('free','Free'),('reserved','Reserved'),('occuiped','Occuiped'),('notavailable','Not Available')],default='free'
    )
