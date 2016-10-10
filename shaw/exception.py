#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from shaw.errors import ERR_CODE_MAP
from shaw.web import error_response, json_response

__author__ = 'Hang Yan'

LOG = logging.getLogger(__name__)


class SHException(Exception):
    def __init__(self, code, message):
        super(SHException, self).__init__(message)
        self.code = code

    def __str__(self):
        return 'code: {}, message: {}'.format(self.code, self.message)


# For django1.10+ middleware

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class SHExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        LOG.error("Capture exception. type: {}, info: {}".format(type(exception), exception))
        if type(exception) == SHException:
            if type(exception.code) == int:
                return error_response(message=exception.message, status=exception.code)
            return json_response(data={
                'message': exception.message,
                'code': exception.code,
            }, status=get_status_code(exception.code))


def get_status_code(err_code):
    return 400 if err_code not in ERR_CODE_MAP else ERR_CODE_MAP[err_code]
