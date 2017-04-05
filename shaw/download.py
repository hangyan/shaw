#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Hang Yan'


def downloads(urls, func):
    from gevent import monkey
    monkey.patch_all()
    from gevent.pool import Pool
    urls = [x for x in urls if x]
    pool = Pool(len(urls))
    result = pool.map(func, urls)
    return result
