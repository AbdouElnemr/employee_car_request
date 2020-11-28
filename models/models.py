# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError

class CarRequest(models.Model):
    _name = "car.request"
    _inherit = "mail.thread"
    _description = "car desc"

    name = fields.Char(string="Request", required=True, )
    date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date",)
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Car", required=True, )
    state = fields.Selection(string="", selection=[('draft', 'Draft'),('confirm', 'Confirm'),
                                                   ('validate', 'Validate'), ('refuse', 'Refuse'),
                                                   ('approved', 'Approved'), ], default="draft", track_visibility='onchange')

    email = fields.Char(string="Email", required=False, )
    website = fields.Char(string="Websit", required=False, )

    _sql_constraints = [
        ('unique_email', 'unique(email)', 'The email should be uniqu !! ')
    ]

    @api.onchange('email')
    def _onchange_email(self):
        result = {}
        if self.email:
            result.update({
                'value':{
                   'website' : 'http://www.%s' % (self.email.split('@')[1])
                },
                'warning':{
                    'title' : 'Congrats',
                    'message' : 'you have added an email '
                },
                'domain':{
                    'employee_id':[('id','!=','20')],
                }
            })
        return  result


    @api.constrains('email')
    def _check_email(self):
        if self.email.endswith('gmail.com'):
            raise ValidationError("Gamil is not accepted")
        if self.email.endswith('yahoo.com'):
            raise ValidationError("yahoo is not accepted")


    @api.multi
    def confirm_request(self):
        self.state = 'confirm'
    @api.multi
    def validate_request(self):
        self.state = 'validate'
    @api.multi
    def refuse_request(self):
        self.state = 'refuse'
    @api.multi
    def approve_request(self):
        self.state = 'approved'