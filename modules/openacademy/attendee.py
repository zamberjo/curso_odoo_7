# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields


class openacademy_attendee(orm.Model):
    _name = 'openacademy.attendee'
    _description = 'Attendee'
    _columns = {
        'partner_id': fields.many2one(
            'res.partner', string="Partner", required=True),
        'session_id': fields.many2one(
            'openacademy.session', string="Session", required=True,
            ondelete="cascade"),
    }

openacademy_attendee()
