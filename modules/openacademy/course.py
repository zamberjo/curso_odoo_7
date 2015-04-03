# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields
# Debugger
import pdb
# Openerp
from openerp import tools


class openacademy_course(orm.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    def _set_image(self, cr, uid, id, field_name, field_value, arg,
                   context=None):
        """
            Método inverseo a _get_image. Ahora nos están guardando el valor en
            los fields image_medium o image_small, por tanto, debemos reescalar
            la imagen (dejándola tal cual en caso de que sea menor que
            1024x1024px) y guardando el valor en image.

            :param int id: ID del registro de este método el cuál ejecuta este
            método para guardar el valor del campo function.
            :param str field_name: Nombre del field el cuál ejecuta este método
            :param field_value: Valor a guardar. Este puede ser de varios tipos
            depende del tipo que contenga el field.
            :param list arg: Lista de argumentos definidos en el
            fields.function
        """
        # Para reescalar la imagen utilizamos el método:
        #   openerp/tools/image.py:96 -> image_resize_image_big
        # Siempre devolvemos un True, al igual que el método write.
        return self.write(cr, uid, [id], {
            'image': tools.image_resize_image_big(field_value),
        }, context=context)

    def _get_image(self, cr, uid, ids, field_name, arg, context=None):
        """
            Método que ejecuta OpenERP para la obtención del valor de un field.
            En nuestro caso como hemos definido un multi, y en el store
            triggers, cuando se activen dichos triggers devolverá el valor a
            todos los fields con el mismo multi (image_medium y image_small).

            :param list ids: Lista de ids de los registros de este modelo el
            cuál hay que obeter el valor de las imágenes mediana y pequeña.
            :param str|list field_name: Nombre del field el cuál ejecuta este
            método. En caso de contener un multi, su valor será una lista de
            str con los nombres de los fields de mismo multi.
            :param list arg: Lista de argumentos definidos en el
            fields.function
        """
        # Para reescalar la imagen utilizamos el método:
        #   openerp/tools/image.py:144 -> image_get_resized_images
        # Tener en cuenta que dicho método nos devuelve un diccionario con
        # clave nombre del campo, y valor la imagen en base64. Por tanto, ya
        # que tenemos un multi y que nuestra función debe devolver un
        # diccionario con ID el del registro y como valor el anterior
        # diccionario, se lo asignamos directamente.
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = tools.image_get_resized_images(
                record.image, avoid_resize_medium=True)
        return res

    _columns = {
        'image': fields.binary(
            string="Image",
            help="This field holds the image used as image for the product, "
                 "limited to 1024x1024px."),

        'image_medium': fields.function(
            _get_image, fnct_inv=_set_image, type="binary", multi="image",
            help="This field holds...128x128px", string="Image", store={
                'openacademy.course': (
                    lambda self, cr, uid, ids, context: ids, ['image'], 10),
            }),

        'image_small': fields.function(
            _get_image, fnct_inv=_set_image, type="binary", multi="image",
            help="This field holds...64x64px", string="Image", store={
                'openacademy.course': (
                    lambda self, cr, uid, ids, context: ids, ['image'], 10),
            }),

        'name': fields.char('Title', size=128, translate=True, required=True),
        'description': fields.text('Description', translate=True),
        'active': fields.boolean('Active'),
        'responsible_id': fields.many2one(
            'res.users', string="Responsible", required=True),
        'responsible_phone': fields.related(
            'responsible_id', 'phone', type="char",
            string="Responsible Phone", store=True),
        'responsible_email': fields.related(
            'responsible_id', 'email', type="char",
            string="Responsible Email", store=True),
        'session_ids': fields.one2many(
            'openacademy.session', 'course_id', string="Sessions"),
        # Comentada en attendee.py, bidireccional.
        # 'attendee_ids': fields.many2many(
        #     'openacademy.attendee', 'course_attendee_rel', 'course_id',
        #     'attendee_id', string='Attendees'),
    }

    def _check_description(self, cr, uid, ids, context=None):
        for course in self.browse(cr, uid, ids, context):
            if course.name == course.description:
                return False
        return True

    _constraints = [
        (
            _check_description,
            'Course title and description must be different',
            ['name', 'description']
        )
    ]

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Course titles must be unique!')
    ]

    def _get_responsible(self, cr, uid, context=None, *a):
        return uid

    _defaults = {
        'active': True,
        # 'responsible_id': lambda self, cr, uid, context, *a: uid,
        'responsible_id': _get_responsible,

    }
openacademy_course()
