# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class sprint(models.Model):
    _name = 'managerebeca.sprint'
    _description = 'managerebeca.sprint'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")   
    duration = fields.Integer(default = 15)
    start_date = fields.Datetime(string="Fecha inicio")    
    end_date = fields.Datetime(string="Fecha fin", compute="_get_end_date", store=True)

    tasks_ids = fields.One2many(string = "Tareas", comodel_name = "managerebeca.task", inverse_name = "sprint_id")
    project_id = fields.Many2one("managerebeca.project")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            #try:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date