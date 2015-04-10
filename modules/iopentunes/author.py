# -*- coding: utf-8 -*-

from osv import orm, fields


class iopentunes_author(orm.Model):
    _name = 'iopentunes.author'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'active': fields.boolean('Active'),
        'album_ids': fields.many2many(
            'iopentunes.album', 'iopentunes_author_album_rel', 'author_id',
            'album_id', string="Albums"),
        'song_ids': fields.many2many(
            'iopentunes.song', 'iopentunes_author_song_rel', 'author_id',
            'song_id', string="Songs"),
    }

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Author\'s name must be unique!')
    ]

    _defaults = {
        'active': True,
    }

iopentunes_author()
