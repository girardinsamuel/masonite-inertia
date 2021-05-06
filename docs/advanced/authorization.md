# Authorization

With Inertia, authorization is best handled server-side in your policies. However, you may be wondering how to check against your policies from within your JavaScript page components, since you won't have access to your server-side helpers. The simplest approach here is to pass your authorization checks as props to your page components.

{% code title="app/http/controllers/UsersController.py" %}
```python
from masonite.auth import Auth
from masonite.inertia import InertiaResponse

class UsersController(Controller):

    def index(self, auth: Auth, view:InertiaResponse):
        return view.render("Users/Index", {
            "can": {
                "create_user": # add custom check with the current user auth.user()
            },
            "users": User.all().serialize()
        })
```
{% endcode %}

