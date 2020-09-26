"""A TestController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class TestController(Controller):
    """TestController Controller Class."""

    def __init__(self, request: Request):
        """TestController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render("test")
