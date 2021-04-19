# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Club(models.Model):
    _name = 'viin_sports.club'
    _description = 'viin_sports.club'

    club_name = fields.Char(string='Club Name')
    slogan = fields.Text(string='Slogan')
    avatar = fields.Image(string='Avatar',attachment=True)
    publication = fields.Html(string = 'Publication')
    member_ids = fields.Many2many(
        string="Member",
        comodel_name="hr.employee"
    )
    
