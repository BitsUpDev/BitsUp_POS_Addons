# -*- coding: utf-8 -*-
{
    'name': 'POS Booking Order',
    'version': '16.0.1.0.0',
    'summary': """From a POS session, users can create pickup or 
                delivery orders, which they can then confirm as POS orders.""",
    'description': """The module helps you to book orders from Shop,
                  Bar/Restaurant in POS.User can create pickup or delivery 
                  orders,later confirm booked orders to POS orders.""",
    'category': 'Point of Sale, FM',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': "https://www.bitsuptech.com",
    'depends': ['base', 'point_of_sale'],
    'images': ['static/description/banner.jpg'],
    'data': ['security/ir.model.access.csv',
             'data/ir_sequence_data.xml',
             'views/pos_config_views.xml',
             'views/book_order_views.xml',
             'views/pos_order_views.xml'
             ],
    'assets': {
        'point_of_sale.assets': [
            '/pos_book_order/static/src/xml/Buttons.xml',
            '/pos_book_order/static/src/xml/BookOrderPopup.xml',
            '/pos_book_order/static/src/xml/BookedOrdersScreen.xml',
            '/pos_book_order/static/src/xml/OrderReceipt.xml',
            '/pos_book_order/static/src/js/BookOrderPopup.js',
            '/pos_book_order/static/src/js/BookOrderButton.js',
            '/pos_book_order/static/src/js/BookedOrdersButton.js',
            '/pos_book_order/static/src/js/BookedOrdersScreen.js',
            '/pos_book_order/static/src/js/models.js',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
