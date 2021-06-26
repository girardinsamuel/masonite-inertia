---
description: With Inertia all routing is defined server-side.
---

# Routing

## Generating URLs

To avoid hard-coding URLs path into your application client-side it would be good if Masonite could send the routes information. There are different options you can use.

### Generate server-side and send them as props

Here the url to create a user is generated in the controller and sent to client through the prop `create_url`.

```python
from masonite.routes import Router

class UsersController(Controller):

    def index(self, view: InertiaResponse, router: Router):
        return view.render(
            "Users/Index",
            {
                "users": User.all().serialize(),
                "create_url": router.route("users.create"),
            },
        )
```

### Generated as JSON and include in view

You can also generate all your routes \(or a selection\) as a JSON payload that you will include into your view.

To help you in the process you can use the small package [masonite-js-routes](https://github.com/girardinsamuel/masonite-js-routes). It provides a `routes()` helper that you can use in your view to include the routes client-side. After installing the package you just have to add this to your view.

{% code title="app.html" %}

```markup
<head>
    <!-- ... -->
    {{ routes() }}
<head>
```

{% endcode %}

It will actually generate this

```javascript
var Routes = {
  namedRoutes: {
    home: { uri: "/", methods: ["GET", "HEAD"], domain: null },
    login: { uri: "login", methods: ["GET", "HEAD"], domain: null },
    users: { uri: "users", methods: ["GET", "HEAD"], domain: null },
    "users.create": { uri: "users", methods: ["POST", "HEAD"], domain: null },
  },
  baseUrl: "http://your-app.com/",
  baseProtocol: "http",
  baseDomain: "your-app.com",
  basePort: false,
};

export { Routes };
```

Then you're free to use this global variable into your client-side application to get route path from the name.

Hopefully an existing package called [ziggy-js](https://github.com/tighten/ziggy) can be installed to provide some javascript helpers that can parse this `Routes` variable.

```javascript
route("home"); // 'https://your-app.com/
route("users.create"); // 'https://your-app.com/users'
```
