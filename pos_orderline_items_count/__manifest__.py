# -*- coding: utf-8 -*-
{
    'name': 'Pos Order Line Items Count',
    'version': '16.0.1.0.0',
    'summary': 'Module to show the count, quantity of items in the pos screen and pos receipt',
    'description': 'This module helps to show the count, quantity of items in the pos screen and pos receipt',
    'category': 'Point of Sale, FM',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': "https://www.bitsuptech.com",
    'license': 'LGPL-3',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'pos_orderline_items_count/static/src/js/product_screen.js',
            'pos_orderline_items_count/static/src/js/pos_receipt.js',
            'pos_orderline_items_count/static/src/xml/pos_items_count.xml',
            'pos_orderline_items_count/static/src/xml/pos_receipt.xml',
        ],

    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False
}
