# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "POS Bag Charges in Odoo",
    "version": "16.0.0.0",
    "category": "Point of Sale",
    "depends": ['base', 'sale', 'point_of_sale'],
    "author": "BrowseInfo",
    'summary': 'add POS bag Charges on POS order POS Bag Charges pos charges on Bag pos packing charges extra bag charges on pos bag charge POS carry bag charges POS bag amount point of sale bag charges point of sale extra bag charges on pos extra charges on point of sale',
    "description": """
    
    Purpose :- 
This Module allow us to add bag charges on particular order.
    POS bag changes
    POS carry bag
    POS bag amount
    POS bag extra changes
    POS bag extra payment
    Point of sale  bag changes
    Point of sale  carry bag
    Point of sale  bag amount
    Point of sale  bag extra changes
    Point of sale  bag extra payment
    
    """,
    "website": "https://www.browseinfo.in",

    "currency": "EUR",
    "data": [
        'data/data.xml',
        'views/custom_pos_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_bag_charges/static/src/js/pos_bag_charges.js',
            'pos_bag_charges/static/src/js/PosBagPopupWidget.js',
            'pos_bag_charges/static/src/xml/pos_bag_charges.xml',
        ],
    },
    "auto_install": False,
    "installable": True,
    "images": ['static/description/Banner.gif'],
    "live_test_url": 'https://youtu.be/sH8p2Id64fk',
    'license': 'OPL-1',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
