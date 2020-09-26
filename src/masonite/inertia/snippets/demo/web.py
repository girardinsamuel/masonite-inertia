"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get("/", "InertiaController@show"),
    Get("/helloworld", "InertiaController@helloworld"),
]
