{
    'name': "Clean Attachments",
    'summary': "Optimize and manage attachments efficiently by cleaning redundant files.",
    "license": "AGPL-3",
    'description': """
        Clean Attachments module helps to optimize storage by identifying and removing redundant or unnecessary attachments in Odoo. 
        Key Features:
        - Detect and remove duplicate attachments.
        - Automate attachment cleanup based on specific rules.
        - Improve storage efficiency and system performance.
        - User-friendly interface for managing attachments.
        This module is ideal for businesses looking to optimize their database and maintain a clutter-free document management system.
    """,
    'author': "GrowingUpp",
    'website': "",
    'category': 'Tools',
    'version': '16.0.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
