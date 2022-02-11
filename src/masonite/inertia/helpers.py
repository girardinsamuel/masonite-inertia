from markupsafe import Markup


def inertia(page_data, app_id="app"):
    """Inertia view helper to render a div with page data required by client-side
    Inertia.js adapter."""
    return Markup(f'<div id="{app_id}" data-page="{page_data}"></div>')
