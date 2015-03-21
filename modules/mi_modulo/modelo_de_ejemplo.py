# -*- coding: utf-8 -*-

# OpenERP
import openerp
# Necesario para poder definir nuestro modelo.
from osv import orm, fields
# Utilizaremos el paquete python PDB para debuggear.
import pdb
# Tratando fechas
import datetime
# from datetime import datetime
from tools import DEFAULT_SERVER_DATE_FORMAT as DEF_DATE
from tools import DEFAULT_SERVER_DATETIME_FORMAT as DEF_DATETIME
# Loggers
import logging
_logger = logging.getLogger(__name__)


class modelo_de_ejemplo(orm.Model):
    # Definimos el nombre de nuestro modelo. Recordamos que por convención
    # vamos a llamarlo con el "nombre del modulo"."nombre del modelo"
    _name = 'mi_modulo.modelo_de_ejemplo'

    # Determinamos el campo por el cuál queremos que se ordenen los registros
    # de nuestro modelo.
    _order = "name desc"

    # Por defecto OpenERP muestra el campo name en los campos relacionales, en
    # caso de que queramos que OpenERP muestre otro campo se lo indicaríamos
    # con el atributo _rec_name
    # _rec_name = "otro_name"

    # Definimos las columnas (propiedades) de nuestro objeto (modelo).
    _columns = {
        # Definimos un campo de nombre "name" el tipo es texto, de tamaño
        # máximo 5 carácteres, y al cuál especificamos a OpenERP que tiene que
        # mostrar como label el string "Nombre", por lo que en la interfaz
        # veremos un label "Nombre" seguido de un input text.
        'name': fields.char(string="Name", size=5, change_default=True),

        # Indicamos otro campo de texto.
        'otro_name': fields.char(
            string="Otro Nombre",
            help="Este campo es para ...\n"\
                 "Esta es otra línea",
            translate=True),

        # Boolean
        'active': fields.boolean("Activo"),

        # Integer
        'valor_a': fields.integer('Valor A', required=True),
        'valor_b': fields.integer('Valor B', required=True),
        'valor_c': fields.integer('Valor C', readonly=True, states={
            'draft': [('readonly', False)],
            'selled': [('invisible', True)],
        }),

        # Float
        'float_a': fields.float('Float A', digits=(3,2)),
        'float_b': fields.float('Float B', digits=(1,5)),

        # Text && HTML
        'notes': fields.text('Notas del usuario', required=True),
        'notes_ui': fields.html("Notas para el cliente", required=True),

        # Fechas
        'date_start': fields.date('Fecha inicio'),
        'date_end': fields.date('Fecha fin', readonly=True),

        # Fechas y horas
        'datetime_start': fields.datetime('Fecha y hora inicio'),
        'datetime_end': fields.datetime('Fecha y hora fin'),

        # Fichero, imagen, doc...
        'file': fields.binary('Upload a file'),
        'image': fields.binary('Upload your image', filters="*.png,*.jpg"),

        # Selection - Incluímos el special field "state"
        'state': fields.selection([
                ('draft', 'Borrador'),
                ('confirmed', 'Confirmado'),
                ('selled', 'Vendido'),
                ('cancelled', 'Cancelado'),
            ], string="States")
    }

    def create(self, cr, uid, vals, context=None):
        """
            Aprovechamos para ver una de las formas de documentar los métodos
            en python.
            Al definir este método extendemos del create del ORM, por lo que
            podemos modificar el valor de los parámetros, o realizar cualquier
            tipo de gestión antes/después de crear el registro.

            :param cr: Cursor de la base de datos.
            :param uid: Id del usuario que ejecuta el método, para las
                comprobaciones de seguridad
            :param dict vals: Valores a guardar en el registro que vamos a
            crear.
            :param context: información común del usuario. Puede contener
            valores como el idioma del usuario, y la hora de este.
        """
        # Definimos un breakpoint
        pdb.set_trace()

        if vals['datetime_start'] and vals['datetime_end']:
            self.check_datetime(vals['datetime_start'], vals['datetime_end'])



        # El método create devuelve el id del registro recien creado.
        record_id = super(modelo_de_ejemplo, self).create(
            cr, uid, vals, context=context)

        # Realizamos acciones después de crear el registro.

        # Devolvemos el id del registro.
        return record_id

    def write(self, cr, uid, ids, vals, context=None):
        """
            TODO::
        """
        _logger.info("ids = %r" % (ids))
        _logger.error("vals = %r" % (vals))
        _logger.warning("context = %r" % (context))

        if 'datetime_start' in vals and 'datetime_end' in vals:
            if vals['datetime_start'] and vals['datetime_end']:
                self.check_datetime(
                    vals['datetime_start'],
                    vals['datetime_end']
                )
        return super(modelo_de_ejemplo, self).write(
            cr, uid, ids, vals, context=context)


    def _get_default_name(self, cr, uid, context=None, *args):
        return 'AAAAA'

    def _get_default_date_end(self, cr, uid, context=None, *args):
        today = datetime.datetime.now().date()
        end_date = today + datetime.timedelta(days=5)
        return end_date.strftime(DEF_DATE)

    # Definimos los valores por defecto de los fields anteriormente declarados.
    _defaults = {
        # Podemos definir el valor directamente, on invocando un método.
        # 'name': 'AAAAA'
        # 'name': lambda *a: 'AAAAA',
        'name': _get_default_name,
        'state': 'draft',
        'active': lambda *a: True,
        'date_start': fields.date.today(),
        'date_end': _get_default_date_end,
    }

    def check_datetime(self, datetime_start, datetime_end, context=None):
        """
        Comprobamos la lógica de fechas...
        """
        # 1ro comprobamos que el field datetime_start venga inicializado.
        if datetime_start > datetime_end:
            raise openerp.exceptions.AccessError(
                "Las fechas de 'inicio' no pueden ser posteriores " \
                "a las fechas 'fin'"
            )
        return True

modelo_de_ejemplo()
















