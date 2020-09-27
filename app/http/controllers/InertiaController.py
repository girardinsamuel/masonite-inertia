"""Inertia Demo Controller"""
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse
from masonite.view import View
from masonite.request import Request


class InertiaController(Controller):
    """Controller for testing Inertia."""

    def show(self, view: View):
        return view.render("app")

    def inertia(self, view: InertiaResponse):
        def lazy_prop():
            return "6"

        return view.render("Index", {"user": "Sam", "lazy": lazy_prop})

    def inertia_with_error(self, view: InertiaResponse, request: Request):
        request.session.flash("error", "form error")
        return request.redirect("/")

    def helloworld(self, view: InertiaResponse):
        return view.render("HelloWorld", {"first_name": "Sam"}).with_root_view(
            "spa_view_2"
        )
