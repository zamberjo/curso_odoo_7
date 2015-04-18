# -*- encoding: utf-8 -*-


{
    'name': 'Open Academy',
    'version': '1.0',
    'author': 'Jose Zambudio Bernabeu',
    'category': 'Courses',
    'description': """
OpenAcademy
===========

Módulo Open Academy para gestionar cursos
-----------------------------------------
- Cursos
- Sesiones
- Registro de asistentes
    """,
    'depends': ['base', 'report_webkit'],
    'data': [
        'security/openacademy_security.xml',
        'security/ir.model.access.csv',
        'views/openacademy_menu.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/partner_view.xml',
        'wizards/subscription_wizard_view.xml',
        'workflows/session_workflow.xml',
        'report/session_report.xml',
    ],
}
