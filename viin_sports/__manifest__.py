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
        'views/root_menu.xml',
        'wizards/add_contribute_member_view.xml',
        'views/templates.xml',
        'views/sports_team.xml',
        'views/sports_clubs.xml',
        'views/sports_budget_manager.xml',
        'views/sports_contribute.xml',
        'views/sports_transaction.xml',
        
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
