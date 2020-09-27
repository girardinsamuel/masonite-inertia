from jinja2 import Markup


def inertia(page_data):
    return Markup("<div id='app' data-page='{0}'></div>".format(page_data))
