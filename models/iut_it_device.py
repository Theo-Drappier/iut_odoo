# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class IutItDevice(models.Model):
    _name = 'iut.it.device'

    # region Fields Declaration

    name = fields.Char('Name', required=True)
    date_allocation = fields.Date('Allocation Date')
    serial_number = fields.Char('Serial Number', required=True)
    date_purchase = fields.Date('Purcharse Date', default=datetime.datetime.today())
    date_warranty_end = fields.Date('End Warranty Date')
    res_partner_id = fields.Many2one(string='Partner', comodel_name='res.partner')
    model_id = fields.Many2one(string='Model', comodel_name='iut.it.model')
    room_id = fields.Integer(related='res_partner_id.room_id.id', store=True, string="Room")
    office_id = fields.Integer(related='res_partner_id.room_id.office_id.id', store=True, string='Office')

    _sql_constraints = [
        (
            'serial_number_unique',
            'unique(serial_number)',
            'There is already a device with the Serial Number given !'
        )
    ]
    # endregion

    @api.onchange('date_purchase', 'model_id')
    def check_change(self):
        self.date_warranty_end = (datetime.datetime.strptime(self.date_purchase, '%Y-%m-%d') +
                                  datetime.timedelta(self.model_id.brand_id.warrantly_delay_month * 365 / 12)).strftime('%Y-%m-%d')
