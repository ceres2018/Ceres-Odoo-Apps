# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPlaceholderColor(http.Controller):
#     @http.route('/custom_placeholder_color/custom_placeholder_color', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_placeholder_color/custom_placeholder_color/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_placeholder_color.listing', {
#             'root': '/custom_placeholder_color/custom_placeholder_color',
#             'objects': http.request.env['custom_placeholder_color.custom_placeholder_color'].search([]),
#         })

#     @http.route('/custom_placeholder_color/custom_placeholder_color/objects/<model("custom_placeholder_color.custom_placeholder_color"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_placeholder_color.object', {
#             'object': obj
#         })
