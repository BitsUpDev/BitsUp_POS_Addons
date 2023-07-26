# -*- coding: utf-8 -*-
{
    'name': 'Simplified POS',
    'version': '16.0.1.0.0',
    'category': 'Point of Sale, FM',
    'summary': 'All aspects of POS on a single page.',
    'description': 'A straightforward point-of-sale system that enables '
                   'payment,order confirmation, and product selection all on '
                   'the same page.',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'images': ['static/description/banner.jpg'],
    'website': 'https://www.bitsuptech.com',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'simplified_pos/static/src/js/ProductScreen.js',
            'simplified_pos/static/src/js/ConfirmationPopup.js',
            'simplified_pos/static/src/js/PrintPopup.js',
            'simplified_pos/static/src/js/ProductScreenPaymentLine.js',
            'simplified_pos/static/src/js/ProductWidgetSimple.js',
            'simplified_pos/static/src/scss/pos.scss',
            'simplified_pos/static/src/xml/ProductScreen.xml',
            'simplified_pos/static/src/xml/OrderWidget.xml',
            'simplified_pos/static/src/xml/ActionpadWidget.xml',
            'simplified_pos/static/src/xml/ConfirmationPopup.xml',
            'simplified_pos/static/src/xml/PrintPopup.xml',
            'simplified_pos/static/src/xml/PaymentScreenPaymentLine.xml',
            'simplified_pos/static/src/xml/ProductWidgetControlPanel.xml',
            'simplified_pos/static/src/xml/chrome.xml',
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
