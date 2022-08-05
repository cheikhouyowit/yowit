from odoo import models,fields,api


class Departement(models.Model):
    _name= "departement.yowit"
    nom=fields.Char("nom")
    code=fields.Char()

    
