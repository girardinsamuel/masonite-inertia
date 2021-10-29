"""A InertiaProvider Service Provider."""
from masonite.providers import Provider

from masoniteinertia.core.InertiaResponse import InertiaResponse
from masoniteinertia.commands.InstallCommand import InstallCommand
from masoniteinertia.commands.DemoCommand import DemoCommand
from masoniteinertia.helpers import inertia


class InertiaProvider(Provider):
    """Masonite adapter for Inertia.js Service Provider."""

    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.bind("Inertia", InertiaResponse(self.application))
        self.application.make('commands').add(
            InstallCommand(), DemoCommand()
        )

        self.application.make('view').share({"inertia": inertia})

    def boot(self):
        pass
