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
        'views/helpdesk_menu.xml',
        'data/helpdesk_ticket_category_data.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}