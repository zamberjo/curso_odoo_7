# -*- coding: utf-8 -*-

{
    'name': 'Mi ejemplo',
    'version': '1.0',
    'summary': 'Breve explicación',
    'author': 'Jose Zambudio',
    'license': 'AGPL-3',
    'category': 'Uncategorized',
    # Como vimos en clase, en la descripción podemos añadir una descripción más
    # extensa de nuestro módulo OpenERP utilizando reStructuredText.
    # Os dejo la documentación:
    # ~ http://docutils.sourceforge.net/rst.html
    'description': '''
Este es mi módulo de ejemplo
============================

Esto es un subtitulo
--------------------

* item 1
* item 2
''',
    # Para este módulo de ejemplo no vamos a heredar por lo que no vamos a
    # depender de nada.
    'depends': [],
    'data': [
        'views/modelo_de_ejemplo_view.xml',
    ],
    'installable': True,
    'active': True,
    'js': [],
    'qweb': [],
    'css': [],
}
