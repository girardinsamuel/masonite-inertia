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
        self.application.bind("Inertia", InertiaResponse(self.application))
        self.application.bind("config.inertia", "masonite.inertia.config.inertia")
        self.application.make("commands").add(
            InstallCommand(),
            DemoCommand()
        )

    def boot(self, view: View):
        self.register_view_helper(view)

    def register_view_helper(self, view):
        view.share({"inertia": inertia})
