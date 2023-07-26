# -*- coding: utf-8 -*-

{
    'name': 'Point of Sale Logo',
    'version': '16.0.1.0.0',
    'summary': """Logo For Every Point of Sale (Screen & Receipt)""",
    'description': """"This module helps you to set a logo for every point of sale. This will help you to
                 identify the point of sale easily. You can also see this logo in pos screen and pos receipt.""",
    'category': 'Point Of Sale, FM',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'website': "http://www.bitsuptech.com",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/pos_config_image_view.xml',
    ],
    'assets': {
            'point_of_sale.assets': [
                'point_of_sale_logo/static/src/xml/pos_screen_image_view.xml',
                'point_of_sale_logo/static/src/xml/pos_ticket_view.xml'
            ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'Sequence': 1
}

