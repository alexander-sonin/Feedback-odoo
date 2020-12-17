# -*- coding: utf-8 -*-

from odoo import models, fields, api


class feedback(models.Model):
    _name = 'feedback.feedback'
    _description = 'feedback.feedback'

    title = fields.Char(required=True)
    user_name = fields.Char(required=True)
    user_email = fields.Char(required=True)
    message = fields.Text(required=True)
