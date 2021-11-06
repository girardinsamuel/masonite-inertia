import html
from inspect import signature

from masonite.utils.collections import flatten
from masonite.utils.structures import data_get, load

from .InertiaResponse import InertiaResponse
from .Lazy import LazyProp


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
    def __init__(self, application, options={}):
        self.application = application
        self.shared_props = {}
        self.rendered_template = ""
        self._version = ""
        self.options = options
        self.root_view = options.get("root_view")
        if self.options.get("include_routes"):
            self._load_routes()

    def set_configuration(self, options):
        self.options = options
        return self

    def set_root_view(self, root_view):
        self.root_view = root_view

    def _load_routes(self):
        routes = (load(self.application.make("routes.location"), "ROUTES", []),)
        self.routes = {}
        for route in flatten(routes):
            if route._name:
                self.routes.update({route._name: route.url})

    def render(self, component, props={}, custom_root_view=None):
        request = self.application.make("request")
        page_data = self.get_page_data(component, props)

        if request.header("X-Inertia"):
            response = self.application.make("response")
            response.header("X-Inertia", "true")
            response.header("Vary", "Accept")
            return response.json(page_data)
        return InertiaResponse(
            self.application,
            page_data,
            custom_root_view if custom_root_view else self.root_view,
        ).render()

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
        if self.options.get("include_routes"):
            page_data.update({"routes": self.routes})

        return page_data

    def get_shared_props(self, key=None, default=None):
        """Get all Inertia shared props or the one with the given key."""
        if key:
            return data_get(self.shared_props, key, default)
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

    def flush_shared(self):
        self.shared_props = {}

    def get_props(self, all_props, component):
        """Get props to return to the page:
        - when partial reload, required return 'only' props
        - add adapter props along view props (errors, message, auth ...)"""

        request = self.application.make("request")

        # partial reload feature
        only_props_header = request.header("X-Inertia-Partial-Data")
        partial_component_header = request.header("X-Inertia-Partial-Component") or {"name": ""}
        is_partial = only_props_header and partial_component_header == component
        props = {}

        if is_partial:
            only_props = only_props_header
            for key in all_props:
                if key in only_props:
                    props.update({key: all_props[key]})
        else:
            for prop_key, value in all_props.items():
                if not isinstance(value, LazyProp):
                    props.update({prop_key: value})

        # add adapter data to props
        props.update({"auth": self.get_auth()})

        if self.options.get("include_routes"):
            props.update({"routes": self.routes})
        return props

    def get_auth(self):
        user = self.application.make("auth").guard("web").user()
        if not user:
            return {"user": ""}
        return {"user": user.serialize()}

    def get_component(self, component):
        # TODO: check if escaping before here is needed
        return html.escape(component)
