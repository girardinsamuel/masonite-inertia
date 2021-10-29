"""Inertia Demo Controller"""
from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response

from src.masonite.inertia import Inertia, lazy


class InertiaController(Controller):
    """Controller for testing Inertia locally."""

    def home(self, view: View):
        """Classic HTML home page"""
        return view.render("base")

    def basic(self, request: Request):
        """Inertia home page"""
        # we can also resolve inertia in app container
        return request.app.make("inertia").render("Index", {"user": "User 1"})

    def second_page(self, view: Inertia):
        """Inertia second page"""
        return view.render("HelloWorld", {"first_name": "John"})

    def states(self, view: Inertia):
        return view.render("States", {"name": "Initial name"})

    def lazy_props(self, request: Request, view: Inertia):
        def callable_prop(request):
            return 1

        def other_callable_prop(request):
            return 2

        return view.render(
            "LazyProps",
            {
                "basic": "Normal prop !",
                "callable": callable_prop,
                "lazy_prop": lazy(other_callable_prop),
            },
        )

    def external(self, request: Request, view: Inertia):
        return view.location("https://inertiajs.com")

    def add_errors(self, request: Request, response: Response):
        request.app.make("session").driver("cookie").flash("errors", {"form": "Form error !"})
        return response.redirect("/inertia")

    def other_root_view(self, view: Inertia):
        return view.render("Index", {"user": "Sam"}, custom_root_view="app2.html")
