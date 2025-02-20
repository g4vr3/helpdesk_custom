#helpdesk_custom/models/ticket_reminder.py
from odoo import models, fields
import datetime

class HelpdeskTicketReminder(models.Model):
    _name = 'helpdesk.ticket.reminder'

    def send_unattended_ticket_reminder(self):
        # Obtener la fecha y hora actual y restar 48 horas usando datetime
        time_limit = datetime.datetime.now() - datetime.timedelta(days=1)

        # Buscar tickets no atendidos
        unattended_tickets = self.env['helpdesk.ticket'].search([
            ('state', '=', 'new'),
            ('create_date', '<=', time_limit)
        ])

        # Enviar recordatorio para cada ticket no atendido
        for ticket in unattended_tickets:
            template = self.env.ref('helpdesk_custom.mail_template_ticket_reminder')
            if template:
                template.send_mail(ticket.id, force_send=True)
