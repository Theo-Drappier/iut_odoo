# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutItOffice(models.Model):
    _name = 'iut.it.office'
    _inherit = 'res.partner'

    employee_nb = fields.Integer('Employee Number', compute='_compute_nb')
    room_ids = fields.One2many(string='Rooms', comodel_name='iut.it.room', inverse_name='office_id')

    @api.depends('room_ids.partner_ids')
    def _compute_nb(self):
        result = 0
        for room_id in self.room_ids:
            result += len(room_id.partner_ids)

        self.employee_nb = result

    @api.depends('is_company', 'parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        pass
