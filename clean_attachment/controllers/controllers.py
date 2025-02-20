# -*- coding: utf-8 -*-
# from odoo import http


# class CleanAttachment(http.Controller):
#     @http.route('/clean_attachment/clean_attachment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clean_attachment/clean_attachment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clean_attachment.listing', {
#             'root': '/clean_attachment/clean_attachment',
#             'objects': http.request.env['clean_attachment.clean_attachment'].search([]),
#         })

#     @http.route('/clean_attachment/clean_attachment/objects/<model("clean_attachment.clean_attachment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clean_attachment.object', {
#             'object': obj
#         })
