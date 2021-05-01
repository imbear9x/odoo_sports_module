
from odoo import models, fields, api


class MemberContribute(models.Model):
    _name = 'sports.contribute'
    _description = 'Amount contribute of a member in a club'
    
    member_id = fields.Many2one(
        string="Member Contribute",
        comodel_name="res.users",
        ondelete="set null",
    )

    state = fields.Boolean(string="State", default=False)
    budget_manager_id = fields.Many2one(
        string="Budget Manager",
        comodel_name="sports.budget_manager",
    )
    offer_amount = fields.Float(string='Offer Amount',related='budget_manager_id.contributions_convention',store=True,)
