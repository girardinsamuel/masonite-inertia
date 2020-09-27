"""A InertiaProvider Service Provider."""
from masonite.provider import ServiceProvider
from masonite.view import View

from masonite.inertia.core.InertiaResponse import InertiaResponse
from masonite.inertia.commands.InstallCommand import InstallCommand
from masonite.inertia.commands.DemoCommand import DemoCommand
from masonite.inertia.helpers import inertia


class InertiaProvider(ServiceProvider):
    """Masonite adapter for Inertia.js Service Provider."""

    wsgi = False

    def register(self):
        self.app.bind("Inertia", InertiaResponse(self.app))
        self.app.bind("InstallCommand", InstallCommand())
        self.app.bind("DemoCommand", DemoCommand())

    def boot(self, view: View):
        self.register_view_helper(view)

    def register_view_helper(self, view):
        view.share({"inertia": inertia})
        # snippets_path = os.path.join(os.path.dirname(__file__), "../snippets")
        # app_path = os.path.join(snippets_path, "static")

        # self.publishes(
        #     {
        #         os.path.join(
        #             app_path, "mix-manifest.json"
        #         ): "storage/static/mix-manifest.json",
        #         os.path.join(app_path, "app.js"): "storage/static/js/app.js",
        #         os.path.join(
        #             app_path, "pages/Index.vue"
        #         ): "storage/static/js/pages/Index.vue",
        #         os.path.join(
        #             app_path, "pages/HelloWorld.vue"
        #         ): "storage/static/js/pages/HelloWorld.vue",
        #     },
        #     tag="app",
        # )

        # self.publishes(
        #     {
        #         os.path.join(
        #             snippets_path, "demo/InertiaController.py"
        #         ): "app/http/controllers/InertiaController.py",
        #     },
        #     tag="demo",
        # )

        # # TODO append two routes
