from masonite.testing import TestCase
from masonite.routes import Get
from jinja2 import Markup
from src.masonite.inertia.helpers import inertia as inertia_helper


class TestPackage(TestCase):
    def setUp(self):
        super().setUp()
        self.routes(only=[Get("/app", "InertiaController@inertia")])

    def test_inertia_helper_directly(self):
        data = inertia_helper()
        self.assertIsInstance(data, Markup)
        self.assertEqual(
            "<div id='app' data-page='{{ page | safe }}'></div>", str(data)
        )

    def test_inertia_helper_is_in_page_if_inertia_route(self):
        """Check if beginning of what helper outputs is in the page"""
        assert self.get("/app").assertContains("id='app'")
        assert self.get("/app").assertContains("data-page='{{ page | safe }}'")
