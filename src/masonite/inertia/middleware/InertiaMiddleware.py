import hashlib
import os
from masonite.middleware import Middleware
from masonite.utils.structures import load
# from masonite.utils.location import public_path
from ..helpers import inertia as inertia_view_helper


# TODO: move this as a PR into M4
def public_path(relative_path, absolute=True):
    from os.path import join, abspath
    """Build the absolute path to the given relative_path assuming it exists in the configured
    migrations location. The relative path can be returned instead by setting absolute=False."""
    relative_dir = join("tests/integrations/public", relative_path)
    return abspath(relative_dir) if absolute else relative_dir


class InertiaMiddleware(Middleware):
    """Inertia Middleware to check whether this is an Inertia request."""

    root_view = "app"

    def before(self, request, response):
        inertia = request.app.make("inertia")
        if not inertia.get_version():
            inertia.version(self.version(request))
        inertia.share(self.share(request))
        inertia.set_root_view(self.set_root_view(request))
        request.app.make("view").share({"inertia": inertia_view_helper})


    def after(self, request, response):
        self.check_version(request, response)
        response = self.change_redirect_code(request, response)
        return response

    def is_inertia_request(self, request):
        if request.header("X-Inertia"):
            return request.header("X-Inertia").value
        return False

    def check_version(self, request, response):
        """In the event that the assets change, initiate a client-side location visit
        to force an update."""
        inertia = request.app.make("inertia")
        version_header = request.header("X-Inertia-Version").value if request.header("X-Inertia-Version") else ""
        if (
            self.is_inertia_request(request)
            and request.get_request_method() == "GET"
            and str(version_header) != inertia.get_version()
        ):
            # TODO: implements reflash/keep in M4
            # if ($request->hasSession()) {
            #     $request->session()->reflash();
            # }
            return inertia.location(request.get_path())

        return response

    def change_redirect_code(self, request, response):
        if self.is_inertia_request(request) and response.is_status(302) and request.get_request_method() in ("PUT", "PATCH", "DELETE"):
            response.status(303)
        return response

    def get_session(self, request):
        # TODO: how to get current session driver, not hard coding cookie
        return request.app.make("session").driver("cookie")

    def resolve_validation_errors(self, request):
        """Get validation errors in flash session if any and serialize it to be easy to use
        client-side."""
        # TODO:
        session = self.get_session(request)
        if not session.has("errors"):
            return {}
        else:
            # TODO: fix this
            # return session.get_error_messages()
            return {}

        # return (object) collect($request->session()->get('errors')->getBags())->map(function ($bag) {
        #     return (object) collect($bag->messages())->map(function ($errors) {
        #         return $errors[0];
        #     })->toArray();
        # })->pipe(function ($bags) use ($request) {
        #     if ($bags->has('default') && $request->header('x-inertia-error-bag')) {
        #         return [$request->header('x-inertia-error-bag') => $bags->get('default')];
        #     } elseif ($bags->has('default')) {
        #         return $bags->get('default');
        #     } else {
        #         return $bags->toArray();
        #     }
        # });

    def share(self, request):
        """Defines the props that are shared by default. Can be overriden."""
        errors = self.resolve_validation_errors(request)
        return {"errors": errors}

    def version(self, request):
        """Determines the current asset version. Can be overriden."""
        assets_url = load(request.app.make("config.inertia")).PUBLIC_PATH
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
        return self.root_view
