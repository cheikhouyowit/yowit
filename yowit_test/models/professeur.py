from odoo import models,fields,api


class Professeur(models.Model):
    _name= "professeur.yowit"
    prenom=fields.Char("prenom")
    nom=fields.Char("nom")
    adresse=fields.Char("adresse")
    sexe=fields.Selection([("masculin","Masculin"), ("feminin","Feminin")])
    email=fields.Char()
    telephone=fields.Char()
    date_debut=fields.DateTime("date debut")
    
