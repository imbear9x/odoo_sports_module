# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Clubs(models.Model):
    _name = 'viin_sports.clubs'
    _description = 'viin_sports.clubs'

    club_name = fields.Char(string='Club Name')
    slogan = fields.Text(string='Slogan')
    avatar = fields.Image(string='Avatar',attachment=True)
    publication = fields.Html(string = 'Publication')
    
