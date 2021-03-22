"""A InertiaProvider Service Provider."""
from masonite.providers import Provider
from masonite.views import View

from masonite.inertia.core.InertiaResponse import InertiaResponse
from masonite.inertia.commands.InstallCommand import InstallCommand
from masonite.inertia.commands.DemoCommand import DemoCommand
from masonite.inertia.helpers import inertia


class InertiaProvider(Provider):
    """Masonite adapter for Inertia.js Service Provider."""

    def __init__(self, application):
        self.application = application

    def register(self):
        self.app.bind("Inertia", InertiaResponse(self.application))
        self.app.bind("InstallCommand", InstallCommand())
        self.app.bind("DemoCommand", DemoCommand())

    def boot(self, view: View):
        self.register_view_helper(view)

    def register_view_helper(self, view):
        view.share({"inertia": inertia})
