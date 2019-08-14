# -*- coding: utf-8 -*-
from odoo import http

# class OdooAppTest(http.Controller):
#     @http.route('/odoo_app_test/odoo_app_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_app_test/odoo_app_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_app_test.listing', {
#             'root': '/odoo_app_test/odoo_app_test',
#             'objects': http.request.env['odoo_app_test.odoo_app_test'].search([]),
#         })

#     @http.route('/odoo_app_test/odoo_app_test/objects/<model("odoo_app_test.odoo_app_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_app_test.object', {
#             'object': obj
#         })