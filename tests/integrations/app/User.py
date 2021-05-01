from masoniteorm.models import Model
from masonite.authentication import Authenticates


class User(Model, Authenticates):
    __fillable__ = ["name", "password", "email"]
