from markupsafe import Markup

from masonite.routes import Route
from masonite.tests import TestCase
from src.masonite.inertia.helpers import inertia


class TestInertiaViewHelper(TestCase):
    def setUp(self):
        super().setUp()
        self.setRoutes(
            Route.get("/root-with-helper", "TestController@custom_root"),
            Route.get("/custom-id", "TestController@custom_id"),
        )
        # set predictable version for unit testing
        self.application.make("inertia").version("123")

    def tearDown(self):
        super().tearDown()
        self.application.make("inertia").version("")

    def test_helper_directly(self):
        page_data = {"page": "test"}
        data = inertia(page_data)
        self.assertIsInstance(data, Markup)
        self.assertEqual("<div id='app' data-page='{\"page\": \"test\"}'></div>", str(data))

    def test_helper_renders_page_data_correctly_inside_template(self):
        response = self.get("/root-with-helper")
        response.assertContains(
            "<div id='app' data-page='\"{&quot;component&quot;: &quot;Index&quot;, &quot;props&quot;: {&quot;auth&quot;: {&quot;user&quot;: &quot;&quot;}, &quot;errors&quot;: {}}, &quot;url&quot;: &quot;/root-with-helper&quot;, &quot;version&quot;: &quot;123&quot;}\"'></div>"  # noqa: E501
        )

    def test_can_customize_app_id_through_helper(self):
        response = self.get("/custom-id")
        response.assertContains("<div id='my_app'")
