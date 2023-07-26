# -*- coding: utf-8 -*-

{
    'name': 'POS Service Charges',
    'version': '16.0.1.0.0',
    'category': 'Point Of Sale, FM',
    'summary': 'Allows you to set service charges.',
    'description': 'Allows you to set service charges for an order by globally and session wise.',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'images': ['static/description/banner.png'],
    'website': 'https://www.bitsuptech.com',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_config_settings.xml',
        'views/pos_config.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'service_charges_pos/static/src/js/pos_load_data.js',
            'service_charges_pos/static/src/js/service_charge_button.js',
            'service_charges_pos/static/src/xml/ServiceChargeButton.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,

}
