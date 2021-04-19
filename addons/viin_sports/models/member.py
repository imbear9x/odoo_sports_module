# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Member(models.Model):
    _name = 'viin_sports.member'
    _description = 'viin_sports.member'
    _inherits = {'hr.employee': "employee_ids"}

    
