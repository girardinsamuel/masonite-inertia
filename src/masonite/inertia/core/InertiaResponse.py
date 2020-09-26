import html
import json
import os

from masonite.inertia.core.InertiaAssetVersion import inertia_asset_version
from masonite.helpers import compact
from masonite.helpers.routes import flatten_routes
from masonite.response import Responsable


class InertiaResponse(Responsable):
    def __init__(self, container):
        self.container = container
        self.request = self.container.make("Request")
        self.view = self.container.make("View")
        self.root_view = "app"
        self.shared_props = {}
        self.rendered_template = ""
        self.load_routes()

    def set_root_view(self, root_view):
        self.root_view = root_view

    def load_routes(self):
        from routes.web import ROUTES

        self.routes = {}
        for route in flatten_routes(ROUTES):
            if route.named_route:
                self.routes.update({route.named_route: route.route_url})

    def render(self, component, props={}):
        page_data = self.get_page_data(component, props)

        if self.request.is_inertia:
            self.rendered_template = json.dumps(page_data)
            return self

        self.rendered_template = self.view(
            self.root_view, {"page": html.escape(json.dumps(page_data))}
        ).rendered_template

        return self

    def get_response(self):
        return self.rendered_template

    def get_page_data(self, component, props):
        # merge shared props with page props (lazy props are resolved now)
        props = {**self.get_props(props), **self.get_shared_props()}

        def load_lazy_props(d):
            for k,v in d.items():
                if isinstance(v, dict):
                    load_lazy_props(v)
                elif callable(v):
                    d[k] = v()
        load_lazy_props(props)

        return {
            "component": self.get_component(component),
            "props": props,
            "url": self.request.path,
            "version": inertia_asset_version(),
            "routes": self.routes,
        }

    def get_shared_props(self, key=None):
        if key:
            return self.shared_props.get(key, None)
        else:
            return self.shared_props

    def share(self, key, value=None):
        if isinstance(key, dict):
            self.shared_props = {**self.shared_props, **key}
        else:
            self.shared_props.update({key: value})

    def get_props(self, props):
        # if partial reload, only use given props
        """
                $only = array_filter(explode(',', $request->header('X-Inertia-Partial-Data')));

        $props = ($only && $request->header('X-Inertia-Partial-Component') === $this->component)
            ? Arr::only($this->props, $only)
            : $this->props
        """
        import pdb
        pdb.set_trace()
        only_props = self.request.header("X-Inertia-Partial-Data")
        if only_props and self.request.header("X-Inertia-Partial-Component") == self.component:
            pass

        # add adapter data to props
        props.update({"errors": self.get_errors()})
        props.update({"auth": self.get_auth()})
        props.update({"messages": self.get_messages()})
        props.update({"routes": self.routes})
        return props

    def get_auth(self):
        user = self.request.user()

        csrf = self.request.get_cookie("csrf_token", decrypt=False)

        self.request.cookie("XSRF-TOKEN", csrf, http_only=False, encrypt=False)

        if not user:
            return {"user": None}

        user.__hidden__ = ["password", "remember_token"]
        # @josephmancuso, what is self meta attribute ? It gives me error when querying user
        # user.set_appends(["meta"])

        return {"user": user.serialize()}

    def get_messages(self):
        return {
            "success": (self.request.session.get("success") or ""),
            "error": (self.request.session.get("error") or ""),
            "danger": (self.request.session.get("danger") or ""),
            "warning": (self.request.session.get("warning") or ""),
            "info": (self.request.session.get("info") or ""),
        }

    def get_errors(self):
        return self.request.session.get("errors") or {}

    def get_component(self, component):
        return html.escape(component)
