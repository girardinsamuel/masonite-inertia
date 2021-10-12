from masonite.pipeline import Pipeline
from masonite.request import Request
from masonite.response.response import Response
from masonite.routes import Route
from masonite.tests import TestCase
from masonite.utils.http import generate_wsgi
from src.masonite.inertia import InertiaMiddleware


class AppInertiaMiddleware(InertiaMiddleware):
    """Test middleware needed for unit tests"""

    test_version = ""

    def version(self, request):
        return self.test_version


class TestInertiaMiddleware(TestCase):
    def setUp(self):
        super().setUp()
        self.setRoutes(
            Route.get("/basic", "TestController@basic").name("testing.basic"),
        )

    def tearDown(self):
        super().tearDown()
        self.application.make("inertia").version("")

    def create_request(self, url, method="GET"):
        request = Request(generate_wsgi(path=url, method=method))
        request.app = self.application
        self.application.bind("request", request)
        return request

    def create_response(self, request, component, props):
        self.application.bind("response", Response(self.application))
        view = self.application.make("inertia").render(component, props)
        Pipeline(request, self.application.make("response")).through(
            self.application.make("middleware").get_http_middleware(),
            handler="before",
        )
        self.application.make("response").view(view)
        Pipeline(request, self.application.make("response")).through(
            self.application.make("middleware").get_http_middleware(),
            handler="after",
        )
        test_response = self.application.make("tests.response").build(
            self.application, request, self.application.make("response"), ""
        )
        return test_response

    def test_response_ok_without_version(self):
        AppInertiaMiddleware.test_version = ""
        self.application.make("middleware").http_middleware[0] = AppInertiaMiddleware

        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        request.header("X-Inertia-Version", "")
        response = self.create_response(request, "Index", {"user": "Sam"})
        response.assertOk().assertJsonPath("component", "Index")

    def test_response_ok_with_correct_version_number(self):
        AppInertiaMiddleware.test_version = 1234
        self.application.make("middleware").http_middleware[0] = AppInertiaMiddleware

        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        request.header("X-Inertia-Version", 1234)
        response = self.create_response(request, "Index", {"user": "Sam"})

        response.assertOk().assertJsonPath("component", "Index")

    def test_response_ok_with_correct_version_string(self):
        AppInertiaMiddleware.test_version = "1234"
        self.application.make("middleware").http_middleware[0] = AppInertiaMiddleware

        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        request.header("X-Inertia-Version", "1234")
        response = self.create_response(request, "Index", {"user": "Sam"})

        response.assertOk().assertJsonPath("component", "Index")

    def test_it_will_instruct_inertia_to_reload_on_a_version_mismatch(self):
        AppInertiaMiddleware.test_version = "1234"
        self.application.make("middleware").http_middleware[0] = AppInertiaMiddleware

        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        request.header("X-Inertia-Version", "4321")

        response = self.create_response(request, "Index", {"user": "Sam"})

        response.assertNoContent(409).assertHasHeader("X-Inertia-Location", "/basic")

    def test_setting_root_view_via_middleware_property(self):
        AppInertiaMiddleware.root_view = "spa_view"
        AppInertiaMiddleware.test_version = ""
        self.application.make("middleware").http_middleware[0] = AppInertiaMiddleware

        response = self.get("/basic")
        response.assertViewIs("spa_view")

    def test_setting_root_view_via_middleware_method(self):
        def set_root_view(self, request):
            return "spa_view"

        AppInertiaMiddleware.set_root_view = set_root_view
        AppInertiaMiddleware.test_version = ""
        self.application.make("middleware").http_middleware[0] = AppInertiaMiddleware

        response = self.get("/basic")
        response.assertViewIs("spa_view")
