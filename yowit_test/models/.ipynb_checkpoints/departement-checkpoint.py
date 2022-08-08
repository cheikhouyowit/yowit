from odoo import models,fields,api


class Departement(models.Model):
    _name= "departement.yowit"
    nom=fields.Char("nom")
    code=fields.Char()
    professeur_id=fields.One2many(comodel_name='professeur.yowit', inverse_name='departement_id')
    matiere_id=fields.One2many(comodel_name='matiere.yowit', inverse_name='departement_id')
    
