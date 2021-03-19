from sanic.log import logger

import settings
from app import app
from app import clients


def run_server():
    async def start_up(app, loop):
        logger.info('START APP')
        await clients.setup(app)

    async def shutdown(app, loop):
        await clients.shutdown(app)
        logger.info('STOP APP')

    app.listener('before_server_start')(start_up)
    app.listener('after_server_stop')(shutdown)

    app.go_fast(
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.NUM_OF_WORKERS,
        debug=settings.DEBUG,
        auto_reload=settings.DEBUG
    )


if __name__ == '__main__':
    run_server()
