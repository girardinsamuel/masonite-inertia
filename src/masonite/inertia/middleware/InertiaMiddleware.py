import hashlib
import os

from masonite.configuration import config
from masonite.middleware import Middleware

# from masonite.utils.location import public_path


# TODO: move this as a PR into M4
def public_path(relative_path, absolute=True):
    from os.path import abspath, join

    """Build the absolute path to the given relative_path assuming it exists in the configured
    migrations location. The relative path can be returned instead by setting absolute=False."""
    relative_dir = join("tests/integrations/public", relative_path)
    return abspath(relative_dir) if absolute else relative_dir


class InertiaMiddleware(Middleware):
    """Inertia Middleware to check whether this is an Inertia request."""

    def before(self, request, response):
        inertia = request.app.make("inertia")
        if not inertia.get_version():
            inertia.version(self.version(request))
        inertia.share(self.share(request))

        inertia.set_root_view(self.set_root_view(request))
        return request

    def after(self, request, response):
        self.check_version(request, response)
        response = self.change_redirect_code(request, response)
        # set CSRF token as cookie in response so that axios sent back the token
        # in a X-XSRF-TOKEN header in the subsequent request
        # It's important that, the cookie has not HttpOnly and Secure as discussed
        # here: https://stackoverflow.com/a/54132068/15131933
        response.cookie("XSRF-TOKEN", request.cookie("csrf_token"), secure=False, http_only=False)
        return request

    def is_inertia_request(self, request):
        return request.header("X-Inertia")

    def check_version(self, request, response):
        """In the event that the assets change, initiate a client-side location visit
        to force an update."""
        inertia = request.app.make("inertia")
        if (
            self.is_inertia_request(request)
            and request.get_request_method() == "GET"
            and str(request.header("X-Inertia-Version")) != inertia.get_version()
        ):
            # TODO: implements reflash/keep in M4
            # if ($request->hasSession()) {
            #     $request->session()->reflash();
            # }
            return inertia.location(request.get_path())

        return response

    def change_redirect_code(self, request, response):
        if (
            self.is_inertia_request(request)
            and response.is_status(302)
            and request.get_request_method() in ("PUT", "PATCH", "DELETE")
        ):
            response.status(303)
        return response

    def get_session(self, request):
        return request.app.make("session")

    def resolve_validation_errors(self, request):
        """Get validation errors in flash session if any and serialize it to be easy to use
        client-side."""
        # TODO: implement laravel behaviour
        session = self.get_session(request)
        if not session.has("errors"):
            return {}
        else:
            return session.get("errors")

    def share(self, request):
        """Defines the props that are shared by default. Can be overriden."""
        errors = self.resolve_validation_errors
        return {"errors": errors}

    def version(self, request):
        """Determines the current asset version. Can be overriden."""
        assets_url = config("inertia.public_path")
        if assets_url:
            return hashlib.md5(assets_url.encode()).hexdigest()

        manifest_file_path = public_path("mix-manifest.json")
        if os.path.exists(manifest_file_path):
            hasher = hashlib.md5()
            with open(manifest_file_path, "rb") as manifest_file:
                buf = manifest_file.read()
                hasher.update(buf)
            return hasher.hexdigest()

    def set_root_view(self, request):
        """Can be overriden."""
        return config("inertia.root_view")
