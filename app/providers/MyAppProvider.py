from masonite.provider import ServiceProvider

from masonite.inertia.core.InertiaResponse import InertiaResponse


class MyAppProvider(ServiceProvider):
    """Custom app provider to configure app"""

    wsgi = False

    def boot(self, inertia: InertiaResponse):
        # update default view to use with Inertia
        inertia.set_root_view("spa_view")

