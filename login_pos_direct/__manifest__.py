# -*- coding: utf-8 -*-

{
    'name': 'POS Direct Login',
    'version': '16.0.1.0.0',
    'category': 'Point of Sale, FM',
    'summary': 'Helps to directly login to POS.',
    'description': 'Log in to configured POS shop to save time without backend.',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': 'https://www.bitsuptech.com',
    'license': 'AGPL-3',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_users_views.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
