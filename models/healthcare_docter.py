from odoo import models,fields
class Doctor(models.Model):
    _inherit = 'res.users'


    specialization = fields.Selection([
        ('general_practitioner', 'General Practitioner'),
        ('specialist', 'Specialist'),
    ], 'Specialization')

    doctor_appointment=fields.One2many("healthcare.appointment","docter",domain=[('state','in',['draft','active'])])