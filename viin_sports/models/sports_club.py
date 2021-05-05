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
        default=lambda self: self.env.user,
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
    is_member = fields.Boolean(compute='_check_is_member', string='Check is member')
    has_team = fields.Boolean(compute='_check_has_team', string='Check has member')
    
    
    def _check_is_member(self):
        for r in self:
            if r.env.user in r.member_ids:
                r.is_member = True
            else:
                r.is_member = False
    def _check_has_team(self):
        for r in self:
            if r.env.user.team_ids & r.team_ids:
                r.has_team = True
            else:
                r.has_team = False
    @api.depends('member_ids')
    def _compute_member_count(self):
        for r in self:
            r.member_count = len(r.member_ids)
            
    def action_request_join(self):
        # sau nay se tao ra approval request o day
        for r in self:
            r.member_ids |= self.env.user
            
    def action_leave_club(self):
        for r in self:
            r.member_ids = r.member_ids - self.env.user
            self.env.user.team_ids -= r.team_ids
    def action_leave_team(self):
        for r in self:
            self.env.user.team_ids -= r.team_ids
            
    def action_join_random_team(self):
        for r in self:
            _team_to_join = None
            _lst_team = r.team_ids.sorted(key=lambda team: len(team.member_ids))
            _diff_member_len = abs(len(_lst_team[0].member_ids - _lst_team[-1].member_ids))
            if _diff_member_len >= 3:
                _team_to_join = _lst_team[0] if len(_lst_team[0].member_ids) < len(_lst_team[-1].member_ids) else _lst_team[-1]
            else:
                _min_index = 9999
                for team in r.team_ids:
                    if _min_index > len(team.member_ids):
                        _min_index = len(team.member_ids)
                        _team_to_join = team
            _team_to_join.member_ids |= r.env.user
            
        
            
            
