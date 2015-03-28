# -*- encoding: utf-8 -*-

# Debugger
import pdb
# Necesario para definir los modelos de nuestro módulo OpenERP y sus fields.
from osv import orm, fields
# Fechas
import datetime
from tools import DEFAULT_SERVER_DATE_FORMAT as DEF_DATE


class openacademy_session(orm.Model):
    _name = 'openacademy.session'
    _description = 'Session'
    _order = 'date_start'
    _date_name = 'date_start'

    def _search_by_taken_seats(self, cr, uid, model, field_name, criterion,
                               context=None):
        """
            TODO::
        """
        # pdb.set_trace()
        session_ids = self.search(cr, uid, [])
        session_ids_founded = []
        for criteria in criterion:
            for record in self.browse(cr, uid, session_ids, context=context):
                if criteria[0] == 'taken_seats_pct':
                    if criteria[1] == '=':
                        if criteria[2] == record.taken_seats_pct:
                            session_ids_founded += [record.id]
                    elif criteria[1] == '>=':
                        if criteria[2] >= record.taken_seats_pct:
                            session_ids_founded += [record.id]
                    elif criteria[1] == '<=':
                        if criteria[2] >= record.taken_seats_pct:
                            session_ids_founded += [record.id]
        return [('id', 'in', session_ids_founded)]

    def _get_taken_seats_pct(self, cr, uid, ids, field_name, args,
                             context=None):
        """
            TODO::
        """
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = record.seats \
                and 100.0 * len(record.attendee_ids) / record.seats
        return res

    def _get_date_end(self, cr, uid, ids, field_name, args, context=None):
        """
            TODO::
            :param list ids: Lista de ID de los registros del modelo.

        """
        # pdb.set_trace()
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            if record.date_start:
                date_start_datetime = datetime.datetime.strptime(
                    record.date_start, DEF_DATE)

                if record.duration:
                    days = datetime.timedelta(record.duration, seconds=-1)
                    date_end = date_start_datetime + days
                else:
                    date_end = date_start_datetime

                res[record.id] = date_end.strftime(DEF_DATE)
        return res

    _columns = {
        'name': fields.char('Title', size=128, required=True),
        'date_start': fields.date('Start Date'),
        'date_end': fields.function(
            _get_date_end, type="date", string="End date", store=True),
        'duration': fields.float('Duration', help='Duration in days'),
        'seats': fields.integer('Number of Seats'),


        'taken_seats_pct': fields.function(
            _get_taken_seats_pct, type="float",
            fnct_search=_search_by_taken_seats,
            string="Taken Seats",
            help="Percentage of taken seats"),



        'active': fields.boolean('Active'),
        'state': fields.selection(
            [
                ('draft', 'Draft'),
                ('confirmed', 'Confirmed'),
                ('done', 'Done')
            ], string='State', required=True, readonly=True),
        'course_id': fields.many2one(
            'openacademy.course', string="Course", required=True),
        'instructor_id': fields.many2one(
            'res.partner', string="Instructor",
            domain="[('is_company', '=', False)]"),
        'attendee_ids': fields.one2many(
            'openacademy.attendee', 'session_id', string="Attendees")
    }

    _defaults = {
        'active': True,
        'state': 'draft',
        'date_start': fields.date.today(),
    }

openacademy_session()
