from jinja2 import Markup


def inertia():
    return Markup("<div id='app' data-page='{{ page | safe }}'></div>")

