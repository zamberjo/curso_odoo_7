# -*- coding: utf-8 -*-

from osv import orm, fields
import tools


class iopentunes_album(orm.Model):
    _name = 'iopentunes.album'

    def _set_image(self, cr, uid, id, field_name, field_value, arg,
                   context=None):
        return self.write(cr, uid, [id], {
            'image': tools.image_resize_image_big(field_value),
        }, context=context)

    def _get_image(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = tools.image_get_resized_images(
                record.image, avoid_resize_medium=True)
        return res

    _columns = {
        'name': fields.char('Name', size=256, translate=True, required=True),
        'active': fields.boolean('Active'),
        'image': fields.binary(
            string="Image",
            help="This field holds the image used as image for the album, "
                 "limited to 1024x1024px."),
        'image_medium': fields.function(
            _get_image, fnct_inv=_set_image, type="binary", multi="image",
            help="This field holds...128x128px", string="Image", store={
                'iopentunes.album': (
                    lambda self, cr, uid, ids, context: ids, ['image'], 10),
            }),
        'image_small': fields.function(
            _get_image, fnct_inv=_set_image, type="binary", multi="image",
            help="This field holds...64x64px", string="Image", store={
                'iopentunes.album': (
                    lambda self, cr, uid, ids, context: ids, ['image'], 10),
            }),
        'description': fields.text('Description', translate=True),
        'date_published': fields.date('Published date', required=True),
        'format_ids': fields.many2many(
            'iopentunes.album_format', string="Formats", required=True),
        'author_ids': fields.many2many(
            'iopentunes.author', 'iopentunes_author_album_rel', 'album_id',
            'author_id', string="Authors", required=True, ondelete="restrict"),
        'song_ids': fields.one2many(
            'iopentunes.song', 'album_id', string="Songs", required=True),
        'price': fields.float(
            'Sale Price', digits=(3, 2),
            help="Base price to compute the customer price. Sometimes called "
                 "the catalog price."),
        'downloads': fields.integer("Downloads"),
    }

    _sql_constraints = [
        (
            'price',
            'CHECK(price > 0)',
            'Error ! Price must be greater than 0!'
        )
    ]

    _defaults = {
        'active': True,
    }
iopentunes_album()
