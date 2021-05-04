from odoo import models, fields, api


class ContributeMemeber(models.TransientModel):
    _name = 'add_contribute_member'

    user_ids = fields.Many2many(string='User',comodel_name='res.users')
    
    def action_add_member(self):
        _manager_id = self.env.context['active_id'] # selected manager id
        _budget_manager = self.env["sports.budget_manager"].browse(_manager_id)
        _contribute_datas = []
        for user_id in self.user_ids:
            data = {
                'user_id': user_id.id,
                'state': False,
                'budget_manager_id': _manager_id,
                'offer_amount': _budget_manager.person_contribute
            }
            _contribute_datas.append(data)
        
        self.env['sports.contribute'].create(_contribute_datas)