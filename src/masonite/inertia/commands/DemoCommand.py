"""A DemoCommand Command."""
import os
from cleo import Command
from masonite.packages import append_web_routes


package_directory = os.path.dirname(os.path.realpath(__file__))


class DemoCommand(Command):
    """
    Create a Inertia.js demo and add it to your project.

    command:name
        {argument : description}
    """

    def handle(self):
        demo_path = os.path.join(package_directory, "../snippets/demo")
        append_web_routes(os.path.join(demo_path, "routes.py"))
        # install controller

        # scaffold app ?
