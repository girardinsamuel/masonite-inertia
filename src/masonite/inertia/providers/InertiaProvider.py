"""A InertiaProvider Service Provider."""
# import os
from masonite.configuration import config
from masonite.packages.providers import PackageProvider

from ..core.Inertia import Inertia
from ..helpers import inertia
from ..testing import InertiaTestingResponse

# package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class InertiaProvider(PackageProvider):
    """Masonite adapter for Inertia.js Service Provider."""

    def configure(self):
        (
            self.root("src/masonite/inertia")
            .name("inertia")
            .config("config/inertia.py", publish=True)
        )
        inertia = Inertia(self.application, config("inertia"))
        self.application.bind("inertia", inertia)
        self.application.make("tests.response").add(InertiaTestingResponse)

    # def register(self):
    #     # Config.merge_with("inertia", os.path.join(package_root, "config/inertia.py"))
    #     Config.merge_with("inertia", "masonite.inertia.config.inertia")
    #     inertia = Inertia(self.application, config("inertia"))
    #     self.application.bind("inertia", inertia)

    #     self.application.make("commands").add(InstallCommand(), DemoCommand())
    #     self.application.make("tests.response").add(InertiaTestingResponse)

    def boot(self):
        self.application.make("view").share({"inertia": inertia})
