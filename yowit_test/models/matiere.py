from odoo import models,field,api


class Matiere(models.Model):
    _name= "matiere.yowit"
    nom=field.Char("nom")
    code=field.Char()

    
