# Installation

## Requirements

- a Masonite 4 project
- a Node.js environment

## Installation

Install the latest Inertia server-side adapter in your project

```
pip install masonite-inertia
```

{% hint style="warning" %}
`masonite-inertia 4.X` versions are for Masonite 4. `masonite-inertia 3.X` versions are for Masonite 3.
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

Add the Inertia middleware to your project

```python
from masonite.inertia import InertiaMiddleware


class HandleInertiaRequests(InertiaMiddleware):
```

{% hint style="warning" %}
It's important to put this middleware before the `EncryptCookies` middleware !
{% endhint %}

{% code title="config/middleware.py" %}

```python
# ...
http_middleware = [
    #...,
    HandleInertiaRequests,
    EncryptCookies
]
```

{% endcode %}

Finally you can (optionally) publish the package configuration file to your project if you want to
change some configuration parameters:

```python
python craft package:publish inertia
```

You should now have a configuration file `inertia.py` in your project configuration folder.

You're ready to start working with Inertia !
