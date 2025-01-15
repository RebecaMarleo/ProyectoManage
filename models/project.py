# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _name = 'managerebeca.project'
    _description = 'managerebeca.project'

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripción")
    # variables de ampliación
    progress = fields.Float(String="Progreso", compute="_get_progress")
    is_favorite = fields.Boolean(default=False) # indica si la tarea es favorita
    # FIN de variables de ampliación

    histories_ids = fields.One2many("managerebeca.history", string = "Historia", inverse_name = "project_id")
    sprints_ids = fields.One2many(comodel_name = "managerebeca.sprint", inverse_name = "project_id", string = "Sprint")

    # funciones de ampliación
    @api.depends('histories_ids', 'sprints_ids')
    def _get_progress(self):
        for project in self:
            if project.histories_ids and project.sprints_ids:
                project.progress = ((sum(history.progress for history in project.histories_ids) + sum(sprint.progress for sprint in project.sprints_ids)) / (len(project.histories_ids) + len(project.sprints_ids)))
            elif project.histories_ids and not project.sprints_ids:
                project.progress = (sum(history.progress for history in project.histories_ids) / len(project.histories_ids))
            elif project.sprints_ids and not project.histories_ids:
                project.progress = (sum(sprint.progress for sprint in project.sprints_ids) / len(project.sprints_ids))
            else:
                project.progress = 0
    # FIN de funciones de ampliación