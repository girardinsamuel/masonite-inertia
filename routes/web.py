""" Web Routes """
from masonite.routes import Get

ROUTES = [
    Get("/", "InertiaController@inertia"),
    Get("/helloworld", "InertiaController@helloworld"),
]
