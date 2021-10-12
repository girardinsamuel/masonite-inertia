"""Test controllers using InertiaResponse"""
import io
import sys

from _pytest.outcomes import Failed

from masonite.routes import Route
from masonite.tests import TestCase


class TestInertiaAssertions(TestCase):
    def setUp(self):
        super().setUp()
        self.setRoutes(
            Route.get("/nested-props", "TestController@nested_props"),
            Route.get("/hello-world", "TestController@helloworld"),
        )

    def test_assert_is_inertia(self):
        self.get("/hello-world").assertIsInertia()

    def test_assert_inertia_component(self):
        self.get("/hello-world").assertInertiaComponent("HelloWorld")

    def test_assert_inertia_version(self):
        self.application.make("inertia").version("123456")
        self.get("/hello-world").assertInertiaVersion("123456")
        self.application.make("inertia").version("")  # reset

    def test_assert_inertia_root_view(self):
        self.get("/hello-world").assertInertiaRootView("spa_view_2")

    def test_assert_inertia_has_prop(self):
        self.get("/nested-props").assertInertiaHasProp("count", 3).assertInertiaHasProp(
            "nested.a"
        ).assertInertiaHasProp("nested.b.end", "finally")

    def test_assert_inertia_missing_prop(self):
        self.get("/hello-world").assertInertiaMissingProp("not")

    def test_assert_inertia_prop_count(self):
        self.get("/nested-props").assertInertiaPropCount("array", 3)

    def test_component(self):
        self.get("/hello-world").withInertia().component("HelloWorld")

    def test_has(self):
        self.get("/nested-props").withInertia().has("count", 3).has("nested.a").has(
            "nested.b.end", "finally"
        )

    def test_has_count(self):
        self.get("/nested-props").withInertia().hasCount("array", 3)

    def test_url(self):
        self.get("/hello-world").withInertia().url("/hello-world")

    def test_version(self):
        self.application.make("inertia").version("123456")
        self.get("/hello-world").withInertia().version("123456")
        self.application.make("inertia").version("")  # reset

    def test_missing(self):
        response = self.get("/hello-world").withInertia()
        response.missing("not")
        with self.assertRaises(AssertionError):
            response.missing("first_name")

    def test_dump(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.get("/hello-world").withInertia().dump()
        dumped_output = capturedOutput.getvalue()
        assert "HelloWorld" in dumped_output
        assert "first_name" in dumped_output
        assert "hello-world" in dumped_output

    def test_dd(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(Failed):
            self.get("/hello-world").withInertia().dd().component("HelloWorld")

        dumped_output = capturedOutput.getvalue()
        assert "HelloWorld" in dumped_output
