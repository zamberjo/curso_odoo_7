# -*- coding: utf-8 -*-

{
    # Nombre del módulo
    'name' : False,
    # Versión del módulo. Esta versión la adapta al odoo en el que estamos.
    # En nuestro caso 7.0.1.0 -> Ver en release.py 'major_version' line 35
    'version' : '1.0',
    # Breve descripción o palabras clave (keywords)
    'summary': '',
    # Autor del módulo
    'author' : '',
    # Licencia que adopta el módulo.
    'license': 'AGPL-3',
    # Categoría del modulo, esta después lo filtrará openerp en la lista de módulos.
    'category' : 'Uncategorized',
    # Descripción mas extensa del módulo.
    'description' : '',
    # URL de la web del módulo
    'website': '',
    # Dependencias con otros módulos.
    'depends' : [],
    # Lista de XML + CSV + YML que serán instalados/actualizados. --update=module
    'data': [],
    # Listado de datos demo que se introducirarn al instalar/actualizar el módulo en caso de tener
    # activado el flag 'demo' en la creación de la DDBB.
    'demo': [],
    # TODO:: YML que proporcionan YAML test
    'test': [],
    # True or False. Determina si el módulo es instalable o no.
    'installable': True,
    # True or False. En caso de ser verdadero se "auto"instalará en el momento que todas las
    # dependencias estén instaladas. En el caso del módulo web y base, no tienen dependencias y el
    # campo auto_install es True, por lo que nada más crear la DDBB se instalarán los módulos.
    'auto_install': False,
    # En caso de estar activo renombra el anterior valor 'auto_install' con este
    # valor
    'active': True,
    # TODO:
    'application': False,
    # Especificar un path alternativo para el icono del módulo
    'icon': 'static/src/img/icon.png',
    # TODO:
    'post_load': None,
    # TODO:
    'web': False
    # TODO:
    'sequence': 100,
    # TODO:
    'init_xml': [],
    # TODO:
    'update_xml': [],
    # TODO:
    'demo_xml': [],


    # Imágenes para mostrar pantallazos de nuestro módulo en la selección de módulos.
    # http://apps.openerp.com
    'images' : [],
    # TOREVIEW:
    # Listado de XML que van a ser cargados cuando el servicio de Openerp se inicie con el argumento
    # --init=module
    'init': [],
    # Listado de JS y librerías JS que cargaremos en el navegador del cliente.
    'js': [],
    # TODO:: 
    'qweb' : [],
    # Listado de CSS que cargaremos en el navegador del cliente.
    'css':[],
    # True or False. Indica al servidor de Openerp que debe cargar el módulo al iniciar el servicio
    # de Openerp.
    'bootstrap': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
