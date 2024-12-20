# -*- coding: utf-8 -*-
# from odoo import http


# class Managerebeca(http.Controller):
#     @http.route('/managerebeca/managerebeca', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managerebeca/managerebeca/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managerebeca.listing', {
#             'root': '/managerebeca/managerebeca',
#             'objects': http.request.env['managerebeca.managerebeca'].search([]),
#         })

#     @http.route('/managerebeca/managerebeca/objects/<model("managerebeca.managerebeca"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managerebeca.object', {
#             'object': obj
#         })
