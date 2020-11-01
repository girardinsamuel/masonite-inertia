"""Test controllers using InertiaResponse"""

import pdb
from masonite.testing import TestCase
from masonite.routes import Get


class TestInertiaController(TestCase):
    def setUp(self):
        super().setUp()
        self.routes(
            only=[
                Get("/lazy-props", "TestController@lazy_view"),
                Get("/lazy-props-request", "TestController@lazy_view_with_request"),
            ]
        )

    def test_props_can_be_lazy_loaded(self):
        content = self.get("/lazy-props")
        assert content.assertContains("{&quot;count&quot;: 2")

    def test_lazy_loaded_props_can_access_request(self):
        content = self.get("/lazy-props-request")
        assert content.assertContains("{&quot;is_authenticated&quot;: false")
