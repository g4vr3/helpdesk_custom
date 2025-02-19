from odoo import models, fields

class HelpdeskTicketCategory(models.Model):
    _name = 'helpdesk.ticket.category'
    _description = 'Categoría del Ticket de Soporte'

    name = fields.Char(string='Nombre de la categoría', required=True)