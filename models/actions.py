# helpdesk_custom/models/actions.py

from odoo import models

class HelpdeskTicketActions(models.Model):
    _name = 'helpdesk.ticket.actions'

    def execute_ticket_notifications(self, record):
        # Notificar al cliente cuando el ticket se resuelve
        self.env['helpdesk.ticket.notifications'].notify_customer_ticket_resolved(record)
        
        # Notificar al técnico cuando se le asigna un ticket
        self.env['helpdesk.ticket.notifications'].notify_technician_ticket_assigned(record)
        
    def execute_ticket_reminders(self):
        # Llamar al método de recordatorio de tickets no atendidos
        self.env['helpdesk.ticket.reminder'].send_unattended_ticket_reminder()
