"""Test controllers using InertiaResponse"""

from masonite.testing import TestCase
from masonite.routes import Get


class TestInertiaController(TestCase):
    def setUp(self):
        super().setUp()
        self.routes(only=[Get("/helloworld", "InertiaController@helloworld")])

    def test_test(self):
        # assert self.get("/app").hasMiddleware("inertia")
        # view = self.get("/helloworld")
        # view.request.header("HTTP_X_INERTIA", True)

        # response = view.response
        # request = view.request
        pass