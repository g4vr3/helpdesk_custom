from odoo import models, fields

class HelpdeskCategory(models.Model):
    _name = 'helpdesk.category'
    _description = 'Categoría de Ticket de Soporte'

    name = fields.Char(string='Nombre de la Categoría', required=True) #nombre de la categoria
    description = fields.Text(string='Descripción') #descripcion de la categoria