from odoo import models, fields, api


class Member(models.Model):
    _description = 'Exte'
    _inherit = 'res.users'

    club_ids = fields.Many2many(
        string="Clubs",
        comodel_name="viin_sports.club",
        relation="club_member_user",
        column1="user_id",
        column2="club_id"
    )
    team_ids = fields.Many2many(
        string="Teams",
        comodel_name="sports.team",
        relation="team_member_user",
        column1="user_id",
        column2="team_id"
    )