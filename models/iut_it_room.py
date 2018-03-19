# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutItRoom(models.Model):
    _name = 'iut.it.room'

    name = fields.Char('Name', required=True)
    floor = fields.Char('Floor')
    partner_ids = fields.One2many(string='Partners', comodel_name='res.partner', inverse_name='room_id')
    office_id = fields.Many2one(string='Office', comodel_name='iut.it.office')

    _sql_constraints = [
        (
            'name_unique',
            'unique(name)',
            'Choose another value - it has to be unique !'
        )
    ]
