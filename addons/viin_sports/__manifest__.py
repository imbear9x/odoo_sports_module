# -*- coding: utf-8 -*-
{
    'name': "viin_sports",

    'summary': "Management sports clubs",

    'description': "Mô tả hiện đang viết bằng tiếng Việt do chwưa biết cách localizezation",

    'author': "vukhoi1999",
    'website': "https://viindoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'viindoo/Sports',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/main.xml',
        'views/templates.xml',
        'views/clubs.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': ['static/src/css/style.css'],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'installable': True
}
