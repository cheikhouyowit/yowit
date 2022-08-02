from odoo import fields, models, api

class Index(models.Model):
    _name='index.index'
    _description= 'ceci est un teste de devdingo'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
    