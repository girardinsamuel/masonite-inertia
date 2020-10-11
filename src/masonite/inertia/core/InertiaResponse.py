import html
import json
from masonite.helpers.routes import flatten_routes
from masonite.response import Responsable
from masonite.helpers import config
from masonite.inertia.core.InertiaAssetVersion import inertia_asset_version


def load_lazy_props(d):
    for k, v in d.items():
        if isinstance(v, dict):
            load_lazy_props(v)
        elif callable(v):
            d[k] = v()


class InertiaResponse(Responsable):
    def __init__(self, container):
        self.container = container
        self.request = self.container.make("Request")
        self.view = self.container.make("View")
        self.root_view = config("inertia.root_view")
        self.shared_props = {}
        self.rendered_template = ""
        # parameters
        self.include_flash_messages = config("inertia.include_flash_messages")
        self.include_routes = config("inertia.include_routes")
        if self.include_routes:
            self._load_routes()

    def set_root_view(self, root_view):
        self.root_view = root_view

    def _load_routes(self):
        from routes.web import ROUTES

        self.routes = {}
        for route in flatten_routes(ROUTES):
            if route.named_route:
                self.routes.update({route.named_route: route.route_url})

    def render(self, component, props={}, custom_root_view=None):
        page_data = self.get_page_data(component, props)

        if self.request.is_inertia:
            self.rendered_template = json.dumps(page_data)
            return self

        self.rendered_template = self.view(
            custom_root_view if custom_root_view else self.root_view,
            {"page": html.escape(json.dumps(page_data))},
        ).rendered_template

        return self

    def location(self, url):
        # TODO: make request with 409 code and X-Inertia-Location: url header
        self.request.header("X-Inertia-Location", url)
        self.request.status(409)
        # self.rendered_template = self.view("").rendered_template
        # self.rendered_template = self.view(
        #     custom_root_view if custom_root_view else self.root_view,
        #     {"page": html.escape(json.dumps(page_data))},
        # ).rendered_template
        return self

    def get_response(self):
        return self.rendered_template

    def get_page_data(self, component, props):
        # merge shared props with page props (lazy props are resolved now)
        props = {**self.get_props(props, component), **self.get_shared_props()}
        load_lazy_props(props)

        page_data = {
            "component": self.get_component(component),
            "props": props,
            "url": self.request.path,
            "version": inertia_asset_version(),
        }
        if self.include_routes:
            page_data.update({"routes": self.routes})

        return page_data

    def get_shared_props(self, key=None):
        """Get all Inertia shared props or the one with the given key."""
        if key:
            return self.shared_props.get(key, None)
        else:
            return self.shared_props

    def share(self, key, value=None):
        if isinstance(key, dict):
            self.shared_props = {**self.shared_props, **key}
        else:
            self.shared_props.update({key: value})

    def get_props(self, all_props, component):
        """Get props to return to the page:
        - when partial reload, required return 'only' props
        - add adapter props along view props (errors, message, auth ...)"""

        # partial reload feature
        only_props = self.request.header("HTTP_X_INERTIA_PARTIAL_DATA")
        if (
            only_props
            and self.request.header("HTTP_X_INERTIA_PARTIAL_COMPONENT") == component
        ):
            props = {}
            for key in all_props:
                if key in only_props:
                    props.update({key: all_props[key]})
        else:
            props = all_props

        # add adapter data to props
        props.update({"auth": self.get_auth()})
        if self.include_flash_messages:
            props.update({"errors": self.get_errors()})
            props.update({"messages": self.get_messages()})
        if self.include_routes:
            props.update({"routes": self.routes})
        return props

    def get_auth(self):
        user = self.request.user()
        csrf = self.request.get_cookie("csrf_token", decrypt=False)
        self.request.cookie("XSRF-TOKEN", csrf, http_only=False, encrypt=False)
        if not user:
            return {"user": None}
        user.__hidden__ = ["password", "remember_token"]
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
