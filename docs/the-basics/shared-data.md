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

## Flash messages \(UPDATE for M4\)

In order for your server-side validation errors to be available client-side, Masonite adapter shares flash messages **automatically** through an `errors` prop and a `success` prop.

It means that when you flash a message in session in your controller, the message will be available client-side \(in your e.g. Vue.js component\).

```python
self.request.session.flash("success", "User created.")
self.request.session.flash("errors", "An error occured.")
```

With the Vue adapter you would then access the messages with

```javascript
$page.props.success; // == "User created."
$page.props.errors; // == "An error occured."
```

You can disable flash messages automatic sharing in [inertia configuration](../advanced/configuration.md) by setting `INCLUDE_FLASH_MESSAGES` to `False`. If disabled globally, but you want to share a message in some places in a controller you can do it manually by returning the message as a prop.

If you want to update the automatic share messages logic you could disable it and then use the global sharing data feature to get message from session and share it with prop name and logic you would have chosen. This could look like

{% code title="app/providers/MyAppProvider.py" %}
```python
from masonite.provider import ServiceProvider
from masonite.request import Request


class MyAppProvider(ServiceProvider):
    """Custom app provider to configure app"""

    wsgi = False

    def boot(self, request: Request):

        # share flash messages from sessions
        request = self.container.make("request")
        self.app.make('Inertia').share({
            'messages': {
                'errors': request.session.get_flashed("errors"),
                'success': request.session.get_flashed("success"),
                'warnings': request.session.get_flashed("warnings"),
            }
        })
```
{% endcode %}

