{
    'name': 'Helpdesk Personalizado',
    'version': '1.0',
    'summary': 'Sistema de gestión de tickets de soporte',
    'author': 'Izan (g4vr3)',
    'category': 'Services',
    'depends': ['base', 'mail'],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_category_views.xml',
        'views/helpdesk_message_views.xml',
        'views/helpdesk_menu.xml',
        'data/helpdesk_demo_data.xml',
        'data/helpdesk_server_actions.xml',
        'data/helpdesk_mail_templates.xml',
    
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}