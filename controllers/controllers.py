# -*- coding: utf-8 -*-
# from odoo import http


# class Dam2(http.Controller):
#     @http.route('/dam2/dam2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dam2/dam2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dam2.listing', {
#             'root': '/dam2/dam2',
#             'objects': http.request.env['dam2.dam2'].search([]),
#         })

#     @http.route('/dam2/dam2/objects/<model("dam2.dam2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dam2.object', {
#             'object': obj
#         })

