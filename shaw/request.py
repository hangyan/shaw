from __future__ import unicode_literals
import logging

from shaw.exception import SHException

LOG = logging.getLogger(__name__)


def is_success(code):
    return 200 <= code <= 299


class ShawRequest(object):
    endpoint = None
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    class Meta:
        abstract = True

    @classmethod
    def send(cls, path, auth=None, method='GET', endpoint=None,
             params=None, data=None, headers=None):
        if endpoint is None:
            endpoint = cls.endpoint
        url = '/'.join([endpoint, path.lstrip('/')])

        LOG.info('Requesting url={}, method={}, header={}, '
                 'data={}, params={}'.format(url, method, headers, data, params))

        if headers is None:
            headers = cls.headers.copy()

        args = {'headers': headers}
        if auth is not None:
            args['auth'] = auth
        if params is not None:
            args['params'] = params
        if data is not None:
            args['json'] = data

        import requests
        if method == 'POST':
            response = requests.post(url, **args)
        elif method == 'PUT':
            response = requests.put(url, **args)
        elif method == 'DELETE':
            response = requests.delete(url, **args)
        else:
            response = requests.get(url, **args)

        return cls._parse_response(response)

    @classmethod
    def _parse_response(cls, response):
        code = response.status_code
        LOG.debug('Response status_code={}, content={}'.format(code, response.content))

        result = {
            'status_code': code,
            'data': None,
        }

        if code == 204:
            return result
        elif code == 503:
            raise SHException(code=503, message='Service is unavailable! | {}'.format(cls.endpoint))

        try:
            result['data'] = response.json()
        except Exception as ex:
            LOG.error('Failed to parse response. | {} - {}'.format(type(ex), ex.message))
            raise SHException(code=500, message='Service data was not in valid json format!')

        if not is_success(code):
            data = result['data']
            if 'code' in data:
                raise SHException(code=data['code'], message=data['message'])
            raise SHException(code=code, message=response.text)

        return result
