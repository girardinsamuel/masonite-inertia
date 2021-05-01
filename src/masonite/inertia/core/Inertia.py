import html
import json
from inspect import signature
from src.masonite.inertia.core.Lazy import LazyProp
from masonite.utils.helpers import flatten
from masonite.utils.structures import load


def load_callable_props(d, request):
    for k, v in d.items():
        if isinstance(v, dict):
            load_callable_props(v, request)
        elif callable(v):
            # evaluate prop and pass request if prop accept it
            if len(signature(v).parameters) > 0:
                d[k] = v(request)
            else:
                d[k] = v()
        elif isinstance(v, LazyProp):
            if len(signature(v.callable).parameters) > 0:
                d[k] = v(request)
            else:
                d[k] = v()


class Inertia:
    def __init__(self, application, config={}):
        self.application = application
        self.root_view = load("inertia.root_view")
        self.shared_props = {}
        self.rendered_template = ""
        self._version = ""
        # parameters
        self.config = config
        # self.include_flash_messages = load("inertia.include_flash_messages")
        # self.include_routes = load("inertia.include_routes")
        if self.config.INCLUDE_ROUTES:
            self._load_routes()

    def set_configuration(self, config):
        self.config = config
        return self

    def set_root_view(self, root_view):
        self.root_view = root_view

    def _load_routes(self):
        from routes.web import ROUTES

        self.routes = {}
        for route in flatten(ROUTES):
            if route.named_route:
                self.routes.update({route.named_route: route.route_url})

    def render(self, component, props={}, custom_root_view=None):
        request = self.application.make("request")
        page_data = self.get_page_data(component, props)

        if request.header("X-Inertia"):
            response = self.application.make("response")
            response.header("X-Inertia", "true")
            response.header("Vary", "Accept")
            return response.json(page_data)

        return self.application.make("view").render(
            custom_root_view if custom_root_view else self.root_view,
            {"page": html.escape(json.dumps(page_data))}
        )

    def location(self, url):
        response = self.application.make("response")
        response.header("X-Inertia-Location", url)
        response.status(409)
        response.content = b""
        return b""

    def get_page_data(self, component, props):
        # merge shared props with page props (lazy props are resolved now)
        request = self.application.make("request")
        props = {**self.get_props(props, component), **self.get_shared_props()}

        # lazy load props and make request available to props being lazy loaded
        load_callable_props(props, request)

        page_data = {
            "component": self.get_component(component),
            "props": props,
            "url": request.get_path(),
            "version": self.get_version(),
        }
        if self.config.INCLUDE_ROUTES:
            page_data.update({"routes": self.routes})

        return page_data

    def get_shared_props(self, key=None):
        """Get all Inertia shared props or the one with the given key."""
        if key:
            return self.shared_props.get(key, None)
        else:
            return self.shared_props

    def version(self, version):
        self._version = version

    def get_version(self):
        if callable(self._version):
            version = self._version()
        else:
            version = self._version
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
        only_props_header = request.header("X-Inertia-Partial-Data")
        partial_component_header = request.header("X-Inertia-Partial-Component") or {"name": ""}
        is_partial = only_props_header and partial_component_header.value == component
        props = {}

        if (is_partial):
            only_props = only_props_header.value
            for key in all_props:
                if key in only_props:
                    props.update({key: all_props[key]})
        else:
            # remove lazy props
            for prop_key, value in all_props.items():
                if not isinstance(value, LazyProp):
                    props.update({prop_key: value})

        # add adapter data to props
        props.update({"auth": self.get_auth()})

        if self.config.INCLUDE_FLASH_MESSAGES:
            props.update({"messages": self.get_messages()})
        if self.config.INCLUDE_ROUTES:
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
            return {"user": ""}
        return {"user": user.serialize()}

    def get_messages(self):
        session = self.application.make("session").driver("cookie")
        return session.get_flashed_messages()

    def get_errors(self):
        session = self.application.make("session").driver("cookie")
        import pdb;pdb.set_trace()
        return session.get_error_messages()

    def get_component(self, component):
        return html.escape(component)
