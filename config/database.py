""" Database Settings """

import os

from masonite.environment import LoadEnvironment, env
from masoniteorm.query import QueryBuilder
from masoniteorm.connections import ConnectionResolver

"""
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
"""

LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""
DATABASES = {
    "default": env("DB_CONNECTION"),
    "sqlite": {
        "driver": "sqlite",
        "database": env("DB_DATABASE"),
        "log_queries": env("DB_LOG"),
    },
    "mysql": {
        "driver": "mysql",
        "host": env("DB_HOST"),
        "database": env("DB_DATABASE"),
        "port": env("DB_PORT"),
        "user": env("DB_USERNAME"),
        "password": env("DB_PASSWORD"),
        "log_queries": env("DB_LOG"),
    },
    "postgres": {
        "driver": "postgres",
        "host": env("DB_HOST"),
        "database": env("DB_DATABASE"),
        "port": env("DB_PORT"),
        "user": env("DB_USERNAME"),
        "password": env("DB_PASSWORD"),
        "log_queries": env("DB_LOG"),
    },
}
DB = ConnectionResolver().set_connection_details(DATABASES)