# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Team(models.Model):
    _name = 'sports.team'
    _description = 'The team in a club sports'

    name = fields.Char(string="Team Name", )

    avatar = fields.Image(
        string='Avatar',
        attachment=True)

    slogan = fields.Char(string='Slogan')

    member_count = fields.Integer(
        string='Member Count',
        compute='_compute_member_count',
        default=0)

    admin_ids = fields.Many2many(
        string="Admins",
        comodel_name="res.users",
        relation="team_admin_users_rel",
        column1="team_id",
        column2="user_id",
        domain="[('team_ids', 'in', id)]",
        default=lambda self: self.env.user
    )
    member_ids = fields.Many2many(
        string="Members",
        comodel_name="res.users",
        relation="team_users_rel",
        column1="team_id",
        column2="user_id",
        domain="[('club_ids', 'in', club_id)]",
        default=lambda self: self.env.user
    )
    club_id = fields.Many2one(
        string="Clubs",
        comodel_name="sports.club",
        ondelete="cascade"
    )
    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)

    
