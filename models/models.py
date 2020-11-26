# -*- coding: utf-8 -*-

from odoo import models, fields, api
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