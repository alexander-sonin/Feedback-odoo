# -*- coding: utf-8 -*-
from odoo import http


class Feedback(http.Controller):
    @http.route('/feedback/feedback/', auth='public')
    def index(self, **kw):
        return "Test"

    @http.route('/feedback/feedback/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('feedback.listing', {
            'root': '/feedback/feedback',
            'objects': http.request.env['feedback.feedback'].search([]),
        })

    @http.route('/feedback/feedback/objects/<model("feedback.feedback"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('feedback.object', {
            'object': obj
        })
