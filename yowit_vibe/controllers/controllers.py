# -*- coding: utf-8 -*-
# from odoo import http


# class YowitVibe(http.Controller):
#     @http.route('/yowit_vibe/yowit_vibe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yowit_vibe/yowit_vibe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yowit_vibe.listing', {
#             'root': '/yowit_vibe/yowit_vibe',
#             'objects': http.request.env['yowit_vibe.yowit_vibe'].search([]),
#         })

#     @http.route('/yowit_vibe/yowit_vibe/objects/<model("yowit_vibe.yowit_vibe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yowit_vibe.object', {
#             'object': obj
#         })
