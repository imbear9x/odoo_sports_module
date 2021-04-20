# -*- coding: utf-8 -*-

from . import controllers
from . import models
from functools import partial

def uninstall_hook(cr, registry):
    def rem_website_id_null(dbname):
        db_registry = odoo.modules.registry.Registry.new(dbname)
        with api.Environment.manage(), db_registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['ir.model.fields'].search([
                ('name', '=', 'viin_sports_id'),
                ('model', '=', 'res.config.settings'),
            ]).unlink()
    cr.after('commit', partial(rem_website_id_null, cr.dbname))
