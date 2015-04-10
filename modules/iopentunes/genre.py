# -*- coding: utf-8 -*-

from osv import orm, fields


class iopentunes_genre(orm.Model):
    _name = 'iopentunes.genre'

    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'parent_id': fields.many2one(
            'iopentunes.genre', 'Parent', select=True,
            ondelete='cascade'),
        'child_ids': fields.one2many(
            'iopentunes.genre', 'parent_id', string='Child Genres'),
        'parent_left': fields.integer('Left Parent', select=1),
        'parent_right': fields.integer('Right Parent', select=1),
    }

    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _check_recursion(self, cr, uid, ids, context=None):
        level = 100
        while len(ids):
            cr.execute(
                'select distinct parent_id '
                'from iopentunes_genre '
                'where id IN %s',
                (tuple(ids),)
            )
            ids = filter(None, map(lambda x: x[0], cr.fetchall()))
            if not level:
                return False
            level -= 1
        return True

    _constraints = [
        (
            _check_recursion,
            'Error ! You cannot create recursive genres.',
            ['parent_id']
        )
    ]

iopentunes_genre()
