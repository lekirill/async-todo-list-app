import pytest

from app import app as application  # TODO find import error cause
from app import clients


@pytest.fixture
def test_app():
    async def start_up(app, loop):
        await clients.setup(app)

    async def shutdown(app, loop):
        await clients.shutdown(app)

    application.listener('before_server_start')(start_up)
    application.listener('after_server_stop')(shutdown)

    return application
