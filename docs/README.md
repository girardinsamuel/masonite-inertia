# Introduction and installation

{% hint style="warning" %}
WORK IN PROGRESS ! Coming soon in January 2021, stay tuned !
{% endhint %}

Welcome to the documentation for [masonite-inertia](https://github.com/girardinsamuel/masonite-inertia) adapter for [MasoniteFramework](https://docs.masoniteproject.com/) and [Inertia.js](https://inertiajs.com/). 

## Why an other doc ?

The existing documentation is really good but documents only official Laravel and Rails server side adapters. Here, you will find mostly the same content but written for MasoniteFramework ! 

This documentation is off course based on official [Inertia.js documentation](https://inertiajs.com/), but will only explains how to use Inertia.js with MasoniteFramework and won't explain again how to configure and use it client-side as it's already covered in official documentation.

{% hint style="info" %}
Throughout the documentation, you will see that code examples are the same as the official server-side documentation in order to ease the understanding. If something is not clear please first go to official documentation to check if more details are given.
{% endhint %}

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

