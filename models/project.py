# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _name = 'managerebeca.project'
    _description = 'managerebeca.project'

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripción")

    history_ids = fields.One2many(string = "Historia", comodel_name = "managerebeca.history", inverse_name = "project_id")
    sprints_id = fields.One2many(string = "Sprint", comodel_name = "managerebeca.sprint", inverse_name = "project_id")