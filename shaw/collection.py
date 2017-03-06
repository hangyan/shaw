#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict

__author__ = 'Hang Yan'


def chunks(l, n):
    """Split list l in N-sized chunks"""
    return [l[i:i + n] for i in xrange(0, len(l), n)]


def pop_keys(keys, data):
    """Remove list of keys from data(dict)"""
    [data.pop(x, None) for x in keys]


def merge_dict(x, y):
    return dict(x.items() + y.items())


def sub_dict(data, keys):
    return {k: data[k] for k in keys}


def comp_dict_list(x, y):
    """Compare two list of dicts.

    Note:
        1. If the values are mutable, don't use this function.
        2. The list will be sorted.
        3. No empty list allowed.
    """
    if len(x) != len(y) or not x or not y:
        return False
    xs = sorted(x)
    yx = sorted(y)
    for idx, val in enumerate(xs):
        if cmp(val, yx[idx]) != 0:
            return False
    return True


def check_missing_keys(data, keys):
    return [key for key in keys if key not in data]


def superdict(arg=()):
    """recursive defaultdict which can init with other dict """
    update = lambda obj, arg: obj.update(arg) or obj  # noqa
    return update(defaultdict(superdict), arg)
