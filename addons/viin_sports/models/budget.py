
from odoo import models, fields, api


class Budget(models.Model):
    _description = 'viin_sports.budget'
    _inherit = 'viin_sports.club'

    total_balance = fields.Float(string='Total Balance',default=0)
    current_month = fields.Integer(string='Current Month',default=1)
    # Contribute funds: đóng góp quỹ
    
    
    # Budget history: Lịch sử
