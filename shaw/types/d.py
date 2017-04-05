#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict

__author__ = 'Hang Yan'


def pop_keys(keys, data):
    """Remove list of keys from data(dict)"""
    _ = [data.pop(x, None) for x in keys]


def merge(x, y):
    "Merge two dict."
    return dict(x.items() + y.items())


def subset(data, keys):
    """Get subset of dict by keys"""
    return {k: data[k] for k in keys}


def check_missing_keys(data, keys):
    """Given a list of keys, find the missing ones"""
    return [key for key in keys if key not in data]


def superdict(arg=()):
    """Recursive defaultdict which can init with other dict """
    def update(obj, arg):
        return obj.update(arg) or obj
    return update(defaultdict(superdict), arg)


def rget(d, key):
    """Recursively get keys from dict, for example:
    'a.b.c' --> d['a']['b']['c'], return None if not exist.
    """
    if not isinstance(d, dict):
        return None
    assert isinstance(key, str) or isinstance(key, list)

    keys = key.split('.') if isinstance(key, str) else key
    cdrs = cdr(keys)
    cars = car(keys)
    return rget(d.get(cars), cdrs) if cdrs else d.get(cars)
