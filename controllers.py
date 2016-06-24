# -*- coding: utf-8 -*-
from openerp import http

# class CustomerEdu(http.Controller):
#     @http.route('/customer_edu/customer_edu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_edu/customer_edu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_edu.listing', {
#             'root': '/customer_edu/customer_edu',
#             'objects': http.request.env['customer_edu.customer_edu'].search([]),
#         })

#     @http.route('/customer_edu/customer_edu/objects/<model("customer_edu.customer_edu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_edu.object', {
#             'object': obj
#         })