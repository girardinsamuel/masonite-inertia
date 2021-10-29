from masonite.routes import Route

ROUTES = [
    Route.get("/", "InertiaController@home"),
    Route.get("/inertia", "InertiaController@basic"),
    Route.get("/inertia/page-2", "InertiaController@second_page"),
    Route.get("/inertia/states", "InertiaController@states"),
    Route.get("/inertia/external", "InertiaController@external"),
    Route.get("/inertia/add-errors", "InertiaController@add_errors"),
    Route.get("/inertia/other-root", "InertiaController@other_root_view"),
    Route.get("/inertia/lazy-props", "InertiaController@lazy_props"),
]
