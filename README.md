# Masonite Inertia

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="130px">
<img src="https://avatars1.githubusercontent.com/u/47703742?s=200&v=4" width="130px">
</p>

<p align="center">
  <a href="https://docs.masoniteproject.com">
    <img alt="Masonite Package" src="https://img.shields.io/static/v1?label=Masonite&message=package&labelColor=grey&color=blue&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAAA6gAwAEAAAAAQAAAA4AAAAATspU+QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAnxJREFUKBVNUl1IVEEUPjPObdd1VdxWM0rMIl3bzbVWLSofVm3th0AhMakHHyqRiNSHEAq5b2HSVvoQRUiEECQUQkkPbRslRGigG8auoon2oPSjpev+3PWeZq7eaC5nDt93vplz5txDQJYpNxX4st4JFiwj9aCqmswUFQNS/A2YskrZJPYefkECC2GhQwAqvLYybwXrwBvq8HSNOXRO92+aH7nW8vc/wS2Z9TqneYt2KHjlf9Iv+43wFJMExzO0YE5OKe60N+AOW6OmE+WJTBrg23jjzWxMBauOlfyycsV24F+cH+zAXYUOGl+DaiDxfl245/W9OnVrSY+O2eqPkyz4sVvHoKp9gOihf5KoAVv3hkQgbj/ihG9fI3RixKcUVx7lJVaEc0vnyf2FFll+ny80ZHZiGhIKowWJBCEAKr+FSuNDLt+lxybSF51lo74arqs113dOZqwsptxNs5bwi7Q3q8npSC2AWmvjTncZf1l61e5DEizNn5mtufpsqk5+CZTuq00sP1wkNPv8jeEikVVlJso+GEwRtNs3QeBt2YP2V2ZI3Tx0e+7T89zK5tNASOLEytJAryGtkLc2PcBM5byyUWYkMQpMioYcDcchC6xN220Iv36Ot8pV0454RHLEwmmD7UWfIdX0zq3GjMPG5NKBtv5qiPEPekK2U51j1451BZoc3i+1ohSQ/UzzG5uYFFn2mwVUnO4O3JblXA91T51l3pB3QweDl7sNXMyEjbguSjrPcQNmwDkNc8CbCvDd0+xCC7RFi9wFulD3mJeXqxQevB4prrqgc0TmQ85NG/K43e2UwnMVAJIEBNfWRYR3HfnvivrIzMyo4Hgy+hfscvLo53jItAAAAABJRU5ErkJggg==">
  </a>
  <img alt="GitHub Workflow Status (branch)" src="https://img.shields.io/github/workflow/status/girardinsamuel/masonite-inertia/Test%20Application/master">
  <img alt="Coveralls github branch" src="https://img.shields.io/coveralls/github/girardinsamuel/masonite-inertia/master">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-inertia">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/girardinsamuel/masonite-inertia">
  <img alt="License" src="https://img.shields.io/github/license/girardinsamuel/masonite-inertia">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Introduction

Inertia is a new approach to building classic server-driven web apps. From their own web page:

> Inertia allows you to create fully client-side rendered, single-page apps, without much of the complexity that comes with modern SPAs. It does this by leveraging existing server-side frameworks.

Inertia requires an adapter for each backend framework.

This repo contains the Masonite server-side adapter for [Inertia.js](https://inertiajs.com/).
[Work In Progress] You can find the legacy Inertia PingCRM demo with Masonite here [demo](https://github.com/girardinsamuel/pingcrm-masonite).

## Features

Almost all features of the official server-side adapters are present 😃

- Shared data
- Partial reloads
- Lazy loaded props
- Set root view in a provider
- Set root view per view
- Enable sharing Masonite routes (prefer using [masonite-js-routes](https://github.com/girardinsamuel/masonite-js-routes))
- Enable sharing Masonite flash messages

## Official Masonite Documentation

New to Masonite ? Please first read the [Official Documentation](https://docs.masoniteproject.com/).
Masonite strives to have extremely comprehensive documentation 😃. It would be wise to go through the tutorials there.
If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](http://slack.masoniteproject.com/)!

## Installation

**Requirements**

To get started you will need the following:

- Masonite 2.3+
- Laravel Mix installed (new Masonite 2.3 projects come with this installed already)
- a Node.js environment (npm or yarn)

```bash
pip install masonite-inertia
```

**Install NPM dependencies**

First we'll need to install some NPM packages (we are using Vue here as frontend framework and `inertia-vue` as Inertia.js client-side adapter):

```
$ npm install vue @inertiajs/inertia @inertiajs/inertia-vue
```

## Configuration

Add InertiaProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite.inertia import InertiaProvider

# ...
PROVIDERS = [
    # ...

    # Third Party Providers
    InertiaProvider,
]
```

Inertia adapter comes with a middleware that will control some of the flow of data. Add InertiaMiddleware to your project in `config/middleware.py`:

```python
# config/middleware.py
# ...
from masonite.inertia import InertiaMiddleware

# ...
HTTP_MIDDLEWARE = [
    LoadUserMiddleware,
    CsrfMiddleware,
    #...
    InertiaMiddleware,
]
```

Then install the package to get the `config/inertia.py` in your project:

```bash
python craft inertia:install
```

**Scaffold a base Vue app and a template (optional)**
Then, if you want you can quicky scaffold a Vue app with two components to test Inertia behaviour by running the publish command :

```
python craft publish InertiaProvider --tag app
```

## Usage [Doc In Progress]

### How to use Inertia.js with Masonite adapter

We will create two routes and a controller which will load the two components scaffolded with previous command and see Inertia.js behaviour. In order to create Inertia response in our Controller, we are going to use newly available response `InertiaResponse`. And that's it !

We can quickly create this demo (routes & controller) with the publish command :

```
$ python craft publish InertiaProvider --tag demo
```

or you can create it manually:

```
$ craft controller InertiaController
```

This will create a controller `InertiaController` but you can name it whatever you like. It would be good to keep the standard of whatever setup you have now for your home page. Then create two routes to that controller if you don't have them already:

```python
ROUTES = [
    Get('/', 'InertiaController@index'),
    Get('/helloworld', 'InertiaController@helloworld')
]
```

And finally create the controller methods. We just need to use the new `InertiaResponse` to render our controller.

```python
# app/controllers/InertiaController.py
from masonite.inertia import InertiaResponse

## ..
def inertia(self, view: InertiaResponse):
    return view.render('Index')

def helloworld(self, view: InertiaResponse):
  return view.render('HelloWorld')

## ..
```

This controller will render the view based on template `templates/app.html` and will load the Vue components into it depending on the route.
Note that instead of specifying a Jinja template like we normally do we can just specify a page here. So since we have `../pages/Index.vue` we specify to render `Index` here.

### Test it !

Ok now we need to do 2 more commands. The first thing is to run `npm run dev` (at root) to compile all of this (with webpack mix):

```
$ npm run dev
```

Now we can run the server like we normally do:

```
$ craft serve
```

When we go to our homepage we will see we see `Index.vue` component:

```
Home Page
```

Click on the link you can now see `HelloWorld` without page refresh !!!!

Congratulations! You have now setup Inertia in our project! For more information on how to use Inertia.js got to its [documentation](https://inertiajs.com/installation).

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

**CONTRIBUTORS**

- [josephmancuso](https://github.com/josephmancuso)
- [girardinsamuel](https://github.com/girardinsamuel)

## License

Masonite Inertia is open-sourced software licensed under the [MIT license](LICENSE).
