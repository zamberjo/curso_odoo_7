# -*- encoding: utf-8 -*-

from osv import orm, fields


# class openacademy_subscription_wizard(osv.osv_memory):
class openacademy_subscription_wizard(orm.TransientModel):
    _name = 'openacademy.subscription_wizard'

    _columns = {
        'course_id': fields.many2one(
            'openacademy.course', string="Course"),
        'session_ids': fields.many2many(
            'openacademy.session', 'subscription_session_rel',
            'subscription_id', 'session_id', string="Sessions",
            required=True),

        'attendee_ids': fields.one2many(
            'openacademy.attendee_wizard', 'subscription_id',
            string="Attendees"),
    }

    def subscribe(self, cr, uid, ids, context=None):
        session_pool = self.pool.get('openacademy.session')
        wizard_record = self.browse(cr, uid, ids[0], context=context)
        session_ids = []
        for session_record in wizard_record.session_ids:
            session_ids += [session_record.id]

        attendee_data = []
        for attendee_record in wizard_record.attendee_ids:
            attendee_data += [(0, 0, {
                'partner_id': attendee_record.partner_id.id,
            })]

        return session_pool.write(cr, uid, session_ids, {
                'attendee_ids': attendee_data,
            }, context=context)

    def onchange_course(self, cr, uid, ids, course_id, context=None):
        """
            Definimos el método a ejecutar por el on_change definido para el
            campo curse_id.

            En este caso por defecto cuando seleccionemos un curso, vamos a
            añadir todas las sesiones asociadas a él. En caso de eliminar el
            curso debe resetear las sesiones y avisar al usuario.

            :param list ids: Lista con el id del registro del cual se ha
            modificado el campo curse_id. Hay que tener en cuenta que puede que
            este valga [], este caso corresponde a un nuevo registro.
            :param int course_id: Parámetro que devuelve el navegador, con el
            valor introducido por el usuario, para operar sobre este.
            :rtype: dict
            :return: diccionario con los valores de los campos a modificar con
            respecto la selección del curso, warnings para el usuario, y domain
            para los campos.
        """
        course_pool = self.pool.get('openacademy.course')

        value = {}
        domain = {}
        warning = {}

        if course_id:
            course_record = course_pool.browse(
                cr, uid, course_id, context=context)

            session_ids = []

            for session_record in course_record.session_ids:
                session_ids += [session_record.id]

            value['session_ids'] = session_ids
            domain['session_ids'] = [
                ('id', 'in', session_ids)
            ]
        else:
            value['session_ids'] = []
            warning = {
                'title': "Warning!",
                'message': "Al borrar el curso se han eliminado todas las "
                           "sesiones contempladas",
            }
        return {
            'value': value,
            'domain': domain,
            'warning': warning,
        }


openacademy_subscription_wizard()


class openacademy_attendee_wizard(orm.TransientModel):
    _name = 'openacademy.attendee_wizard'

    _columns = {
        'subscription_id': fields.many2one(
            'openacademy.subscription_wizard'),
        'partner_id': fields.many2one(
            'res.partner', string="Partner", required=True),
    }

openacademy_attendee_wizard()
