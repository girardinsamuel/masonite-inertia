from masonite.inertia.core.InertiaAssetVersion import inertia_asset_version


class InertiaMiddleware:
    """Inertia Middleware to check whether this is an Inertia request."""

    def before(self, request, response):
        request.is_inertia = request.header("X_INERTIA")
        if (
            request.is_inertia
            and request.get_request_method() == "GET"
            and request.header("X_INERTIA_VERSION") != inertia_asset_version(request.app)
        ):
            request.header("X-Inertia-Location", request.get_path())
            return response.view("", status=409)

    def after(self, request, response):


        if request.is_inertia:
            response.header("Vary", "Accept")
            response.header("X-Inertia", 'true')

            # use 303 response code when redirecting from PUT, PATCH, DELETE requests
            if (
                request.get_request_method() in ["PUT", "PATCH", "DELETE"]
                and response.is_status(302)
            ):
                response.status(303)
