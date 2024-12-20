# -*- coding: utf-8 -*-

from odoo import models, fields, api


class technology(models.Model):
    _name = 'managerebeca.technology'
    _description = 'managerebeca.technology'

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripción")
    photo = fields.Image(string="Imagen", max_width=200, max_height=200)

    tasks_ids = fields.Many2many(comodel_name = "managerebeca.task",
                                       relation = "technologies_tasks",
                                       column1 = "tasks_ids",
                                       column2 = "technologies_ids")