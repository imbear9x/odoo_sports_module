# -*- coding: utf-8 -*-
from odoo import http


class ViinSports(http.Controller):
    @http.route('/viin_sports/viin_sports/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/viin_sports/viin_sports/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('viin_sports.listing', {
            'root': '/viin_sports/viin_sports',
            'objects': http.request.env['viin_sports.viin_sports'].search([]),
        })

    @http.route('/viin_sports/viin_sports/objects/<model("viin_sports.viin_sports"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('viin_sports.object', {
            'object': obj
        })
