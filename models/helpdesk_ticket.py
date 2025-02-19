from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket de Soporte'

    name = fields.Char(string='Nombre del Ticket', required=True)
    customer_id = fields.Many2one('res.partner', string='Cliente')
    assigned_user_id = fields.Many2one('res.users', string='Usuario Asignado')
    state = fields.Selection([
        ('new', 'Nuevo'),
        ('in_progress', 'En Progreso'),
        ('done', 'Completado'),
        ('cancelled', 'Cancelado')
    ], string='Estado', default='new')
    priority = fields.Selection([
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('very_high', 'Muy Alta')
    ], string='Prioridad', default='medium')
    category_id = fields.Many2one('helpdesk.ticket.category', string='Categoría')
    deadline = fields.Date(string='Fecha Límite')
    description = fields.Text(string='Descripción')