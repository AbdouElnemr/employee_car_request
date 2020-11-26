# -*- coding: utf-8 -*-

from odoo import models, fields, api
class CarRequest(models.Model):
    _name = "car.request"
    _description = "car desc"

    name = fields.Char(string="Request", required=True, )
    date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date",)
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Car", required=True, )