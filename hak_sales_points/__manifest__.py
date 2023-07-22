# -*- coding: utf-8 -*-
{
    'name': "POS Sales Points",

    'summary': """
            POS Sales Points
        """,

    'description': """
        POS Sales Points
        Add sales point in products it will show the total sales point per order also in order analysis report 
    """,

   'author': "HAK Technologies",
    'website': "http://www.HAKTechnologies.com",
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
