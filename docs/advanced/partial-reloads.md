# Partial reloads

You can find all details in [Official documentation](https://inertiajs.com/partial-reloads).

For partial reloads to be most effective, be sure to also use lazy data evaluation server-side.

This can be done by wrapping all optional page data in a callable or the adapter lazy function. When Inertia performs a visit, it will determine which data is required, and only then will it call the function. This can significantly increase the performance of pages with a lot of optional data.

{% code title="app/http/controllers/UsersController.py" %}
```python
from masonite.inertia import lazy

def show(self, view: InertiaResponse):

    def get_users(request):
        return User.all().serialize()

    return view.render("Users/Index", {
        # ALWAYS included on first visit
        # OPTIONALLY included on partial reloads
        # ALWAYS evaluated
        'users': User.all().serialize(),

        # ALWAYS included on first visit
        # OPTIONALLY included on partial reloads
        # ONLY evaluated when needed
        'users': lambda: _: User.all().serialize(),
        # above can also written as
        'users': get_users
        
        # NEVER included on first visit
        # OPTIONALLY included on partial reloads
        # ONLY evaluated when needed
        'users': lazy(get_users)
    })
```
{% endcode %}

{% hint style="info" %}
For convenience, the `request` argument will be automatically passed to lazy loaded props. In the example above the `get_users` will receive the request object \(even if not used\).
{% endhint %}

