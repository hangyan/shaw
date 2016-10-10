#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Hang Yan'

JSON_AC_HEADER = {'Accept': 'application/json'}
JSON_CT_HEADER = {'Content-Type': 'application/json'}
JSON_HEADER = dict(JSON_AC_HEADER.items() + JSON_CT_HEADER.items())

URL_REGEX = '[A-Za-z0-9-_.]+'


def gen_con_list(prefix):
    temp = globals().copy()
    return [temp[x] for x in temp if x.startswith(prefix)]


CURRENCY_RMB = 'RMB'
CURRENCY_USD = 'USD'

CURRENCIES = (
    (CURRENCY_RMB, 'RMB'),
    (CURRENCY_USD, 'USD')
)
