# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_partner(models.Model):

    _inherit = 'res.partner'

    nro = fields.Char('Nro', help('Nro'))
