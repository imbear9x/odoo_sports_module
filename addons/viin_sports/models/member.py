from odoo import models, fields, api


class Member(models.Model):
    _description = 'viin_sports.member_inherit_res_users'
    _inherit = 'res.users'

    club_ids = fields.Many2many(
        string="Clubs",
        comodel_name="viin_sports.club",
    )