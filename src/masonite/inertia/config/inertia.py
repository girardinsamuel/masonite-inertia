"""Masonite Inertia Settings"""
import os

"""
|--------------------------------------------------------------------------
| Mix Manifest
|--------------------------------------------------------------------------
|
| Absolute path to mix-manifest.json location. It's needed for computing
| js assets version.
|
| default: root directory
"""

PUBLIC_PATH = os.getcwd()


"""
|--------------------------------------------------------------------------
| Root view
|--------------------------------------------------------------------------
|
| Root template view used by your Inertia Controllers to render the page.
| This is the name of the view without .html. This can also be overriden with
| set_root_view Inertia helper.
|
| default: app
"""

ROOT_VIEW = "app"

"""
|--------------------------------------------------------------------------
| Include routes
|--------------------------------------------------------------------------
|
| Include server-side routes as JSON payload in Inertia response (props)
| Might be needed if you're not using masonite-js-routes. You can also do
| it yourself with Inertia share helper.
|
| default: False
"""

INCLUDE_ROUTES = False
