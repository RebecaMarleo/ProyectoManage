# -*- coding: utf-8 -*-

from odoo import models, fields, api


class history(models.Model):
    _name = 'managerebeca.history'
    _description = 'managerebeca.history'

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripción")
    # variables de ampliación
    progress = fields.Float(String="Progreso", compute="_get_progress")
    is_favorite = fields.Boolean(default=False) # indica si la tarea es favorita
    # FIN de variables de ampliación

    project_id = fields.Many2one(comodel_name="managerebeca.project", string = "Proyecto", ondelete="set null", inverse_name = "histories_ids")
    tasks_ids = fields.One2many(string = "Tareas", comodel_name = "managerebeca.task", inverse_name = "history_id")
    used_technologies = fields.Many2many("managerebeca.technology", compute = "_get_used_technologies")

    def _get_used_technologies(self):
        for history in self:
            technologies = None # Array para concatenar todas las tecnologías. Inicialmente no tiene valor
            for task in history.tasks_ids: # Para cada una de las tareas de la historia
                if not technologies:
                    technologies = task.technologies_ids
                else:
                    technologies = technologies + task.technologies_ids
            history.used_technologies = technologies # Asignar las tecnologías a la historia

    # funciones de ampliación
    @api.depends('tasks_ids')
    def _get_progress(self):
        for history in self:
            if history.tasks_ids:
                history.progress = (sum(task.progress for task in history.tasks_ids) / len(history.tasks_ids))
            else:
                history.progress = 0
    # FIN de funciones de ampliación