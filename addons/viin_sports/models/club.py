# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Club(models.Model):
    _name = 'viin_sports.club'
    _description = 'viin_sports.club'

    club_name = fields.Char(string='Club Name')
    slogan = fields.Char(string='Slogan')
    avatar = fields.Image(string='Avatar', attachment=True)
    publication = fields.Html(string='Publication')
    member_count = fields.Integer(string='Member Count',compute='_compute_member_count',default=0)

    
    presidents = fields.Many2many(
        string="Presidents",
        comodel_name="res.users",
        relation="club_president_user",
        column1="club_id",
        column2="user_id",
        domain="[('club_ids', 'in', id)]",
        default=lambda self: self.env.user
    )
    member_ids = fields.Many2many(
        string="Member",
        comodel_name="res.users",
        relation="club_member_user",
        column1="club_id",
        column2="user_id",
        default=lambda self: self.env.user
    )
    team_ids = fields.One2many(
        'sports.team',
        'club_id',
        string='Teams',
    )

    state = fields.Selection([
        ('offline', 'Offline'),
        ('active', 'Active'),
        ('break', 'Break')],
        string='State',
        default='active')
    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)
