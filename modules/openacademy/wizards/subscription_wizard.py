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
        import pdb
        pdb.set_trace()
        return True

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
