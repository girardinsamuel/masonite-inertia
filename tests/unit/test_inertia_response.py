from masonite.request import Request
from masonite.response.response import Response
from masonite.routes import Route
from masonite.tests import TestCase
from masonite.utils.http import generate_wsgi
from src.masonite.inertia import lazy


class TestInertiaResponse(TestCase):
    def setUp(self):
        super().setUp()
        self.setRoutes(
            Route.get("/external", "TestController@external").name("testing.external"),
            Route.get("/basic", "TestController@basic").name("testing.basic"),
            Route.get("/custom-root", "TestController@custom_root"),
            Route.get("/callables", "TestController@lazy_view").name("testing.lazy_view"),
            Route.get("/lazy", "TestController@with_lazy_props").name("testing.with_lazy_props"),
            Route.get("/errors", "TestController@inertia_with_error").name("testing.errors"),
        )

        # set predictable version for unit testing
        self.application.make("inertia").version("123")

    def tearDown(self):
        super().tearDown()
        self.application.make("inertia").version("")
        self.application.make("inertia").shared_props = {"errors": {}}

    def create_request(self, url, method="GET"):
        request = Request(generate_wsgi(path=url, method=method))
        self.application.bind("request", request)
        return request

    def create_response(self, request, component, props):
        self.application.bind("response", Response(self.application))
        view = self.application.make("inertia").render(component, props)
        self.application.make("response").view(view)
        test_response = self.application.make("tests.response").build(
            self.application, request, self.application.make("response"), ""
        )
        return test_response

    def test_server_response(self):
        response = self.get("/basic")
        response.assertViewHas(
            "page",
            {
                "component": "Index",
                "props": {"user": "Sam", "auth": {"user": ""}, "errors": {}},
                "url": "/basic",
                "version": "123",
            },
        ).assertViewIs("app")

    def test_server_response_renders_data_in_template(self):
        response = self.get("/basic")
        response.assertContains(
            '<div id="app" data-page="{&quot;component&quot;: &quot;Index&quot;, &quot;props&quot;: {&quot;user&quot;: &quot;Sam&quot;, &quot;auth&quot;: {&quot;user&quot;: &quot;&quot;}, &quot;errors&quot;: {}}, &quot;url&quot;: &quot;/basic&quot;, &quot;version&quot;: &quot;123&quot;}"></div>'  # noqa: E501
        )

    def test_xhr_response(self):
        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        response = self.create_response(request, "Index", {"user": "Sam"})
        response.assertJsonExact(
            {
                "component": "Index",
                "props": {
                    "user": "Sam",
                    "auth": {"user": ""},
                    "errors": {},
                },
                "url": "/basic",
                "version": "123",
            }
        )

    def test_xhr_partial_response(self):
        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        request.header("X-Inertia-Partial-Component", "Index")
        request.header("X-Inertia-Partial-Data", ["partial"])
        (
            self.create_response(request, "Index", {"user": "Sam", "partial": "data"})
            .assertJsonPath("component", "Index")
            .assertJsonPath("url", "/basic")
            .assertJsonMissing("props.user")
            .assertJsonPath(
                "props",
                {
                    "partial": "data",
                    "auth": {"user": ""},
                    "errors": {},
                },
            )
        )

    def test_lazy_props_are_not_included_by_default(self):
        request = self.create_request("/basic")
        request.header("X-Inertia", True)

        def callable_prop(request):
            return 4

        (
            self.create_response(request, "Index", {"user": "Sam", "lazy": lazy(callable_prop)})
            .assertJsonPath("component", "Index")
            .assertJsonPath("url", "/basic")
            .assertJsonMissing("props.lazy")
            .assertJsonPath(
                "props",
                {
                    "user": "Sam",
                    "auth": {"user": ""},
                    "errors": {},
                },
            )
        )

    def test_lazy_props_are_included_in_partial_reload(self):
        request = self.create_request("/basic")
        request.header("X-Inertia", True)
        request.header("X-Inertia-Partial-Component", "Index")
        request.header("X-Inertia-Partial-Data", ["lazy"])

        def callable_prop(request):
            return 4

        (
            self.create_response(request, "Index", {"user": "Sam", "lazy": lazy(callable_prop)})
            .assertJsonPath("component", "Index")
            .assertJsonPath("url", "/basic")
            .assertJsonMissing("props.user")
            .assertJsonPath(
                "props",
                {
                    "lazy": 4,
                    "auth": {"user": ""},
                    "errors": {},
                },
            )
        )

    def test_location(self):
        self.get("/external").assertIsStatus(409).assertHasHeader(
            "X-Inertia-Location", "https://inertiajs.com"
        )

    def test_share(self):
        self.application.make("inertia").share({"test": "key", "other": "value"})
        props = self.application.make("inertia").get_shared_props()
        self.assertEqual(props, {"errors": {}, "test": "key", "other": "value"})

    def test_shared_data_can_be_flushed(self):
        self.application.make("inertia").share({"test": "key"})
        assert self.application.make("inertia").get_shared_props() == {
            "test": "key",
            "errors": {},
        }
        self.application.make("inertia").flush_shared()
        assert self.application.make("inertia").get_shared_props() == {}

    def test_get_shared(self):
        self.application.make("inertia").share({"nested": {"key": "4"}})
        assert self.application.make("inertia").get_shared_props("nested.key") == "4"
        assert self.application.make("inertia").get_shared_props("unknown", "nope") == "nope"

    def test_data_can_be_shared_at_anytime(self):
        self.application.make("inertia").share({"test": "key2"})
        self.get("/basic").assertViewHas("page.props.test", "key2")
        # ensure to reset shared data for other tests
        self.application.make("inertia").shared_props = {"errors": {}}

    def test_that_callables_props_are_resolved(self):
        self.get("/callables").assertViewHas("page.props.count", 2)

    def test_customizing_root_view_in_controller(self):
        self.get("/custom-root").assertViewIs("spa_view")

    def test_that_errors_flashed_in_session_are_shared(self):
        res = self.get("/errors")
        res.assertInertiaHasProp("errors", "An error occured.")
