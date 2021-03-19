from sanic import Blueprint
from sanic import Sanic
from sanic_openapi import swagger_blueprint

from app.api.v1 import note
from app.api.health_check import ping


def set_up_routes(app: Sanic):
    api = Blueprint('api', url_prefix='/api/v1')
    api.add_route(note.add, '/add', methods=('POST',))
    api.add_route(note.edit, '/edit/<id:int>', methods=('POST',))
    api.add_route(note.del_by_id, '/delete/<id:int>', methods=('DELETE',))
    api.add_route(note.set_done, '/done/<id:int>', methods=('POST',))
    api.add_route(note.set_undone, '/undone/<id:int>', methods=('POST',))
    api.add_route(note.set_in_progress, '/in_progress/<id:int>', methods=('POST',))
    api.add_route(note.set_off_progress, '/off_progress/<id:int>', methods=('POST',))

    app.blueprint(api)
    app.blueprint(swagger_blueprint)
    app.add_route(ping.ping, '/ping', methods=('GET',))

    return app
