# -*- coding: utf-8 -*-

from odoo import models, fields, api


class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_dev = fields.Boolean(default = True)

    technologies = fields.Many2many("managerebeca.technology",
                                        relation="developer_technologies",
                                        column1="developer_id",
                                        column2="technologies_id")
    
    @api.model
    def create(self, vals):
        # asegura que el campo is_dev sea True al crear un nuevo desarrollador
        vals['is_dev'] = True
        return super(developer, self).create(vals)