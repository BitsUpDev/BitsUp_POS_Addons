# -*- coding: utf-8 -*-
{
    'name': 'POS Manual Weight',
    'version': '16.0.1.0.0',
    'category': 'Point of Sale, FM',
    'summary': 'Add Manual Weight for products in POS.',
    'description': """This module will help you to add product weight manually 
                       using weigh scale screen without a weigh machine.""",
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': "https://www.bitsuptech.com",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_weight_manual/static/src/js/**/*.js',
            'pos_weight_manual/static/src/xml/**/*',
        ]
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
