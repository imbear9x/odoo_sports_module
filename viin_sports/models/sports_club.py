# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Club(models.Model):
    _name = 'sports.club'
    _description = 'The club sports in the company'

    name = fields.Char(string='Club Name')
    slogan = fields.Char(string='Slogan')
    avatar = fields.Image(string='Avatar', attachment=True)
    publication = fields.Html(string='Publication')
    member_count = fields.Integer(string='Member Count',compute='_compute_member_count',default=0)

    
    president_ids = fields.Many2many(
        string="Presidents",
        comodel_name="res.users",
        relation="club_president_user_rel",
        column1="club_id",
        column2="user_id",
        domain="[('club_ids', 'in', id)]",
        default=lambda self: self.env.user
    )
    member_ids = fields.Many2many(
        string="Member",
        comodel_name="res.users",
        relation="club_users_rel",
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
    
    total_balance = fields.Float(string='Total Balance',default=0,readonly=True)
    budget_manager_ids = fields.One2many('sports.budget_manager', 'club_id', string='Budget Manager')
    transaction_ids = fields.One2many('sports.transaction', 'club_id', string='Transaction History')
    # Contribute funds: đóng góp quỹ
    # Budget history: Lịch sử
    
    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)
    @api.depends('')
    def _compute_total_balance(self):
        for r in self:
            r.total_balance = 0
