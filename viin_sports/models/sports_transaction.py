from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import UserError    


class BudgetHistory(models.Model):
    _name = 'sports.transaction'
    _description = 'Transaction History'
    _spec_name = "title"
    
    title = fields.Char(String='Title')
    transaction_time = fields.Datetime(string='Time', default=fields.Datetime.now, readonly=True)
    amount = fields.Float(string='Amount', default=0)
    reason = fields.Text(string='Reason')
    pre_amount = fields.Float(string='Pre Amount')
    balance = fields.Float(string='Balance')
    club_id = fields.Many2one(
        string="Club",
        comodel_name="sports.club",
        ondelete="set null",
    )
    tran_type = fields.Selection([
        ('deposit', 'Deposit'),
        ('withdraw', 'WithDraw')
    ])
    state = fields.Selection(
        [
        ('ready', 'ready'),
        ('done', 'done'),
        ('reject', 'reject'),
        ],
        String='State',
        default='ready' 
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
            if r.state == 'ready':
                r.state = 'done'
                r.cal_club_total_amount()
            else:
                raise UserError('Only transaction with state  is ready')
            
    def action_reject_tran(self):
        for r in self:
            if r.state == 'ready':
                r.state = 'reject'
            else:
                raise UserError('Only transaction with state  is ready')
    
    # def open_contribute(self, cr, uid, ids, context=None):
    #     if context is None:
    #         context = {}
    #     sale_ids = self.pool.get('sports.contribute').search(cr, uid, [('project_id', '=', context.get('search_default_project_id', False)), ('partner_id', 'in', context.get('search_default_partner_id', False))])
    #     names = [record.name for record in self.browse(cr, uid, ids, context=context)]
    #     name = _('Sales Order Lines of %s') % ','.join(names)
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': name,
    #         'view_type': 'form',
    #         'view_mode': 'tree,form',
    #         'context': context,
    #         'domain': [('order_id', 'in', sale_ids)],
    #         'res_model': 'sale.order.line',
    #         'nodestroy': True,
    #     }     
             
