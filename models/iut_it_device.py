# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutItDevice(models.Model):
    _name = 'iut.it.device'

    # region Fields Declaration

    name = fields.Char('Name', required=True)
    date_allocation = fields.Date('Allocation Date')
    serial_number = fields.Char('Serial Number', required=True)
    date_purchase = fields.Date('Purcharse Date')
    date_warranty_end = fields.Date('End Warranty Date')
    res_partner_id = fields.Many2one(string='Partner', comodel_name='res.partner')
    model_id = fields.Many2one(string='Model', comodel_name='iut.it.model')
    room_id = fields.Integer(related='res_partner_id.room_id.id', store=True)
    office_id = fields.Integer(related='res_partner_id.room_id.office_id.id', store=True)

    # endregion

    @api.onchange('date_purchase', 'model_id')
    def check_change(self):
        self.date_warranty_end = self.model_id.brand_id.warrantly_delay_month + self.date_purchase
