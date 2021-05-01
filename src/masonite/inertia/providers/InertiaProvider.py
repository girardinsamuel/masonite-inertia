"""A InertiaProvider Service Provider."""
from masonite.providers import Provider
from masonite.utils.structures import load

from ..core.Inertia import Inertia
from ..commands.InstallCommand import InstallCommand
from ..commands.DemoCommand import DemoCommand
from ..testing import InertiaTestingResponse


class InertiaProvider(Provider):
    """Masonite adapter for Inertia.js Service Provider."""

    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.bind("config.inertia", "masonite.inertia.config.inertia")
        inertia = Inertia(
            self.application, load(self.application.make("config.inertia"))
        )
        self.application.bind("inertia", inertia)
        self.application.make("commands").add(InstallCommand(), DemoCommand())
        self.application.make("tests.response").add(InertiaTestingResponse)

    def boot(self):
        pass
