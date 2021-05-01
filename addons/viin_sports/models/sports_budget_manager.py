
from odoo import models, fields, api


class BudgetManager(models.Model):
    _name = 'sports.budget_manager'
    _description = 'Budget month manager'

    name = fields.Char(string="Name", default='January')
    contributions_convention = fields.Float(string='Contributions Convention')# quy uoc moi nguoi se dong bao nhieu
    estimate_amount = fields.Float(
        string='Estimate Amount', compute='_compute_contribute', store=True,)
    real_amount = fields.Float(
        string='Real Amount', compute='_compute_contribute', store=True, default=0)
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
                a = r.contribute_ids.mapped(lambda x: x.offer_amount if x.state else 0)
                r.real_amount = sum(a)
        except:
            print('huhuh')
