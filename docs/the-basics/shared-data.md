# Shared data

## Sharing data

The server-side adapters provide a way to preassign shared data for each request. Shared data will be automatically merged with the page props provided in your controller.

In Masonite you will typically do it in a `ServiceProvider` that you create in your project.

```python
from masonite.provider import ServiceProvider
from masonite.auth import Auth


class MyAppProvider(ServiceProvider):
    """Custom app provider to configure app"""

    wsgi = False

    def boot(self, auth: Auth):
        
        def get_auth():
            user = auth.user()
            if user:
                return {
                    'user': {
                        'id': user.id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        'role': user.role,
                        'account': {
                            'id': user.account.id,
                            'name': user.account.name
                        }
                    }
                }
            else:
                return {'user': None}
        
        # share data globally in each request
        self.app.make('Inertia').share({
            'auth': get_auth
        })

```

This is done with the `share()` helper. It takes a dict and share this data in every request.

Here you can notice we don't directly share authenticated user but **a callable** returning authenticated user. This will allow to lazy load this prop when doing [partial reloads](../advanced/partial-reloads.md).

{% hint style="danger" %}
Use this feature sparingly as shared data is included with every response. 

Page props and shared data are merged together, so be sure to namespace your shared data appropriately.
{% endhint %}



