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
            TODO::
        """
        pdb.set_trace()
        return self.write(cr, uid, [id], {
            'image': tools.image_resize_image_big(field_value),
        }, context=context)

    def _get_image(self, cr, uid, ids, field_name, arg, context=None):
        """
            TODO::
        """
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
                'openacademy.course': (lambda s,cr,u,ids,c: ids, ['image'], 10),
            }),

        'image_small': fields.function(
            _get_image, fnct_inv=_set_image, type="binary", multi="image",
            help="This field holds...64x64px", string="Image", store={
                'openacademy.course': (lambda s,cr,u,ids,c: ids, ['image'], 10),
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
        # 'attendee_ids': fields.many2many(
        #     'openacademy.attendee', 'course_attendee_rel', 'course_id',
        #     'attendee_id', string='Attendees'),
    }

    def _check_description(self, cr, uid, ids, context=None):
        # pdb.set_trace()
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
