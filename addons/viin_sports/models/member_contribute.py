
from odoo import models, fields, api


class MemberContribute(models.Model):
    _name = 'viin_sports.member_contribute'
    _description = 'viin_sports.budget_contribute'
    member_id = fields.Many2one(
        string="Member Contribute",
        comodel_name="res.users",
        ondelete="set null",
    )
    state = fields.Boolean(string="State",default=False)
    budget_month_ids = fields.Many2many(
        string="Budget Month",
        comodel_name="viin_sports.budget_month",
        relation="budget_month_member_contribute_rels",
        column1="member_contribute_id",
        column2="month_id",
    )
    