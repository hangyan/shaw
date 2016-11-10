#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Hang Yan'

ERR_EMAIL_ALREADY_ACTIVATED = 'email_already_activated'
ERR_DB_INTEGRITY_ERROR = 'db_integrity_error'
ERR_EMAIL_NOT_ACTIVATED = 'email_not_activated'
ERR_EMAIL_VERIFY_FAILED = 'email_verify_failed'
ERR_MISSING_QUERY_PARAMS = 'missing_query_params'
ERR_MISSING_BODY_FIELD = 'missing_body_field'
ERR_TIME_LIMIT_EXCEEDED = 'time_limit_exceeded'
ERR_UNSUPPORTED = 'unsupported'
ERR_INVALID_VALUE = 'invalid_value'
ERR_PHONE_VERIFY_FAILED = 'phone_verify_failed'
ERR_TOO_MANY_REQUESTS = 'too_many_requests'
ERR_CAPTCHA_VERIFY_FAILED = 'captcha_verify_failed'
ERR_CAPTCHA_REQUIRED = 'require_captcha'
# This code is similar to `email_already_activated` but more general.
ERR_ACTION_ALREADY_DONE = 'action_already_done'
# http 412
ERR_PRECONDITION_FAILED = 'precondition_failed'
ERR_CAPTCHA_NEED_REFRESH = 'captcha_need_refresh'
ERR_OBJECT_NOT_FOUND = 'object_not_found'

ERR_UPSTREAM_ERROR = 'upstream_error'

ERR_CODE_MAP = {}
