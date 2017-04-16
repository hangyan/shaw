#!/usr/bin/env python
# -*- coding: utf-8 -*-


import copy
import pickle
from collections import defaultdict

from shaw.types.l import car, cdr

__author__ = 'Hang Yan'


def pop_keys(keys, data):
    """Remove list of keys from data(dict)"""
    [data.pop(x, None) for x in keys]


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


def deepcopy(data):
    """Use pickle to do deep_copy"""
    try:
        return pickle.loads(pickle.dumps(data))
    except TypeError:
        return copy.deepcopy(data)


def deepcp(data):
    """Use ujson to do deep_copy"""
    import ujson
    try:
        return ujson.loads(ujson.dumps(data))
    except Exception:
        return copy.deepcopy(data)


def tree():
    """Simple version of superdict, no support for dict init.

    see: https://gist.github.com/hrldcpr/2012250
    """
    return defaultdict(tree)


class Tree(dict):
    """See: https://en.wikipedia.org/wiki/Autovivification"""

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
