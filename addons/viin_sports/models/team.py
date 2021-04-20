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
    member_ids = fields.Many2many(
        string="Members",
        comodel_name="res.users",
        domain="[('club_ids', 'in', club_id)]",
    )

    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)

    @api.model
    def _default_club(self):
        parent_club_id = self.env.context.get('default_id')
        if parent_club_id:
            parent_obj = self.env['viin_sports.club'].browse(parent_club_id)
            return parent_obj
    club_id = fields.Many2one(
        string="Clubs",
        comodel_name="viin_sports.club",
        ondelete="set null",
        default=_default_club
    )

    
