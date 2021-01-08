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
