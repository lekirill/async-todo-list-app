from sanic.response import json
from sanic.request import Request

from app.utils import http_responses


async def ping(request: Request):
    try:
        await request.app.todo_db.first("select 1")
        return http_responses.http_ok({'ok'})
    except:
        return http_responses.http_bad_request('no database connection')
