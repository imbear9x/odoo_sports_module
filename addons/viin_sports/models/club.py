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
    president = fields.Many2one(
        string="President",
        comodel_name="res.users",
        ondelete="set null",
        default=lambda self: self.env.user.id,
        readonly=True
    )
    member_ids = fields.Many2many(
        string="Member",
        comodel_name="res.users"
    )
    team_ids = fields.One2many(
        'viin_sports.team',
        'club_id',
        string='Teams',
    )
        
    state = fields.Selection([
        ('offline', 'Offline'),
        ('active', 'Active'),
        ('break', 'Break')], string='State',default='active')

    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)