from masonite.routes import Route

ROUTES = [
    Route.get("/", "InertiaController@home").name("home"),
    # routes to test different features of Inertia
    Route.get("/inertia", "InertiaController@basic").name("inertia.home"),
    Route.get("/inertia/page-2", "InertiaController@second_page").name(
        "inertia.page-2"
    ),
    Route.get("/inertia/lazy-props", "InertiaController@lazy_props").name(
        "inertia.lazy-props"
    ),
    Route.get("/inertia/external", "InertiaController@external").name(
        "inertia.external"
    ),
    Route.get("/inertia/states", "InertiaController@states").name("inertia.states"),
    Route.post("/inertia/add-errors", "InertiaController@add_errors").name(
        "inertia.errors"
    ),
    Route.get("/inertia/other-root", "InertiaController@other_root_view").name(
        "inertia.other_root"
    ),
]
