from odoo import models, fields, api
from odoo.exceptions import UserError    

class BudgetHistory(models.Model):
    _name = 'sports.transaction'
    _description = 'Transaction History'
    _spec_name = "title"
    
    title = fields.Char(String= 'Title')
    transaction_time = fields.Date(string='Time', default=fields.Date.today())
    amount = fields.Float(string='Amount',default=0)
    reason = fields.Text(string='Reason')
    pre_amount = fields.Float(string='Pre Amount')
    balance = fields.Float(string='Balance')
    club_id = fields.Many2one(
        string="Club",
        comodel_name="sports.club",
        ondelete="set null",
    )
    tran_type = fields.Selection([
        ('deposit','Deposit'),
        ('withdraw','WithDraw')
    ])
    state = fields.Selection(
        [
        ('draft','draft'),
        ('confirm','confirm'),
        ('done','done')
        ],
        String = 'State',
        default = 'draft' 
    )
    
    

    def cal_club_total_amount(self):
        for r in self:
            old_value = r.club_id.total_balance
            new_value = 0
            if r.tran_type == 'deposit':
                new_value = old_value + r.amount
            else:
                new_value = old_value - r.amount
            r.club_id.write({'total_balance': new_value})
        
    
    def action_approval_tran(self):
        for r in self:
            if r.state == 'confirm':
                r.state = 'done'
                r.cal_club_total_amount()
            else:
                raise UserError('Only transaction with state  is confirm')
            
    def action_confirm_tran(self):
        for r in self:
            if r.state == 'draft':
                r.state = 'confirm'
            else:
                raise UserError('Only transaction with state  is draft')
            
            
            
             