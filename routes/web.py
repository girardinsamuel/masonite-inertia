""" Web Routes """
from masonite.routes import Get, Post

ROUTES = [
    Get("/", "InertiaController@inertia").name("home"),
    Post("/error", "InertiaController@inertia_with_error").name("home.error"),
    Get("/external", "InertiaController@external").name("home.external"),
    Get("/helloworld", "InertiaController@helloworld").name("helloworld"),
]
