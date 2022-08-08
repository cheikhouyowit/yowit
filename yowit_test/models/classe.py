from odoo import models,fields,api


class Classe(models.Model):
    _name= "classe.yowit"
    nom_classe=fields.Char(string="nom")
    code=fields.Char()
    apprenant_id=fields.One2many('apprenant.yowit', inverse_name='classe_id')
    professeur_id=fields.Many2many('professeur.yowit', relation='class_prof', column1="nom", column2="prenom"  )
    matiere_id=fields.Many2many('matiere.yowit', relation='class_mat', column1="nom_classe", column2="nom"  )
    _parent_name= 'classe_id'

    
