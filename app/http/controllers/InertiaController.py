"""Inertia Demo Controller"""
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse
from masonite.view import View


class InertiaController(Controller):
    """Controller for testing Inertia."""

    def show(self, view: View):
        return view.render("app")

    def inertia(self, view: InertiaResponse):
        return view.render("Index")

    def helloworld(self, view: InertiaResponse):
        return view.render("HelloWorld", {"first_name": "Sam"})
