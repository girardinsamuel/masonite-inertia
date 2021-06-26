# Installation

## Requirements

- a Masonite 4 project
- a Node.js environment

## Installation

Install the latest Inertia server-side adapter in your project

```text
pip install masonite-inertia
```

{% hint style="warning" %}
`masonite-inertia 4.X` versions are for Masonite 4.
`masonite-inertia 3.X` versions are for Masonite 3.
{% endhint %}

Add `InertiaProvider` to your project

{% code title="config/providers.py" %}

```python
# ...
from masonite.inertia import InertiaProvider

PROVIDERS = [
    # ...

    # Third Party Providers
    InertiaProvider,
]
```

{% endcode %}

Publish the `HandleInertiaRequests` to your project.
TODO:
For now, just create a new middleware in your project:

```python
from masonite.inertia import InertiaMiddleware


class HandleInertiaRequests(InertiaMiddleware):
```

{% code title="config/middleware.py" %}

And add this middleware as the last item of your middleware stack (located in `Kernel` config):

```python
# ...
http_middleware = [
    #...,
    HandleInertiaRequests
]
```

{% endcode %}

Finally publish the package configuration file to your project

```python
python craft install:inertia
```

You should now have a configuration file `config/inertia.py`.

You're ready to start working with Inertia !
