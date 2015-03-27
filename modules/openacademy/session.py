# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields


class openacademy_session(orm.Model):
    _name = 'openacademy.session'
    _description = 'Session'
    _order = 'date_start'
    _date_name = 'date_start'

    _columns = {
        'name': fields.char('Title', size=128, required=True),
        'date_start': fields.date('Start Date'),
        'duration': fields.float('Duration', help='Duration in days'),
        'seats': fields.integer('Number of Seats'),
        'active': fields.boolean('Active'),
        'state': fields.selection(
            [
                ('draft', 'Draft'),
                ('confirmed', 'Confirmed'),
                ('done', 'Done')
            ], string='State', required=True, readonly=True),
        'course_id': fields.many2one(
            'openacademy.course', string="Course", required=True),
        'intructor_id': fields.many2one(
            'res.partner', string="Instructor",
            domain="[('is_company', '=', False)]"),
    }

    _defaults = {
        'active': True,
        'state': 'draft',
        'date_start': fields.date.today(),
    }

openacademy_session()
