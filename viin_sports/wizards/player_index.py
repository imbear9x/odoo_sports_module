from odoo import models, fields, api


class PlayerIndex(models.TransientModel):
    _name = 'player_index'
    
    i_power = fields.Integer(string="Power Index",)
    i_speed = fields.Integer(string="Speed Index",)
    i_skill = fields.Integer(string="Skill Index",)
    i_defending = fields.Integer(string="Defending Index",)
    i_general = fields.Integer(string="General Index",readonly=True)
    
    @api.model
    def default_get(self,fields):
        values = super(PlayerIndex, self).default_get(fields)
        values['i_power'] = self.env.user.i_power
        values['i_speed'] = self.env.user.i_speed
        values['i_skill'] = self.env.user.i_skill
        values['i_defending'] = self.env.user.i_defending
        values['i_general'] = self.env.user.i_general
        return values
        
    def update_index_action(self):
        self.env.user.i_power = self.i_power
        self.env.user.i_speed = self.i_speed
        self.env.user.i_skill = self.i_skill
        self.env.user.i_defending = self.i_defending
    