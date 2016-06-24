# -*- coding: utf-8 -*-
{
    'name': "Modulo clientes para Eduardo Camacho",

    'summary': """
        Extender el módulo de clientes
    """,

    'description': """
        Extender el módulo de clientes con campos extras
    """,

    'author': "Vaquero y Charro",
    'website': "http://www.vaqueroycharro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}