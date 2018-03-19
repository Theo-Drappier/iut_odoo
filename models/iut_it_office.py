# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutItOffice(models.Model):
    _name = 'iut.it.office'
    _inherit = 'res.partner'

    employee_nb = fields.Integer('Employee Number', compute='_compute_nb')
    room_ids = fields.One2many(string='Rooms', comodel_name='iut.it.room', inverse_name='office_id')

    @api.depends()
    def _compute_nb(self):
        return True
