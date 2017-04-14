#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gc

__author__ = 'Hang Yan'


def queryset_iterator(queryset, chunksize=1000):
    '''''
    Iterate over a Django Queryset ordered by the primary key

    This method loads a maximum of chunksize (default: 1000) rows in it's
    memory at the same time while django normally would load all rows in it's
    memory. Using the iterator() method only causes it to not preload all the
    classes.

    Note that the implementation of the iterator does not support ordered query sets.

    Link: https://djangosnippets.org/snippets/1949/
    '''

    pk = 0

    last_pk = queryset.order_by('-pk').values_list('pk', flat=True).first()
    if last_pk is not None:
        queryset = queryset.order_by('pk')
        while pk < last_pk:
            for row in queryset.filter(pk__gt=pk)[:chunksize]:
                pk = row.pk
                yield row
            gc.collect()
