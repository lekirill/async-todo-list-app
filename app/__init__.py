from sanic import Sanic

from app.routers import set_up_routes

app = Sanic("todo_app")
app = set_up_routes(app)
