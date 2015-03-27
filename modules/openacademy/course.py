# -*- encoding: utf-8 -*-

# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields


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

    # Esto faltaba!
    _defaults = {
        'active': True
    }
openacademy_course()
