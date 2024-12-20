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

    sprint_id = fields.Many2one("managerebeca.sprint", compute = "_get_sprint", store = True)
    technologies_ids = fields.Many2many(comodel_name = "managerebeca.technology",
                                       relation = "technologies_tasks",
                                       column1 = "technologies_ids",
                                       column2 = "tasks_ids",
                                       string = "Tecnologías",)
    history_id = fields.Many2one("managerebeca.history", ondelete="set null", help="Historia relacionada")
    definition_date = fields.Datetime(default=lambda p: datetime.datetime.now())
    project_id = fields.Many2one("managerebeca.project", related = "history_id.project_id", readonly = True)
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