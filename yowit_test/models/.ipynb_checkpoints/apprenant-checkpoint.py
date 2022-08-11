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
    _rec_name='prenom'
    

    def name_get(self):
        dark= []
        for app in self:
            name= '(' + app.classe_id.nom_classe + ')' + app.prenom + ' ' + app.nom 
            dark.append((app.id,name))
            
        return dark