# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


class IutItBrand(models.Model):
    _name = 'iut.it.brand'

    name = fields.Char('Name', required=True)
    warrantly_delay_month = fields.Integer('Warrantly Delay Month')
    support_phone = fields.Integer('Support Phone')
    model_ids = fields.One2many(string='Models', comodel_name='iut.it.model', inverse_name='brand_id')

    _sql_constraints = [
        (
            'name_unique',
            'unique(name)',
            'Choose another value - it has to be unique !'
        )
    ]

    @api.multi
    def change_date_warranty(self):
        self.ensure_one()
        for model in self.model_ids:
            for device in model.device_ids:
                device.check_change()
