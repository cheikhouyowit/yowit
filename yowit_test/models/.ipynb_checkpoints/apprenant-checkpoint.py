from odoo import models,fields,api


class Apprenants(models.Model):
    _name= "apprenant.yowit"
    prenom=fields.Char("prenom")
    nom=fields.Char("nom")
    adresse=fields.Char("adresse")
    sexe=fields.Selection([("masculin","Masculin"),("feminin","Feminin")])
    email=fields.Char()
    telephone=fields.Char()
    date_naiss=fields.Date("Date de naissance")
    date_debut=fields.Datetime("date debut")
    departement_id=fields.Many2one('departement.yowit')
    classe_id=fields.Many2one('classe.yowit')
    _parent_name='apprenant_id'
   

