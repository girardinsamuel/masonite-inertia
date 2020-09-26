"""A InstallCommand Command."""
from cleo import Command
import os
from masonite.packages import create_or_append_config


package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Install Masonite adapter for Inertia.js

    install:inertia
    """

    def handle(self):
        create_or_append_config(
            os.path.join(package_directory, "../snippets/config/inertia.py")
        )
