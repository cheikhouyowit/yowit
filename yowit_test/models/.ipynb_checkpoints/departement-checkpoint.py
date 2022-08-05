from odoo import models,field,api


class Departement(models.Model):
    _name= "departement.yowit"
    nom=field.Char("nom")
    code=field.Char()

    
