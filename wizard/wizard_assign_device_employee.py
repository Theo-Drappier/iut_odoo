# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AssignDeviceEmployee(models.TransientModel):
    _name = 'wizard.assign.device.employee'

    res_partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    device_ids = fields.Many2many(comodel_name='iut.it.device', string='Devices')

    @api.model
    def default_get(self, fields_list):
        res = super(AssignDeviceEmployee, self).default_get(fields_list)
        res['device_ids'] = self.env.context['active_ids']
        return res

    @api.multi
    def assign_employee(self):
        self.res_partner_id.device_ids += self.device_ids
