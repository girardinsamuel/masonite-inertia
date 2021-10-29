from jinja2 import Markup


def inertia(page_data, app_id="app"):
    """Inertia view helper to render a div with page data required by client-side
    Inertia.js adapter."""
    return Markup("<div id='{0}' data-page='{1}'></div>".format(app_id, page_data))
