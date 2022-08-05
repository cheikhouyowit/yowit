from odoo import models,field,api


class Professeur(models.Model):
    _name= "professeur.yowit"
    prenom=field.Char("prenom")
    nom=field.Char("nom")
    adresse=field.Char("adresse")
    sexe=field.Selection([("masculin","Masculin"), ("feminin","Feminin")])
    email=field.Char()
    telephone=field.Char()
    date_debut=field.DateTime("date debut")
    
