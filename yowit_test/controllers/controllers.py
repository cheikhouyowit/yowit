# -*- coding: utf-8 -*-
# from odoo import http


# class YowitTest(http.Controller):
#     @http.route('/yowit_test/yowit_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yowit_test/yowit_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yowit_test.listing', {
#             'root': '/yowit_test/yowit_test',
#             'objects': http.request.env['yowit_test.yowit_test'].search([]),
#         })

#     @http.route('/yowit_test/yowit_test/objects/<model("yowit_test.yowit_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yowit_test.object', {
#             'object': obj
#         })
