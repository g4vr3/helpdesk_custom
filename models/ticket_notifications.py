#helpdesk_custom/models/ticket_notifications.py
from odoo import models

class HelpdeskTicketNotifications(models.Model):
    _name = 'helpdesk.ticket.notifications'
    _inherit = 'helpdesk.ticket'  # Asegurando que los métodos estén disponibles en el modelo de tickets

    def notify_customer_ticket_resolved(self):
        if self.state == 'resolved':
            template = self.env.ref('helpdesk_custom.mail_template_ticket_resolved')
            if template:
                template.send_mail(self.id, force_send=True)

    def notify_technician_ticket_assigned(self):
        if self.assigned_user_id:
            template = self.env.ref('helpdesk_custom.mail_template_ticket_assigned')
            if template:
                template.send_mail(self.id, force_send=True)
