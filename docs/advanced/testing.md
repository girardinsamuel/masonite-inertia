---
description: Unit test your Masonite/Inertia application server-side !
---

# Testing

This adapter comes with handy test assertions that you can use as you would use normal Masonite routes/views assertions.

### Test Assertions

* assertIsInertia\(\)
* assertInertiaComponent\(\)
* assertInertiaHasProp\(\)
* assertInertiaMissingProp\(\)
* assertInertiaPropsCount\(\)
* assertInertiaPropsExact\(\)
* assertInertiaSharedHas\(\)
* assertInertiaSharedHasExact\(\)
* assertInertia\(\)

Let's use this route as an example

{% code title="app/http/controllers/EventsController.py" %}
```python

Route.get("/", "ExampleController@show")


class ExampleController(Controller):

    def show(self, view: Inertia):

        return view.render("Events/Show", {
            "events": Event.all().serialize(),
            "keys": [],
            "extra": {
                "a": "b"
                "e": {"hello": "world"}
            } 
        })
```
{% endcode %}

### assertIsInertia\(\)

Assert that the route returned an inertia response.

```python
self.get("/").assertIsInertia()
```

### assertInertiaComponent\(\)

Assert that the given component name is used.

```python
self.get("/").assertIsInertiaComponent("Events/Show")
```

### assertInertiaHasProp\(key, value=None\)

Assert that the given prop is present in props. The prop value can be asserted too. Nested notations can be used.

```python
self.get("/")
    .assertIsInertiaHasProp("events")
    .assertIsInertiaHasProp("keys", [])
    .assertIsInertiaHasProp("extra.e.hello")
    .assertIsInertiaHasProp("extra.a", "b")
```

