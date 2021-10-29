"""Inertia Demo Controller"""
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse


class InertiaDemoController(Controller):
    """Controller for testing Inertia."""

    def show(self, view: InertiaResponse):
        return view.render("Index", custom_root_view="inertia_demo.html")

    def hello(self, view: InertiaResponse):
        return view.render(
            "Hello", {"first_name": "Sam"}, custom_root_view="inertia_demo.html"
        )
