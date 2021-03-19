import asyncio

from .db import DBClient

import settings


async def setup(app):
    loop = asyncio.get_event_loop()
    app.todo_db = DBClient(settings.DB, loop=loop)
    await app.todo_db.setup()


async def shutdown(app):
    await app.todo_db.close()

