"""A InertiaProvider Service Provider."""

from masonite.provider import ServiceProvider
from masonite.inertia.commands.InstallCommand import InstallCommand


class InertiaProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind("InstallCommand", InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
