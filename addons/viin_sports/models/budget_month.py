
from odoo import models, fields, api


class BudgetMonth(models.Model):
    _name = 'viin_sports.budget_month'
    _description = 'viin_sports.budget_month'

    name = fields.Char(string="Name", default='January')
    estimate_amount = fields.Float(
        string='Estimate Amount', compute='_compute_member_contribute', store=True,)
    real_amount = fields.Float(
        string='Real Amount', compute='_compute_member_contribute', store=True, default=0)
    member_contribute_ids = fields.One2many(
        'viin_sports.member_contribute',
        'budget_month_id',
        string="List Member Contribute",
    )
    club_id = fields.Many2one(
        'viin_sports.club',
        string='Of CLub',
    )

    @api.depends('member_contribute_ids')
    def _compute_member_contribute(self):
        for r in self:
            r.estimate_amount = sum(
                r.member_contribute_ids.mapped('offer_amount'))
            r.real_amount = sum(r.member_contribute_ids.mapped(lambda x: x.offer_amount if x.state != False else 0))
