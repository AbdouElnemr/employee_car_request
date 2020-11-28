# -*- coding: utf-8 -*-
from odoo import http

class EmployeeCarRequest(http.Controller):
    # @http.route('/employee_car_request/employee_car_request/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    @http.route('/api/create_car_request', auth='public', csrf=False, methods=['post'])
    def create_car_request(self, **kw):
        return "The create car request has been Created !!"

    @http.route('/car_request/list/', auth='user', website=True, methods=['GET'], type='http')
    def list(self, **kw):
        return http.request.render('employee_car_request.car_request', {
            'objects': http.request.env['car.request'].search([('employee_id.user_id', '=', http.request.uid)]),
        })

#     @http.route('/employee_car_request/employee_car_request/objects/<model("employee_car_request.employee_car_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_car_request.object', {
#             'object': obj
#         })