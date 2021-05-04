
from odoo import models, fields, api


class BudgetManager(models.Model):
    _name = 'sports.budget_manager'
    _description = 'Budget month manager'

    name = fields.Char(string="Name", default='January')
    person_contribute = fields.Float(string="Person's contribute")# quy uoc moi nguoi se dong bao nhieu
    estimate_amount = fields.Float(
        string='Estimate Amount', compute='_compute_contribute', store=True,)
    real_amount = fields.Float(
        string='Real Amount', compute='_compute_contribute', store=True)
    state = fields.Selection(
        [
        ('ready','ready'),
        ('active','active'),
        ('finish','finish'),
        ],
        default='ready',
        String = 'State'
    )
    # state = fields.Boolean(string= 'State',default=False)
    contribute_ids = fields.One2many(
        'sports.contribute',
        'budget_manager_id',
        string="List Contribute",
    )
    club_id = fields.Many2one(
        'sports.club',
        string='CLub',
    )
    

    @api.depends('contribute_ids')
    def _compute_contribute(self):
        try:
            for r in self:
                r.estimate_amount = sum(
                    r.contribute_ids.mapped('offer_amount'))
                _offer_amounts = r.contribute_ids.mapped(lambda x: x.offer_amount if x.state else 0)
                r.real_amount = sum(_offer_amounts)
        except Exception as e:
            print(e)
            
    def action_active_state(self):
        for r in self:
            if r.state == 'ready':
                r.state = 'active'
            else:
                raise UserError('Only with state  is ready')
    def action_finish_state(self):
        for r in self:
            if r.state == 'active':
                r.state = 'finish'
            else:
                raise UserError('Only with state  is active')
                
            
            