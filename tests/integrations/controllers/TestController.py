from masonite.controllers import Controller
from masonite.request import Request
from masonite.sessions import Session
from src.masonite.inertia import Inertia, lazy


class TestController(Controller):
    """TestController used for unit tests only."""

    def basic(self, request: Request):
        return request.app.make("inertia").render("Index", {"user": "Sam"})

    def basic2(self, request: Request):
        return request.app.make("inertia").render("Index", {"user": "Sam"})

    def test(self, request: Request):
        def lazy_prop():
            return "6"

        return request.app.make("inertia").render(
            "Index", {"user": "Sam", "lazy": lazy_prop}
        )

    def inertia_with_error(self, session: Session, inertia: Inertia):
        session.flash("errors", "An error occured.")
        return inertia.render("HelloWorld")

    def helloworld(self, inertia: Inertia):
        return inertia.render("HelloWorld", {"first_name": "Sam"}, "spa_view_2")

    def external(self, request: Request):
        return request.app.make("inertia").location("https://inertiajs.com")

    def custom_root(self, view: Inertia):
        return view.render("Index", custom_root_view="spa_view")

    def custom_id(self, view: Inertia):
        return view.render("Index", custom_root_view="test_custom_id")

    def lazy_view(self, view: Inertia):
        def get_count():
            return 2

        return view.render("Index", {"count": get_count})

    def with_lazy_props(self, view: Inertia):
        def get_count():
            return 2

        return view.render("Index", {"count": lazy(get_count)})

    def lazy_view_with_request(self, view: Inertia):
        def is_authenticated(request):
            return request.user()

        return view.render("Index", {"is_authenticated": is_authenticated})

    def nested_props(self, view: Inertia):
        return view.render(
            "Index",
            {
                "count": 3,
                "array": [1, 2, 3],
                "nested": {"a": 1, "b": {"end": "finally"}},
            },
        )
