
from odoo import models, fields, api


class MemberContribute(models.Model):
    _name = 'sports.contribute'
    _description = 'Amount contribute of a member in a club'
    
    user_id = fields.Many2one(
        string="Member Contribute",
        comodel_name="res.users",
        ondelete="set null",
    )

    state = fields.Boolean(string="State", default=False)
    budget_manager_id = fields.Many2one(
        string="Budget Manager",
        comodel_name="sports.budget_manager",
    )
    # def _default_offer_amount(self):
        
    offer_amount = fields.Float(string='Offer Amount',store=True,)
