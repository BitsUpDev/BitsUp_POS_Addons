# -*- coding: utf-8 -*-
{
    'name': 'POS Chat Box',
    'category': 'Point Of Sale, FM',
    'version': '16.0.1.0.0',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': 'https://www.bitsuptech.com',
    'summary': """POS Chat Box For Odoo16 Community and Enterprise Edition""",
    'description': """Using the POS screen, this module facilitates user '
                   'communication.""",
    'images': ['static/description/banner.png'],
    'depends': [
        'base',
        'point_of_sale',
    ],
    'assets': {
        'point_of_sale.assets': [
            '/pos_chatter/static/src/xml/pos_systray_icon.xml',
            '/pos_chatter/static/src/js/pos_systray_icon.js',
            '/pos_chatter/static/src/js//pos_msg_view.js',
            '/pos_chatter/static/src/js/pos_chat_view.js',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
