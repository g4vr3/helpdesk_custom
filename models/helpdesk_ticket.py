from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket de Soporte'

    name = fields.Char(string='Nombre del Ticket', required=True)
    description = fields.Text(string='Descripción del Problema')
    customer_id = fields.Many2one('res.partner', string='Cliente')
    state = fields.Selection([
        ('new', 'Nuevo'),
        ('in_progress', 'En Proceso'),
        ('resolved', 'Resuelto'),
        ('closed', 'Cerrado')
    ], string='Estado', default='new')
    create_date = fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now, readonly=True)
    deadline = fields.Datetime(string='Fecha Límite de Resolución')
    assigned_user_id = fields.Many2one('res.users', string='Técnico Asignado')
    priority = fields.Selection([
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('very_high', 'Muy Alta')
    ], string='Prioridad', default='medium')
    category_id = fields.Many2one('helpdesk.category', string='Categoría')
    message_ids = fields.One2many('helpdesk.message', 'ticket_id', string='Mensajes/Comentarios')