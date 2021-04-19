import hashlib
import os
from masonite.middleware import Middleware
from masonite.utils.structures import load
from masonite.utils.location import public_path

from masonite.inertia.core.InertiaResponse import InertiaResponse


class InertiaMiddleware(Middleware):
    """Inertia Middleware to check whether this is an Inertia request."""

    root_view = "app"

    def before(self, request, response, inertia: InertiaResponse):
        inertia.version(self.version(request))
        inertia.share(self.share(request))
        inertia.set_root_view(self.set_root_view(request))

    def after(self, request, response, inertia: InertiaResponse):
        response = self.check_version(request, response, inertia)
        response = self.change_redirect_code(request, response)
        return response

    def is_inertia_request(self, request):
        return request.header("X-Inertia")

    def check_version(self, request, response, inertia):
        """In the event that the assets change, initiate a client-side location visit
        to force an update."""
        if (
            self.is_inertia_request(request)
            and request.get_request_method() == "GET"
            and request.header("X-Inertia-Version") != inertia.get_version()
        ):
            # TODO: implements reflash/keep in M4
            # TODO: how to get current session driver, not hard coding cookie
            session = request.app.make("session").driver("cookie")
            # if ($request->hasSession()) {
            #     $request->session()->reflash();
            # }
            return inertia.location(request.get_path())

        return response

    def change_redirect_code(self, request, response):
        if self.is_inertia_request(request) and response.is_status(302) and request.get_request_method() in ("PUT", "PATCH", "DELETE"):
            response.status(303)
        return response

    def resolve_validation_errors(self, request):
        """Get validation errors in flash session if any and serialize it to be easy to use
        client-side."""
        # TODO:
        # if (! $request->session()->has('errors')) {
        #     return (object) [];
        # }

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
        return {}

    def share(self, request):
        """Defines the props that are shared by default. Can be overriden."""
        errors = self.resolve_validation_errors(request)
        return {"errors": errors}

    def version(self, request):
        """Determines the current asset version. Can be overriden."""
        assets_url = load(self.application.make("config.inertia")).PUBLIC_PATH
        if assets_url:

            return

        manifest_file_path = public_path("mix-manifest.json")
        if os.path.exists(manifest_file_path):
            hasher = hashlib.md5()
            with open(manifest_file_path, "rb") as manifest_file:
                buf = manifest_file.read()
                hasher.update(buf)
            return hasher.hexdigest()
        # if (config('app.asset_url')) {
        #     return md5(config('app.asset_url'));
        # }

        # if (file_exists($manifest = public_path('mix-manifest.json'))) {
        #     return md5_file($manifest);
        # }

    def set_root_view(self, request):
        """Can be overriden."""
        return self.root_view
