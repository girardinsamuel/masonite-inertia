---
description: Via the configuration file and/or a custom middleware.
---

# Configuration

### Configuration file

The package can be globally configured via `config/inertia.py` configuration file.

| Variable         | Description                                                                                                                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PUBLIC_PATH`    | <p>Absolute path to mix-manifest.json location. It's needed for computing js assets version.</p><p>Default: <code>project root</code></p>                                                                                                       |
| `ROOT_VIEW`      | <p>Global root template view used by your Inertia Controllers to render the page. Specify the name of the view without <code>.html</code>. See <a href="root-view.md#global-configuration">Root view</a>.</p><p>Default: <code>"app"</code></p> |
| `INCLUDE_ROUTES` | <p>Include server-side routes as JSON payload in Inertia response (as a prop). See <a href="../the-basics/routing.md#generated-as-json-and-include-in-view">routing</a>.</p><p>Default: <code>False</code></p>                                  |

### Overriding Middleware

The \`InertiaMiddleware\` can be overriden to define the root view and the way assets version is computed. You just have to create a middleware in your app inheriting from the \`InertiaMiddleware\` class.

{% code title="app/http/middleware/HandleInertiaRequests.py" %}
```python
from masonite.inertia import InertiaMiddleware

class HandleInertiaRequests(InertiaMiddleware):
    
    root_view = "other_app"
    
    def version(self, request):
         return "123"
```
{% endcode %}

Then include this middleware in the HTTP middleware instead of the original one.
