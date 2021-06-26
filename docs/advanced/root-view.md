---
description: Customizing the root view
---

# Root view

By default an inertia response is rendering data in the default `app.html` view.

## Global configuration

You can change the name of the view globally in the configuration file

{% code title="config/inertia.py" %}

```python
ROOT_VIEW = "inertia_app"
```

{% endcode %}

Now every inertia responses is going to render content in `inertia_app.html` view.

This can also be done through a [custom inertia middleware](configuration.md#overriding-middleware).

## Local configuration

There are situations where you may want to render content in other view but just e.g. for one controller method. We got you covered !

{% code title="app/http/controllers/HomeController.py" %}

```python
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse


class HomeController(Controller):

    def index(self, view: InertiaResponse):
        """This view will be rendered in 'home.html'."""
        return view.render(
            "Home",
            { "first_name": "Sam" },
            custom_root_view="home"
        )

    def contact(self, view: InertiaResponse):
        """This view will be rendered in 'app.html'."""
        return view.render("Contact")
```

{% endcode %}
