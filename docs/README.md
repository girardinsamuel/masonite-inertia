# Introduction and installation

Documentation for [masonite-inertia](https://github.com/girardinsamuel/masonite-inertia) adapter for MasoniteFramework and [Inertia.js](https://inertiajs.com/).

The existing documentation is really good but documents only official Laravel and Rails server side adapters. You will find mostly the same content but written for MasoniteFramework !

This documentation is a work in progress  ! Coming soon in January 2021 !

## Requirements

* a Masonite 3 or 2.X project
* a Node.js environment

## Installation

Install the Inertia server-side adapter in your project.

{% tabs %}
{% tab title="Masonite 3" %}
```text
pip install masonite-inertia
```
{% endtab %}

{% tab title="Masonite 2" %}
```text
pip install 'masonite-inertia < 3'
```
{% endtab %}
{% endtabs %}

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

Add `InertiaMiddleware` to your project

{% code title="config/middleware.py" %}
```python
# ...
from masonite.inertia import InertiaMiddleware

HTTP_MIDDLEWARE = [
    LoadUserMiddleware,
    CsrfMiddleware,
    #...
    InertiaMiddleware,
]
```
{% endcode %}

Finally publish the package configuration file to your project

```python
python craft install:inertia
```

You should now have a configuration file `config/inertia.py` .

You're ready to start working with Inertia !

