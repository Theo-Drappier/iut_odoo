# -*- coding: utf-8 -*-
{
    'name': "IUT",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Théo DRAPPIER",
    'website': "http://www.theodrappier.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/tdsimodel_security.xml',
        'views/brand_view.xml',
        'views/device_view.xml',
        'views/model_view.xml',
        'views/model_type_view.xml',
        'views/office_view.xml',
        'views/room_view.xml',
        'views/inherited_res_partner_view.xml',
        'datas/datas.xml',
        'iut_menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
