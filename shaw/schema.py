#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shaw import errors

from shaw.collection import check_missing_keys
from shaw.exception import SHException

__author__ = 'Hang Yan'


def check_body_keys(data, keys):
    keys = check_missing_keys(data, keys)
    if not keys:
        return
    raise SHException(code=errors.ERR_MISSING_BODY_FIELD,
                      message='Missing required field in request body: {}'.format(keys))


def validate_value(value, values):
    # support django choices
    vs = [x[0] for x in list(values)] if isinstance(values, tuple) else values
    if value not in vs:
        raise SHException(code=errors.ERR_INVALID_VALUE,
                          message='Invalid value {}, possible choices: {} '.format(value, vs))


def check_params_keys(params, keys, exclusion=False):
    if not exclusion:
        missing_keys = check_missing_keys(params, keys)
        if missing_keys:
            raise SHException(message='Missing required query params: {}'.format(missing_keys),
                              code=errors.ERR_MISSING_QUERY_PARAMS)
        return
    for key in keys:
        if key in params:
            return
    raise SHException(message='Missing required query params(or): {}'.format(keys),
                      code=errors.ERR_MISSING_QUERY_PARAMS)
