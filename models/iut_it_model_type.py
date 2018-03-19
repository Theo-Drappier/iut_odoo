# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutItModelType(models.Model):
    _name = 'iut.it.model.type'

    name = fields.Char('Name', required=True)
    model_ids = fields.Many2many(string='Models - Types', comodel_name='iut.it.model')

    _sql_constraints = [
        (
            'name_unique',
            'unique(name)',
            'Choose another value - it has to be unique !'
        )
    ]
