
from odoo import models, fields, api


class Budget(models.Model):
    _description = 'viin_sports.budget'
    _inherit = 'viin_sports.club'

    contributions_convention = fields.Float(string='Monthly Contributions')# quy uoc moi nguoi se dong bao nhieu
    total_balance = fields.Float(string='Total Balance',default=0)
    budget_month_ids = fields.One2many('viin_sports.budget_month', 'club_id', string='Budget Month')
    budget_history_ids = fields.One2many('viin_sports.budget_history', 'club_id', string='Budget History')
    # Contribute funds: đóng góp quỹ
    # Budget history: Lịch sử
