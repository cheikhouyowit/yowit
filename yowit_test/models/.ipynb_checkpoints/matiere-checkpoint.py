from odoo import models,fields,api


class Matiere(models.Model):
    _name= "matiere.yowit"
    nom=fields.Char("nom")
    code=fields.Char()

    
