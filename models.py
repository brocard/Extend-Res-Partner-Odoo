# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_partner(models.Model):

    _inherit = 'res.partner'

    nro_supplier = fields.Char(string='N°', size=10)
    nro_phone = fields.Char(string='Teléfono', size=15)
    nro_phone_1 = fields.Char(string='Teléfono', size=15)
    nro_mobile = fields.Char(string='Celular', size=15)

    plazo = fields.Integer(string='Plazo', size=10)
