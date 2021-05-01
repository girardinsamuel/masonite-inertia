import html
import json
from jinja2.exceptions import TemplateNotFound
from masonite.views import View
from src.masonite.inertia.helpers import inertia as inertia_helper


class InertiaResponse(View):

    def __init__(self, container, page_data, root_view):
    # def __init__(self, component, props, root_view="app", version=None):
    #     self.component = component
    #     self.props = props
    #     self.root_view = root_view
    #     self.version = version
        super().__init__(container)

        # inertia specifics
        self.component = page_data["component"]
        self.props = page_data["props"]
        self.root_view = root_view
        self.version = page_data["version"]
        self.page_data = page_data
        self.add(container.make("views.location"))
        self.share({"inertia": inertia_helper})

    def render(self):
        return super().render(self.root_view, {"page": self.page_data})

    def _render(self):
        # serialize and escape page data here to keep original dictionary as dict
        page_payload = html.escape(json.dumps(self.page_data))
        dictionary = {**self.dictionary, "page": page_payload}
        try:
            # Try rendering the template with '.html' appended
            return self.env.get_template(self.filename).render(dictionary)
        except TemplateNotFound:
            # Try rendering the direct template the user has supplied
            return self.env.get_template(self.template).render(dictionary)
