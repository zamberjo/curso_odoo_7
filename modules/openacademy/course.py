# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields

import pdb


class openacademy_course(orm.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    _columns = {
        'image': fields.binary(
            string="Image",
            help="This field holds the image used as image for the product, "
                 "limited to 1024x1024px."),
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
