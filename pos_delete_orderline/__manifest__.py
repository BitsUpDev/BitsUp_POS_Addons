# -*- coding: utf-8 -*-
{
    'name': "Remove Order Line In POS ",
    'summary': """
        Remove Individual Orderlines In Point Of Sale. """,
    'description': """
        Remove each lines from selected order by simply clicking X button or clear all order with a single click. 
    """,
    'author': "BitsUp Technologies",
    'website': "https://www.bitsuptech.com",
    'maintainer': "BitsUp Technologies",
    'category': 'Point of Sale, FM',
    'version': '16.0.1.0.0',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'pos_delete_orderline/static/src/js/clear_button.js',
            'pos_delete_orderline/static/src/js/clear_order_line.js',
            'pos_delete_orderline/static/src/xml/clear_button.xml',
            'pos_delete_orderline/static/src/xml/clear_order_line.xml',
        ],

    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
