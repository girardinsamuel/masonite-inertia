"""Test controllers using InertiaResponse"""
import io
import sys
from _pytest.outcomes import Failed

from masonite.tests import TestCase
from masonite.routes import Route, RouteCapsule


class TestInertiaAssertions(TestCase):
    def setUp(self):
        super().setUp()
        self.application.bind(
            "router",
            RouteCapsule(
                Route.set_controller_module_location(
                    "tests.integrations.controllers"
                ).get("/nested-props", "TestController@nested_props"),
                Route.set_controller_module_location(
                    "tests.integrations.controllers"
                ).get("/hello-world", "TestController@helloworld"),

            ),
        )

    def test_assert_is_inertia(self):
        self.get("/hello-world").assertIsInertia()

    def test_component(self):
        self.get("/hello-world").assertInertia().component("HelloWorld")

    def test_has(self):
        self.get("/nested-props").assertInertia().has("count", 3).has("nested.a").has("nested.b.end", "finally")

    def test_contains(self):
        self.get("/nested-props").assertInertia().contains("array", 3)

    def test_url(self):
        self.get("/hello-world").assertInertia().url("/hello-world")

    def test_version(self):
        self.application.make("inertia").version("123456")
        self.get("/hello-world").assertInertia().version("123456")
        self.application.make("inertia").version("")  # reset

    def test_missing(self):
        response = self.get("/hello-world").assertInertia()
        response.missing("not")
        with self.assertRaises(AssertionError):
            response.missing("first_name")

    def test_dump(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.get("/hello-world").assertInertia().dump()
        dumped_output = capturedOutput.getvalue()
        assert "HelloWorld" in dumped_output
        assert "first_name" in dumped_output
        assert "hello-world" in dumped_output

    def test_dd(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(Failed):
            self.get("/hello-world").assertInertia().dd().component("HelloWorld")

        dumped_output = capturedOutput.getvalue()
        assert "HelloWorld" in dumped_output