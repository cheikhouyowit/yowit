from odoo import models,field,api


class Classe(models.Model):
    _name= "classe.yowit"
    nom=field.Char("nom")
    code=field.Char()

    
