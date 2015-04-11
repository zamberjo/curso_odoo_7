# -*- encoding: utf-8 -*-

from osv import orm, fields


# class openacademy_subscription_wizard(osv.osv_memory):
class openacademy_subscription_wizard(orm.TransientModel):
    _name = 'openacademy.subscription_wizard'

    _columns = {
        'session_ids': fields.many2many(
            'openacademy.session', 'subscription_session_rel',
            'subscription_id', 'session_id', string="Sessions",
            required=True),

        'attendee_ids': fields.one2many(
            'openacademy.attendee_wizard', 'subscription_id',
            string="Attendees"),
    }

    def subscribe(self, cr, uid, ids, context=None):
        session_pool = self.pool.get('openacademy.session')
        wizard_record = self.browse(cr, uid, ids[0], context=context)
        session_ids = []
        for session_record in wizard_record.session_ids:
            session_ids += [session_record.id]

        attendee_data = []
        for attendee_record in wizard_record.attendee_ids:
            attendee_data += [(0, 0, {
                'partner_id': attendee_record.partner_id.id,
            })]

        return session_pool.write(cr, uid, session_ids, {
                'attendee_ids': attendee_data,
            }, context=context)

openacademy_subscription_wizard()


class openacademy_attendee_wizard(orm.TransientModel):
    _name = 'openacademy.attendee_wizard'

    _columns = {
        'subscription_id': fields.many2one(
            'openacademy.subscription_wizard'),
        'partner_id': fields.many2one(
            'res.partner', string="Partner", required=True),
    }

openacademy_attendee_wizard()
