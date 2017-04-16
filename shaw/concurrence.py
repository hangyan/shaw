#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Hang Yan'


def process(items, func):
    from gevent import monkey
    monkey.patch_all()
    from gevent.pool import Pool
    items = [x for x in items if x]
    pool = Pool(len(items))
    result = pool.map(func, items)
    return result
