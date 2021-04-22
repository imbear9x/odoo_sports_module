# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Team(models.Model):
    _name = 'viin_sports.team'
    _description = 'viin_sports.team'

    team_name = fields.Char(string="Team name", )

    avatar = fields.Image(
        string='Avatar',
        attachment=True)

    slogan = fields.Char(string='Slogan')

    member_count = fields.Integer(
        string='Member Count',
        compute='_compute_member_count',
        default=0)

    admins = fields.Many2many(
        string="Admins",
        comodel_name="res.users",
        relation="team_admin_user",
        column1="team_id",
        column2="user_id",
        domain="[('team_ids', 'in', id)]",
        default=lambda self: self.env.user
    )
    club_id = fields.Many2one(
        string="Clubs",
        comodel_name="viin_sports.club",
        ondelete="set null",
    )
    member_ids = fields.Many2many(
        string="Members",
        comodel_name="res.users",
        relation="team_member_user",
        column1="team_id",
        column2="user_id",
        domain="[('club_ids', 'in', club_id)]",
        default=lambda self: self.env.user
    )

    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)

    
