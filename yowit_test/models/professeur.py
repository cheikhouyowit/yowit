from odoo import models,fields,api


class Professeur(models.Model):
    _name= "professeur.yowit"
    prenom=fields.Char("prenom")
    nom=fields.Char("nom")
    adresse=fields.Char("adresse")
    sexe=fields.Selection([("masculin","Masculin"), ("feminin","Feminin")])
    email=fields.Char()
    telephone=fields.Char()
    date_debut=fields.Datetime("date debut")
    departement_id=fields.Many2one('departement.yowit')
    matiere_id=fields.Many2one('matiere.yowit')
    classe_id=fields.Many2many('classe.yowit', relation='prof_class', column1="prenom", column2="nom"  )
    _rec_name='prenom'
    

    def name_get(self):
        dark= []
        for pro in self:
            name= pro.prenom + ' ' + pro.nom + '(' + pro.departement_id.nom + '/' + pro.classe_id.nom_classe + ')' 
            dark.append((pro.id,name))
            
        return dark
    
    
