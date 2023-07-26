# -*- coding: utf-8 -*-
{
    'name': 'POS Restriction For Zero Quantity.',
    'version': '16.0.1.0.0',
    'category': 'Point of Sale, FM',
    'summary': 'This module will restrict zero quantity confirmation in POS.',
    'description': """This module will help you to avoid zero quantity 
                        confirmation in POS. It will show warning if zero 
                        quantity confirmation occurred.""",
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': "https://www.bitsuptech.com",
    'images': ['static/description/banner.jpg'],
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'pos_zero_quantity_restrict/static/src/js/**/*.js',
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
