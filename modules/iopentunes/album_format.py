# -*- coding: utf-8 -*-

from osv import orm, fields


class iopentunes_album_format(orm.Model):
    _name = 'iopentunes.album_format'
    _order = 'sequence asc'
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'sequence': fields.integer('Sequence'),
    }

    """
    No nos hace falta!
    _defaults = {
        'sequence': 1,
    }
    """

iopentunes_album_format()
