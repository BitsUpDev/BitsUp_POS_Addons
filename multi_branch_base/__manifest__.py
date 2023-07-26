# -*- coding: utf-8 -*-

{
    'name': "Multi Branch Operations",
    'version': "16.0.1.0.1",
    'summary': """ Multiple Branch Unit Operation Setup for All 
                   Modules In Odoo""",
    'description': """Multiple Branch Unit Operation Setup for All 
                      Modules In Odoo, Branch, Branch Operations, 
                      Multiple Branch, Branch Setup""",
    'author': "BitsUp Technologies",
    'company': "BitsUp Technologies",
    'maintainer': "BitsUp Technologies",
    'website': "https://www.bitsuptech.com",
    'category': 'Administration, FM',
    'depends': ['sale_management',
                'sale_stock', 'purchase_stock',
                'stock_account'],
    'data': [
        'security/branch_security.xml',
        'security/ir.model.access.csv',
        'views/res_branch_views.xml',
        'views/branch_product_template_views.xml',
        'views/branch_res_partner_views.xml',
        'views/branch_sale_order_views.xml',
        'views/branch_purchase_order_views.xml',
        'views/branch_res_users_views.xml',
        'views/branch_stock_picking_views.xml',
        'views/branch_account_move_views.xml',
        'views/branch_account_payment_views.xml',
        'views/branch_account_journal.xml',
        'views/branch_account_views.xml',
        'views/branch_stock_warehouse_views.xml',
        'views/branch_report_template.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': False
}
