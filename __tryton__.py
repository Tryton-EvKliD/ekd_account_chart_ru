# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Charts of Accounts Russian Standart',
    'name_ru_RU': 'План счетов Российский стандарт',
    'version': '1.8.0',
    'author': 'Dmitry Klimanov',
    'email': 'k-dmitry2@narod.ru',
    'website': 'http://www.delfi2000.ru/',
    'description': '''Chart of Account Russian Standart
''',
    'description_ru_RU': '''План счетов Российский стандарт
''',
    'depends': [
        'ekd_account',
    ],
    'xml': [
         'xml/account_type_ru.xml',
         'xml/account_chart_ru.xml',
    ],
    'translation': [
#        'fr_FR.csv',
    ],
}
