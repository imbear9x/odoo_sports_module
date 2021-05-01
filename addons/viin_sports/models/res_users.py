from odoo import models, fields, api


class Member(models.Model):
    _description = 'Extend res.users model'
    _inherit = 'res.users'

    club_ids = fields.Many2many(
        string="Clubs",
        comodel_name="sports.club",
        relation="club_users_rel",
        column1="user_id",
        column2="club_id"
    )
    team_ids = fields.Many2many(
        string="Teams",
        comodel_name="sports.team",
        relation="team_users_rel",
        column1="user_id",
        column2="team_id"
    )