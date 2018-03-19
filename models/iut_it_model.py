# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutItModel(models.Model):
    _name = 'iut.it.model'

    name = fields.Char('Name', required=True)
    ref = fields.Char('Reference')
    device_ids = fields.One2many(string='Devices', comodel_name='iut.it.device', inverse_name='model_id')
    type_ids = fields.Many2many(string='Type', comodel_name='iut.it.model.type')
    brand_id = fields.Many2one(string='Brand', comodel_name='iut.it.brand')

    _sql_constraints = [
        (
            'ref_unique',
            'unique(ref)',
            'Choose another value - it has to be unique !'
        )
    ]
