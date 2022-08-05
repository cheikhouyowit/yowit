from odoo import models,field,api


class Apprenants(models.Model):
    _name= "apprenant.yowit"
    prenom=field.Char("prenom")
    nom=field.Char("nom")
    adresse=field.Char("adresse")
    sexe=field.Selection([("masculin","Masculin"),("feminin","Feminin")])
    email=field.Char()
    telephone=field.Char()
    date_naiss=field.Date("Date de naissance")
    date_debut=field.DateTime("date debut")

