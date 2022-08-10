from odoo import models,fields,api


class Matiere(models.Model):
    _name= "matiere.yowit"
    nom=fields.Char("nom")
    code=fields.Char()
    departement_id=fields.Many2one('departement.yowit')
    professeur_id=fields.Many2many('professeur.yowit', relation='mat_prof', column1="nom", column2="prenom"  )
    _rec_name='nom'
    
