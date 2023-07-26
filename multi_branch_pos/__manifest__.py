# -*- coding: utf-8 -*-

{
    'name': "Multiple Branch Setup for POS",
    'version': "16.0.1.0.0",
    'summary': """ Multiple Branch Operation Setup for Odoo POS""",
    'description': """ Manages Multiple Branch Operation setup for Odoo Point of 
                    sale.""",
    'author': "BitsUp Technologies",
    'company': "BitsUp Technologies",
    'maintainer': "BitsUp Technologies",
    'website': "https://bitsuptech.com/",
    'category': 'Point of sale, FM',
    'depends': ['base', 'multi_branch_base', 'point_of_sale'],
    'data': [
        'security/multi_branch_pos_security.xml',
        'views/pos_config_views.xml',
        'views/pos_orders_views.xml',
        'views/pos_session_views.xml',
        'report/pos_order_report_views.xml'
    ],
    'images': ['static/description/banner.png'],
    'assets': {
        'point_of_sale.assets': [
            'multi_branch_pos/static/src/xml/branch.xml',
        ],
    },
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False
}
