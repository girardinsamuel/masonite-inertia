# Redirects

When making a non-GET Inertia request, via `<inertia-link>` or manually, be sure to always respond with a proper Inertia response.

For example, if you're creating a new user, have your "store" endpoint return a redirect back to a standard GET endpoint, such as your user index page.

Inertia will automatically follow this redirect and update the page accordingly. Here's a simplified example.

```python
app/http/controllers/UsersController.py


class UsersController(Controller):

    def index(self, view: Inertia):
        return view.render("Users/Index", {
            "users": User.all().serialize()
        })

    def store(self, view: Inertia, response: Response):
        errors = self.request.validate(
            validate.required(["name", "email"]),
            validate.length(["name", "email"], max=50),
            validate.email("email")
        )
        if errors:
            return response.redirect("users.create")
                .with_errors(errors)
                .with_input()

        return response.redirect("users")
```

## External redirects

Sometimes it's necessary to:

* redirect to an external website
* or even another non-Inertia endpoint in your app, within an Inertia request.

This is possible using a server-side initiated `window.location` visit

```python
url = "https://docs.masoniteproject.com"
return view.location(url)
```

This will generate a `409 Conflict` response, which includes the destination URL in the `X-Inertia-Location` header. Client-side, Inertia will detect this response and automatically do a `window.location = url` visit.

