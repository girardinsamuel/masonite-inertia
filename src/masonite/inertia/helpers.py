from markupsafe import Markup
import json


def inertia(page_data, app_id="app"):
    """Inertia view helper to render a div with page data required by client-side
    Inertia.js adapter."""
    return Markup(f"<div id='{app_id}' data-page='{json.dumps(page_data)}'></div>")
