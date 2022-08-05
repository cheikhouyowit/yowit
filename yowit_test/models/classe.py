from odoo import models,fields,api


class Classe(models.Model):
    _name= "classe.yowit"
    nom=fields.Char("nom")
    code=fields.Char()

    
