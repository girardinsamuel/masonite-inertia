# masonite-inertia demo routes
ROUTES += [
    Get("/inertia", "InertiaDemoController@show"),
    Get("/inertia-hello", "InertiaDemoController@hello"),
]
