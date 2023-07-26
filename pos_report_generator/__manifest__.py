# -*- coding: utf-8 -*-

{
    'name': 'POS All in One Report Generator',
    'version': '16.0.1.0.0',
    'summary': "Dynamic Point Of Sale Report Maker",
    'description': "Dynamic Point Of Sale Report Maker",
    'category': 'Point of Sale, FM',
    'author': 'BitsUp Technologies',
    'maintainer': 'BitsUp Technologies',
    'company': 'BitsUp Technologies',
    'website': 'https://www.bitsuptech.com',
    'depends': [
                'point_of_sale',
                'stock',
                'web'
                ],
    'data': [
            'security/ir.model.access.csv',
            'report/pos_order_report.xml',
            'views/pos_report.xml',
            ],
    'assets': {
        'web.assets_backend': [
            'pos_report_generator/static/src/js/action_manager.js',
            'pos_report_generator/static/src/js/pos_report.js',
            'pos_report_generator/static/src/css/pos_report.css',
            'pos_report_generator/static/src/xml/pos_report_view.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'auto_install': False,
}
