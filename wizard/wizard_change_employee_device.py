# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ChangeEmployeeDevice(models.TransientModel):
    _name = "wizard.employee.device"

    res_partner_id_1 = fields.Many2one(comodel_name='res.partner')
    res_partner_id_2 = fields.Many2one(comodel_name='res.partner')

    @api.model
    def default_get(self, fields_list):
        res = super(ChangeEmployeeDevice, self).default_get(fields_list)
        test = self.env.context
        # res['res_partner_id_1'] = self.env.context['active_ids']
        return res

    @api.multi
    def next_step(self):
        view_id = self.env['ir.model.data'].get_object_reference('iut', 'wizard_change_employee_device_confirm_form')
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'view_id': view_id[1],
            'target': 'new',
            'res_model': 'wizard.assign.device.employee'
        }

    @api.multi
    def change_employee(self):
        self.res_partner_id_2.device_ids += self.res_partner_id_1.device_ids
        self.res_partner_id_1.device_ids.unlink_partner_devices()
