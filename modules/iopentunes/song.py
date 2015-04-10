# -*- coding: utf-8 -*-

from osv import orm, fields
import openerp.addons.decimal_precision as dp


class iopentunes_song(orm.Model):
    _name = 'iopentunes.song'

    _order = 'downloads desc'

    _columns = {
        'name': fields.char('Title', size=64, required=True, translate=True),
        'active': fields.boolean('Active'),
        'author_ids': fields.many2many(
            'iopentunes.author', 'iopentunes_author_song_rel', 'song_id',
            'author_id', string="Authors", ondelete="restrict", required=True),
        'album_id': fields.many2one(
            'iopentunes.album', string="Album", required=True),
        'image': fields.related(
            'album_id', 'image', type="binary", string="Image", store=False),
        'image_medium': fields.related(
            'album_id', 'image_medium', type="binary", string="Image",
            store=True),
        'image_small': fields.related(
            'album_id', 'image_small', type="binary", string="Image",
            store=False),
        'duration': fields.float(
            "Duration", help="Song duration Minutes : Seconds"),
        'downloads': fields.integer("Downloads"),
        'genre_id': fields.many2one('iopentunes.genre', string='Genre'),
        'price': fields.float(
            'Sale Price', digits=(3, 2),
            help="Base price to compute the customer price. Sometimes called "
                 "the catalog price."),
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
iopentunes_song()
