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
            Método donde especificamos mediante una lista de tuplas los modelos
            de los que podemos almacenar registros (varios many2one).

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
        # Ya que en nuestro ejemplo de la academia no los vamos a utilizar, los
        # dejamos como explicados, y dejo comentado el ejemplo.
        # 'my_reference': fields.reference(
        #     string="Campo reference", selection=_get_models, size=128),

        # Importante para el 2do ejercicio. Varios parámetros:
        #   1) Modelo con el que queremos la relación
        #   2) (Optional) Nombre de la tabla que open utilizará para las
        #       relaciones, entre ambos modelos.
        #   3) Nombre de la columna de la tabla 2) que hace referencia a ESTE
        #       Modelo (openacademy_attendee).
        #   4) Nombre de la columna de la tabla 2) que hace referencia al
        #       modelo con el que tenemos la relación, es decir, 1)
        # 'course_ids': fields.many2many(
        #     'openacademy.course', 'course_attendee_rel',
        #     'attendee_id', 'course_id', string='Cursos'),
    }

openacademy_attendee()
