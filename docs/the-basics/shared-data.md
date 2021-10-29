# Shared data

## Sharing data

The server-side adapters provide a way to preassign shared data for each request. Shared data will be automatically merged with the page props provided in your controller.

This is done through the `share()` helper. It takes a dict and share this data in every request.

{% hint style="warning" %}
Page props and shared data are merged together, so be sure to namespace your shared data appropriately.
{% endhint %}

### Via Middleware

{% code title="app/http/middleware/HandleInertiaRequests.py" %}
```python
from masonite.inertia import InertiaMiddleware

class HandleInertiaRequests(InertiaMiddleware):
    
    def share(self, request):
    
         def get_auth():
             user = request.user()
             if user:
                 return user.serialize()
             else:
                 return None
                 
         return {"user": get_auth}
```
{% endcode %}

Here you can notice we don't directly share authenticated user but **a callable** returning authenticated user. This will allow to lazy load this prop when doing [partial reloads](../advanced/partial-reloads.md).

### On-the-fly

{% code title="" %}
```python
from masonite.provider import ServiceProvider
from masonite.auth import Auth


application.make("inertia").share({
    "user": "John",
})
```
{% endcode %}

{% hint style="danger" %}
Use this feature sparingly as shared data is included with every response.
{% endhint %}

## Flash messages (UPDATE for M4)

In order for your server-side validation errors to be available client-side, Masonite adapter shares flash errors messages **automatically** through an `errors` prop.

It means that when you flash a message in session in your controller, the message will be available client-side (in your e.g. Vue.js component).

```python
request.session.flash("errors", "An error occured.")
```

With the Vue adapter you would then access the messages with

```javascript
$page.props.errors; // == "An error occured."
```

If you want to update sharing flash messages logic you can override the share method in the `HandleInertiaRequests` middleware.

{% code title="app/middleware/HandleInertiaRequests.py" %}
```python
class HandleInertiaRequests(InertiaMiddleware):
    
    def share(self, request):
        """Defines the props that are shared by default."""
        flashed_messages = request.session.get_flashed_messages()
        errors = flashed_messages.get("errors")
        success = flashed_messages.get("success")
        return {"errors": errors, "success": success}
```
{% endcode %}
