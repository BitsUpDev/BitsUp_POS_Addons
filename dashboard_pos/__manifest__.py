# -*- coding: utf-8 -*-
{
    'name': "POS Dashboard",
    'version': '16.0.1.0.2',
    'summary': """POS Dashboard""",
    'description': """POS Dashboard""",
    'category': 'Point of Sale, FM',
    'author': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'website': "https://www.bitsuptech.com",
    'depends': ['hr', 'point_of_sale'],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [
        'views/dashboard_views.xml'
    ],
     'assets': {
        'web.assets_backend': [
            'dashboard_pos/static/src/xml/pos_dashboard.xml',
            'dashboard_pos/static/src/js/pos_dashboard.js',
            'dashboard_pos/static/src/css/pos_dashboard.css',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}