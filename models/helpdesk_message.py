from odoo import models, fields

class HelpdeskMessage(models.Model):
    _name = 'helpdesk.message'
    _description = 'Mensaje o Comentario de Ticket de Soporte'

    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket Relacionado')
    user_id = fields.Many2one('res.users', string='Usuario')
    message = fields.Text(string='Mensaje')
    create_date = fields.Datetime(string='Fecha de Envío', default=fields.Datetime.now, readonly=True)