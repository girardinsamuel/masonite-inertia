"""A TestController Module."""
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse


class TestController(Controller):
    """TestController Controller Class."""

    def custom_id(self, view: InertiaResponse):
        return view.render("Index", custom_root_view="test_custom_id")

    def lazy_view(self, view: InertiaResponse):
        def get_count():
            return 2

        return view.render("Index", {"count": get_count})

    def lazy_view_with_request(self, view: InertiaResponse):
        def is_authenticated(request):
            return request.user()

        return view.render("Index", {"is_authenticated": is_authenticated})
