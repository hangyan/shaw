#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Hang Yan'


def car(l):
    """Get first element of list"""
    assert isinstance(l, list)
    return None if not l else l[0]


def cdr(l):
    """Get rest element of list"""
    assert isinstance(l, list)
    return None if not l else l[1:]


def chunks(l, n):
    """Split list l in N-sized chunks"""
    return [l[i:i + n] for i in xrange(0, len(l), n)]
