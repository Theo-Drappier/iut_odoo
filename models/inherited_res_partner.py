# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    employee_ref = fields.Char('Employee Reference')
    device_ids = fields.One2many(string='Devices', comodel_name='iut.it.device', inverse_name='res_partner_id')
    room_id = fields.Many2one(string='Room', comodel_name='iut.it.room')

