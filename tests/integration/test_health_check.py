from sanic_testing import TestManager


def test_ping(monkeypatch, test_app):
    async def select(*args, **kwargs):
        return [(1,)]

    with TestManager(test_app) as client:
        monkeypatch.setattr(test_app.todo_db, 'select', select, raising=True)
        response = client.get(
            '/ping',
        )
        assert response.status_code == 200
