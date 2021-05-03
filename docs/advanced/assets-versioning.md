# Assets versioning

By default masonite-inertia adapter will compute sensible version based on a hash of the compiled assets declared in `webpack.mix.js`.

You can override this behaviour to provide your own logic to compute assets version when they change. This can be any `string` \(letters, numbers, or a file hash\), as long as it changes when your assets have been updated.

### Global configuration via middleware

The `version()` method can be overriden in [custom inertia middleware](configuration.md#overriding-middleware).

### On-the-fly configuration

You can resolve inertia instance from the container and then call the `version()` method.

{% code title="" %}
```python
application.make("inertia").version("123")

# a callable can be provided too

def compute_version():
    return "123"

application.make("inertia").version(compute_version)
```
{% endcode %}

