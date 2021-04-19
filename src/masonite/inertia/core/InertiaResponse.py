import html
import json
from inspect import signature
from masonite.utils.helpers import flatten
from masonite.response import Response
from masonite.utils.structures import load
from masonite.inertia.core.InertiaAssetVersion import inertia_asset_version


def load_lazy_props(d, request):
    for k, v in d.items():
        if isinstance(v, dict):
            load_lazy_props(v, request)
        elif callable(v):
            # evaluate prop and pass request if prop accept it
            if len(signature(v).parameters) > 0:
                d[k] = v(request)
            else:
                d[k] = v()


class InertiaResponse:
    def __init__(self, application):
        self.application = application
        self.root_view = load("inertia.root_view")
        self.shared_props = {}
        self.rendered_template = ""
        # parameters
        self.include_flash_messages = load("inertia.include_flash_messages")
        self.include_routes = load("inertia.include_routes")
        if self.include_routes:
            self._load_routes()

    def set_root_view(self, root_view):
        self.root_view = root_view

    def _load_routes(self):
        from routes.web import ROUTES

        self.routes = {}
        for route in flatten(ROUTES):
            if route.named_route:
                self.routes.update({route.named_route: route.route_url})

    def render(self, component, props={}, custom_root_view="app"):
        request = self.application.make("request")
        page_data = self.get_page_data(component, props)

        if request.is_inertia:
            # self.rendered_template = json.dumps(page_data)
            return json.dumps(page_data)

        # self.rendered_template = self.view(
        #     custom_root_view if custom_root_view else self.root_view,
        #     {"page": html.escape(json.dumps(page_data))},
        # ).rendered_template

        return self.application.make("view").render(
            custom_root_view if custom_root_view else self.root_view,
            {"page": html.escape(json.dumps(page_data))}
        )

    def location(self, url):
        # TODO: make request with 409 code and X-Inertia-Location: url header
        response = Response(self.application)
        response.header("X-Inertia-Location", url)
        response.status(409)
        return self

    def get_response(self):
        return self.rendered_template

    def get_page_data(self, component, props):
        # merge shared props with page props (lazy props are resolved now)
        request = self.application.make("request")
        props = {**self.get_props(props, component), **self.get_shared_props()}

        # lazy load props and make request available to props being lazy loaded
        load_lazy_props(props, request)

        page_data = {
            "component": self.get_component(component),
            "props": props,
            "url": request.get_path(),
            "version": inertia_asset_version(self.application),
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

    def version(self, version):
        self.version = version

    def get_version(self):
        if callable(self.version):
            version = self.version()
        else:
            version = self.version
        return str(version)

    def share(self, key, value=None):
        if isinstance(key, dict):
            self.shared_props = {**self.shared_props, **key}
        else:
            self.shared_props.update({key: value})

    def get_props(self, all_props, component):
        """Get props to return to the page:
        - when partial reload, required return 'only' props
        - add adapter props along view props (errors, message, auth ...)"""

        request = self.application.make("request")

        # partial reload feature
        only_props = request.header("HTTP_X_INERTIA_PARTIAL_DATA")
        if (
            only_props
            and request.header("HTTP_X_INERTIA_PARTIAL_COMPONENT") == component
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
        request = self.application.make("request")
        # user = request.user()
        user = self.application.make("auth").guard("web").user()
        # TODO: is cookie not automatically added ??
        # csrf = request.cookie("csrf_token")
        # request.cookie("XSRF-TOKEN", csrf, http_only=False, encrypt=False)
        request.cookie("XSRF-TOKEN", request.cookie("csrf_token"))
        if not user:
            return {"user": None}
        return {"user": user.serialize()}

    def get_messages(self):
        request = self.application.make("request")
        return {
            "success": (request.session.get_flashed("success") or ""),
            "error": (request.session.get_flashed("error") or ""),
            "danger": (request.session.get_flashed("danger") or ""),
            "warning": (request.session.get_flashed("warning") or ""),
            "info": (request.session.get_flashed("info") or ""),
        }

    def get_errors(self):
        request = self.application.make("request")
        return request.session.get_flashed("errors") or {}

    def get_component(self, component):
        return html.escape(component)
