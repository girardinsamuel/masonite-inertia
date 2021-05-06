"""Database Settings """
from masoniteorm.connections import ConnectionResolver

"""
|--------------------------------------------------------------------------
| Databases connectors details
|--------------------------------------------------------------------------
|
| Setup details of the database connectors you want to use.
|
"""

DATABASES = {
    "default": "sqlite",
    "sqlite": {
        "driver": "sqlite",
        "database": "database.sqlite3",
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)
