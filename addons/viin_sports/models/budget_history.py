
from odoo import models, fields, api


class BudgetHistory(models.Model):
    _name = 'viin_sports.budget_history'
    _description = 'viin_sports.budget_history'

    transaction_time = fields.Date(string='Time', default=fields.Date.today())
    amount = fields.Float(string='Amount',default=0)
    reason = fields.Char(string='Reason')
    pre_amount = fields.Float(string='Pre Amount')
    balance = fields.Float(string='Balance')
    # Contribute funds: đóng góp quỹ
    
    
    # Budget history: Lịch sử
