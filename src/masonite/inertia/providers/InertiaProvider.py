"""A InertiaProvider Service Provider."""
from masonite.configuration import config
from masonite.packages.providers import PackageProvider

from ..core.Inertia import Inertia
from ..helpers import inertia
from ..testing import InertiaTestingResponse


class InertiaProvider(PackageProvider):
    """Masonite adapter for Inertia.js Service Provider."""

    def configure(self):
        self.root("masonite/inertia").name("inertia").config("config/inertia.py", publish=True)
        inertia = Inertia(self.application, config("inertia"))
        self.application.bind("inertia", inertia)
        self.application.make("tests.response").add(InertiaTestingResponse)

    def boot(self):
        # looks like here it's not doing anything.
        self.application.make("view").share({"inertia": inertia})
