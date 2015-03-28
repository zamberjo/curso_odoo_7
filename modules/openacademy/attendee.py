# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields


class openacademy_attendee(orm.Model):
    _name = 'openacademy.attendee'
    _description = 'Attendee'
    _rec_name = 'partner_id'

    '''
    def _get_models(self, cr, uid, context=None):
        """
            TODO::
            [
                ...
                ('_name', 'Nuestro modelo'),
                ...
            ]
        """
        return [
            ('openacademy.course', "Cursos"),
            ('openacademy.session', "Sesiones")
        ]
    '''

    _columns = {
        'partner_id': fields.many2one(
            'res.partner', string="Partner", required=True),
        'session_id': fields.many2one(
            'openacademy.session', string="Session", required=True,
            ondelete="cascade"),
        # 'my_reference': fields.reference(
        #     string="Campo reference", selection=_get_models, size=128),
        # 'course_ids': fields.many2many(
        #     'openacademy.course', 'course_attendee_rel',
        #     'attendee_id', 'course_id', string='Cursos'),
    }

openacademy_attendee()
