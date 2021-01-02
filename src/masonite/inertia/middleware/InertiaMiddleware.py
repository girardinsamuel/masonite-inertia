from masonite.request import Request
from masonite.response import Response

from masonite.inertia.core.InertiaAssetVersion import inertia_asset_version


class InertiaMiddleware:
    """Inertia Middleware to check whether this is an Inertia request."""

    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response

    def before(self):
        self.request.is_inertia = self.request.header("X_INERTIA")
        if (
            self.request.is_inertia
            and self.request.method == "GET"
            and self.request.header("X_INERTIA_VERSION") != inertia_asset_version()
        ):
            self.request.header("X-Inertia-Location", self.request.path)
            return self.response.view("", status=409)

    def after(self):
        if self.request.is_inertia:
            self.response.header("Vary", "Accept")
            self.response.header("X-Inertia", 'true')

            # use 303 response code when redirecting from PUT, PATCH, DELETE requests
            if (
                self.request.method in ["PUT", "PATCH", "DELETE"]
                and self.response.is_status(302)
            ):
                self.response.status(303)
