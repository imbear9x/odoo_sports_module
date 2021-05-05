from odoo import models, fields, api

from ..utils.calc_index import calc_general_index

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
    # chi so bong da
    i_power = fields.Integer(string="Power Index",default = 50)
    i_speed = fields.Integer(string="Speed Index",default = 50)
    i_skill = fields.Integer(string="Skill Index",default = 50)
    i_defending = fields.Integer(string="Defending Index",default = 50)
    i_general = fields.Integer(string="General",default = 50,compute='_compute_general_index',store=True)
    
    @api.depends('i_power','i_speed','i_skill','i_defending')
    def _compute_general_index(self):
        for r in self:
            r.i_general = calc_general_index(
                                            i_power= r.i_power,
                                            i_speed= r.i_speed,
                                            i_skill= r.i_skill,
                                            i_defending= r.i_defending)
            print('hihihihihihi  ' + str(r.i_general))
    
    
    
    
    
    
    