
from odoo import models, fields, api


class BudgetMonth(models.Model):
    _name = 'viin_sports.budget_month'
    _description = 'viin_sports.budget_month'

    month = fields.Integer(string="Current Month",default=1)
    estimate_budget = fields.Float(string='Estimate Budget',)
    current_amount = fields.Float(string='Current Amount',)
    member_contribute_ids = fields.Many2many(
        string="List Member Contribute",
        comodel_name="viin_sports.member_contribute",
        relation="budget_month_member_contribute_rels",
        column1="month_id",
        column2="member_contribute_id"
    )
    club_id = fields.Many2one('viin_sports.club', string='Of CLub')
