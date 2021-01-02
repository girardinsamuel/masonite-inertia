from masonite.testing import TestCase
from masonite.routes import Get
from jinja2 import Markup
from src.masonite.inertia.helpers import inertia as inertia_helper


class TestPackage(TestCase):
    def setUp(self):
        super().setUp()
        self.routes(
            only=[
                Get("/app", "InertiaController@inertia"),
                Get("/helloworld", "InertiaController@helloworld"),
                Get("/custom-id", "TestController@custom_id"),
            ]
        )

    def test_inertia_helper_directly(self):
        page_data = "test_data"
        data = inertia_helper(page_data)
        self.assertIsInstance(data, Markup)
        self.assertEqual("<div id='app' data-page='test_data'></div>", str(data))

    def test_inertia_helper_is_in_page_if_inertia_route(self):
        """Check if beginning of what helper outputs is in the page"""
        response = self.get("/app")
        import pdb

        pdb.set_trace()
        assert response.assertContains('id="app"')
        assert response.assertContains(
            'data-page="{&quot;component&quot;: &quot;Index&quot;,'
        )
        # check at another route an other component is given
        assert self.get("/helloworld").assertContains(
            "data-page='{&quot;component&quot;: &quot;HelloWorld&quot;,"
        )

    def test_inertia_helper_with_custom_div_id(self):
        assert self.get("/custom-id").assertContains("id='my_app'")
