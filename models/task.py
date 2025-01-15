# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class task(models.Model):
    _name = 'managerebeca.task'
    _description = 'managerebeca.task'

    name = fields.Char(String="Nombre")
    description = fields.Char(String="Descripción")
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    # variables de ampliación
    progress = fields.Float(String="Tiempo transcurrido", compute="_compute_progress", store=True) # guarda el progreso de la tarea
    is_finished = fields.Boolean(String="Está terminada", default=False, store=True) # indica si la tarea ha terminado
    is_favorite = fields.Boolean(default=False) # indica si la tarea es favorita
    state = fields.Selection([
        ('paused', 'En pausa'),
        ('finished', 'Finalizada'),
        ('in_progress', 'En progreso')
    ], default='in_progress', string='Estado', compute="_change_state")
    # FIN de variables de ampliación

    sprint_id = fields.Many2one(comodel_name="managerebeca.sprint", compute = "_get_sprint", store = True, inverse_name="tasks_ids")
    technologies_ids = fields.Many2many(comodel_name = "managerebeca.technology",
                                       relation = "technologies_tasks",
                                       column1 = "technologies_ids",
                                       column2 = "tasks_ids",
                                       string = "Tecnologías",)
    history_id = fields.Many2one(comodel_name="managerebeca.history", ondelete="set null", help="Historia relacionada", inverse_name = "tasks_ids")
    definition_date = fields.Datetime(default=lambda p: datetime.datetime.now())
    project_id = fields.Many2one(comodel_name="managerebeca.project", related = "history_id.project_id", readonly = True)
    code = fields.Char(String = "Código", compute = "_get_code")

    @api.depends('start_date', 'end_date')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['managerebeca.sprint'].search([('project_id', '=', task.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
            if not found:
                task.sprint_id = False

    #@api.one
    def _get_code(self):
        for task in self:
            # try:
                task.code = "TSK_"+str(task.id)
                #_logger.info("Código generado: "+task.code)
            #except:
                #raise ValidationError(_("Generación de código errónea"))

    # funciones de ampliación
    @api.depends('start_date', 'end_date', 'is_finished')
    def _compute_progress(self):
        for task in self:
            if task.start_date and task.end_date:
                total_time = (task.end_date - task.start_date).total_seconds()
                elapsed_time = (datetime.datetime.now() - task.start_date).total_seconds() # tiempo transcurrido
                if total_time > 0:
                    if task.is_finished == False:
                        progress = (elapsed_time / total_time) * 100
                        if progress >= 100:
                            task.progress = 100
                        elif progress <= 0:
                            task.progress = 0
                        else:
                            task.progress = progress
                    else: task.progress = 100
                else:
                    task.progress = 0
            else:
                task.progress = 0

    def f_finish_task(self):
        for task in self:
            task.is_finished = True

    def f_continue_task(self):
        for task in self:
            task.is_finished = False

    @api.depends('is_paused', 'progress')
    def _change_state(self):
        for task in self:
            if task.progress == 100:
                task.state = 'finished'
            elif task.is_paused:
                task.state = 'paused'
            else:
                task.state = 'in_progress'

    # FIN de funciones de ampliación