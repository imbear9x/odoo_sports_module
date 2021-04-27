
from odoo import models, fields, api


class MemberContribute(models.Model):
    _name = 'viin_sports.member_contribute'
    _description = 'viin_sports.budget_contribute'
    member_id = fields.Many2one(
        string="Member Contribute",
        comodel_name="res.users",
        ondelete="set null",
    )

    state = fields.Boolean(string="State", default=False)
    budget_month_id = fields.Many2one(
        string="Budget Month",
        comodel_name="viin_sports.budget_month",
    )
    offer_amount = fields.Float(string='Offer Amount',compute='_compute_offer_amount',store=True,)
    @api.depends('budget_month_id.club_id')
    def _compute_offer_amount(self):
        for r in self:
            # if not r.offer_amount or r.offer_amount < r.budget_month_id.club_id.
            if not r.offer_amount:
                r.offer_amount = r.budget_month_id.club_id.contributions_convention
            else:
                r.offer_amount = r.offer_amount
