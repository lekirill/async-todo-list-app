from sanic.response import json


def _error_response(msg: str, code: int):
    response = json({
        'success': False,
        'error': msg
    }, status=code)
    return response


def _success_response(msg: str, code: int):
    response = json({
        'success': True,
        'result': msg
    }, status=code)
    return response


def http_ok(msg='OK'):
    code = 200
    return _success_response(msg, code)


def http_created(msg='Created'):
    code = 201
    return _success_response(msg, code)


def http_bad_request(msg='Bad request'):
    code = 400
    return _error_response(msg, code)
