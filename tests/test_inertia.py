from masonite.testing import TestCase
from masonite.routes import Get


class TestInertiaResponse(TestCase):
    def setUp(self):
        super().setUp()
        self.routes(
            only=[
                Get("/app", "InertiaController@inertia"),
                Get("/external", "InertiaController@external"),
            ]
        )

    def test_location(self):
        view = self.get("/external")
        view.assertIsStatus(409)
        view.assertHeaderIs("X-Inertia-Location", "https://inertiajs.com")
