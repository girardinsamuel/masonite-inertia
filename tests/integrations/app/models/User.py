"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
