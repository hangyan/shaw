#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import logging

__author__ = 'Hang Yan'

LOG = logging.getLogger(__name__)


def json_response(data, status=200):
    """Return a JsonResponse. Make sure you have django installed first."""
    from django.http import JsonResponse
    return JsonResponse(data=data, status=status, safe=isinstance(data, dict))


def empty_response():
    """Return 204 no content response. Make sure you have django installed first."""
    from django.http import HttpResponse
    return HttpResponse(status=204)


def error_response(message, status=400, code=None):
    """"Return error message(in dict)."""
    from django.http import JsonResponse
    data = {'message': message}
    if code:
        data['code'] = code
    LOG.error("Error response, status code is : {} | {}".format(status, data))
    return JsonResponse(data=data, status=status)


def is_success(response):
    if 200 <= response.status_code < 300:
        return True
    return False


def basic_auth_header(username, password):
    auth = base64.encodestring('{}:{}'.format(username, password))
    return {'Authorization': 'Basic {}'.format(auth.strip())}


def token_auth_header(token, prefix='Token'):
    return {'Authorization': '{} {}'.format(prefix, token)}


def ping(saying='Hold the door!'):
    """Return a callable for ping api. Make sure you have django installed first.

    Args:
        saying: hello world.

    Usage:
        url(r^ping/?$', ping())
    """
    from django.http import HttpResponse
    return lambda request: HttpResponse(saying + "\n")
