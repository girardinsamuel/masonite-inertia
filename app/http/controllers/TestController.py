"""A TestController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse


class TestController(Controller):
    """TestController Controller Class."""

    def custom_id(self, view: InertiaResponse):
        return view.render("Index", {}, "test_custom_id")
