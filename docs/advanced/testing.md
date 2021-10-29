---
description: Unit test your Masonite/Inertia application server-side !
---

# Testing

This adapter comes with handy test assertions that you can use as you would use normal Masonite routes/views assertions.

### Test Assertions

- assertIsInertia\(\)
- assertInertiaComponent\(\)
- assertInertiaHasProp\(\)
- assertInertiaMissingProp\(\)
- assertInertiaPropsCount\(\)
- assertInertiaVersion\(\)
- assertInertiaRootView\(\)
- withInertia\(\):
  - component()
  - has()
  - hasCount()
  - missing()
  - url()
  - version()
  - dump()
  - dd()

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
            },
            custom_root_view="my_app"
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

### assertInertiaMissingProp\(key\)

Assert that the given prop is not present in props. Nested notations can be used.

```python
self.get("/")
    .assertInertiaMissingProp("unknown")
    .assertInertiaMissingProp("extra.c")
```

### assertInertiaPropsCount\(count\)

Assert iterable count for a given prop.

```python
self.get("/")
    .assertInertiaPropsCount("extra", 2)
    .assertInertiaPropsCount("keys", 0)
```

### assertInertiaVersion\(version\)

Assert inertia assets version is equal to given version.

```python
self.get("/").assertInertiaVersion("123456")
```

### assertInertiaRootView\(view\)

Assert inertia root view is equal to given view

```python
self.get("/").assertInertiaVersion("my_app")
```

### withInertia\(\)

Assert that the route returned an inertia response and return an inertia testing object to ease further testing assertions.

```python
self.get("/").withInertia()
    .component("Events/Show")
    .has("extra.a", "b")
    .hasCount("keys", 0)
    .url("/")
    .missing("unknown")
    .version("123456")
```

### withInertia\(\).dump()

Dump component name, url, props data and version of the returned response to the console.

### withInertia\(\).dd()

Same as above `dump()` command but will fail and stop the test when executed.
