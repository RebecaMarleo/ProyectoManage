# -*- coding: utf-8 -*-

from odoo import models, fields, api


class history(models.Model):
    _name = 'managerebeca.history'
    _description = 'managerebeca.history'

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripción")

    project_id = fields.Many2one("managerebeca.project", string = "Proyecto", ondelete="set null")
    task_id = fields.One2many(string = "Tarea", comodel_name = "managerebeca.task", inverse_name = "history_id")
    used_technologies = fields.Many2many("managerebeca.technology", compute = "_get_used_technologies")

    def _get_used_technologies(self):
        for history in self:
            technologies = None # Array para concatenar todas las tecnologías. Inicialmente no tiene valor
            for task in history.tasks: # Para cada una de las tareas de la historia
                if not technologies:
                    technologies = task.technologies
                else:
                    technologies = technologies + task.technologies
            history.used_technologies = technologies # Asignar las tecnologías a la historia