# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class IutItOffice(models.Model):
    _name = 'iut.it.office'
    _inherit = 'res.partner'

    employee_nb = fields.Integer('Employee Number', compute='_compute_nb')
    room_ids = fields.One2many(string='Rooms', comodel_name='iut.it.room', inverse_name='office_id')
    device_nb = fields.Integer('Devices Number', compute='_compute_count_devices')

    @api.depends('room_ids.partner_ids')
    @api.multi
    def _compute_nb(self):
        for record in self:
            result = 0
            for room_id in record.room_ids:
                result += len(room_id.partner_ids)

            record.employee_nb = result

    @api.depends('is_company', 'parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        pass

    @api.multi
    def _compute_count_devices(self):
        for record in self:
            result = 0
            for room_id in record.room_ids:
                for partner_id in room_id.partner_ids:
                    result += len(partner_id.device_ids)

            record.device_nb = result

    @api.multi
    def list_devices(self):
        domain = [('res_partner_id.room_id.office_id', '=', self.id)]
        return {
            'name': _('Devices number'),
            'type': 'ir.actions.act_window',
            'res_model': 'iut.it.device',
            'view_id': self.env.ref('iut.view_tree_iut_it_device').id,
            'view_mode': 'tree',
            'view_type': 'form',
            'target': 'new',
            'domain': domain
        }
