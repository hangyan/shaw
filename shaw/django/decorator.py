#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Hang Yan'


def cache_function(length):
    """
    Caches a function, using the function itself as the key, and the return
    value as the value saved. It passes all arguments on to the function, as
    it should.

    The decorator itself takes a length argument, which is the number of
    seconds the cache will keep the result around.

    It will put in a MethodNotFinishedError in the cache while the function is
    processing. This should not matter in most cases, but if the app is using
    threads, you won't be able to get the previous value, and will need to
    wait until the function finishes. If this is not desired behavior, you can
    remove the first two lines after the ``else``.
    """
    def decorator(func):
        def inner_func(*args, **kwargs):
            from django.core.cache import cache

            value = cache.get(func)
            if func in cache:
                return value
            else:
                # This will set a temporary value while ``func`` is being
                # processed. When using threads, this is vital, as otherwise
                # the function can be called several times before it finishes
                # and is put into the cache.
                class MethodNotFinishedError(Exception):
                    pass
                cache.set(func, MethodNotFinishedError(
                    'The function %s has not finished processing yet. This \
value will be replaced when it finishes.' % (func.__name__)
                ), length)
                result = func(*args, **kwargs)
                cache.set(func, result, length)
                return result
        return inner_func
    return decorator
