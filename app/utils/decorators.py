from marshmallow import Schema, ValidationError
from sanic.request import Request
from sanic.log import logger
from functools import wraps

from app.utils.http_responses import *


def validate_json(schema):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, **kwargs):
            try:
                schema().load(data=request.json)
                return await func(request, **kwargs)
            except ValidationError as err:
                logger.info(err.messages)
                return http_bad_request(err.messages)

        return wrapper

    return decorator
