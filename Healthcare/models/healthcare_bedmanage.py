from odoo import models,fields,api
class Healthcare_bedmanage(models.Model):
    _name="healthcare.bedmanage"
    _description="Healthcare bedmanage"

    name=fields.Char("name",required=True)
    reservation_charge=fields.Integer(string="Reservation Charge")
    bed_manage_ids=fields.One2many('healthcare.appointment','bed_manage_ids')
    bed_count=fields.Integer(compute="_bed_count")

    bed_type=fields.Selection(
        string="Bed Type",
        selection=[('common','Common'),('private','Private')]
    )
    bed_status=fields.Selection(
        string="Bed status",
        selection=[('available','Available'),('reserved','Reserved'),('occuiped','Occuiped'),('notavailable','Not Available')],default='free'
    )

    _sql_constraints=[('check_reservation_charge','CHECK(reservation_charge>0)','Reservation Charge must be positive')]

    @api.depends('bed_manage_ids')
    def _bed_count(self):
        for record in self:
            record.bed_count=len(record.bed_manage_ids)

    def action_bedmanage(self):
        return{
            'type': 'ir.actions.act_window',
            'name': ('appointment'),
            'res_model': 'healthcare.appointment',
            'view_type': 'list',
            'view_mode': 'list',
            'domain': [('id', 'in', self.bed_manage_ids.ids)],

        }