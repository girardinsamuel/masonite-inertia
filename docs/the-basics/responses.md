# Responses

## Creating responses

To create a "Inertia" view your controller method should send the name of Javascript page component as well as any props for the page. If you're using for example Vue.js on client-side the controller would pass some props to the given Vue.js component. The props are equivalent to the context that you can pass to a normal Masonite view.

{% hint style="info" %}
To make an Inertia response, use the Inertia **render** function. This method takes the component name, and allows you to pass props.
{% endhint %}

{% code title="app/http/controllers/EventsController.py" %}
```python
from masonite.controllers import Controller
from masonite.inertia import InertiaResponse

from app.Event import Event


class EventsController(Controller):
    
    def show(self, view: InertiaResponse):
        
        return view.render("Events/Show", {
            "event": Event.find(self.request.param("id")).serialize()
        })
```
{% endcode %}

In this example we're passing a single prop, called `event` to the `Event/Show` page component.

### render\(\)

```python
render(self, component, props={}, custom_root_view="app")
```

