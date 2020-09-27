from masonite.request import Request
from masonite.response import Response

from masonite.inertia.core.InertiaAssetVersion import inertia_asset_version


class InertiaMiddleware:
    """Inertia Middleware to check whether this is an Inertia request."""

    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response

    def before(self):
        self.request.is_inertia = self.request.header("HTTP_X_INERTIA")
        if (
            self.request.is_inertia
            and self.request.method == "GET"
            and self.request.header("HTTP_X_INERTIA_VERSION") != inertia_asset_version()
        ):
            self.request.header("X-Inertia-Location", self.request.path)
            return self.response.view("", status=409)

    def after(self):
        if self.request.is_inertia:
            self.request.header("Vary", "Accept")
            self.request.header("X-Inertia", True)

            # use 303 response code when redirecting from PUT, PATCH, DELETE requests
            if (
                self.request.method in ["PUT", "PATCH", "DELETE"]
                and self.request.is_status(302)
            ):
                self.request.status(303)
