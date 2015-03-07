# -*- coding: utf-8 -*-

# Necesario para poder definir nuestro modelo.
from osv import orm, fields
# Utilizaremos el paquete python PDB para debuggear.
import pdb


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
    _rec_name = "otro_name"

    # Definimos las columnas (propiedades) de nuestro objeto (modelo).
    _columns = {
        # Definimos un campo de nombre "name" el tipo es texto, de tamaño
        # máximo 5 carácteres, y al cuál especificamos a OpenERP que tiene que
        # mostrar como label el string "Nombre", por lo que en la interfaz
        # veremos un label "Nombre" seguido de un input text.
        'name': fields.char(string="Nombre", size=5),

        # Indicamos otro campo de texto.
        'otro_name': fields.char(string="Nombre", size=5),
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

        # Realizamos acciones antes de crear el registro.

        # El método create devuelve el id del registro recien creado.
        record_id = super(modelo_de_ejemplo, self).create(
            cr, uid, vals, context=context)

        # Realizamos acciones después de crear el registro.

        # Devolvemos el id del registro.
        return record_id

    def _get_default_name(self, cr, uid, context=None, *args):
        return 'AAAAA'

    # Definimos los valores por defecto de los fields anteriormente declarados.
    _defaults = {
        # Podemos definir el valor directamente, on invocando un método.
        # 'name': 'AAAAA'
        # 'name': lambda *a: 'AAAAA',
        'name': _get_default_name,
    }

modelo_de_ejemplo()
