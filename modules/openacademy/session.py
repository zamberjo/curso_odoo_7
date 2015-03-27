# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields


class openacademy_session(orm.Model):
    _name = 'openacademy.session'
    _description = 'Session'
    _order = 'date_start'

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
        'date_end': fields.function(_get_end_date, type='date', string="End date"),
    }

    _defaults = {
        'active': True,
        'state': 'draft',
        'date_start': fields.date.today(),
    }

openacademy_session()
