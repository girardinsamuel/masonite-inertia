"""A InstallCommand Command."""
from cleo import Command
import os
import shutil
from masonite.utils.location import config_path


package_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class InstallCommand(Command):
    """
    Install Masonite adapter for Inertia.js

    install:inertia
    """

    def handle(self):
        # publish config file
        default_config = os.path.join(package_root, "config/inertia.py")
        published_config = config_path("inertia.py")
        if not os.path.isfile(published_config):
            shutil.copyfile(default_config, published_config)
            self.info("Configuration File Created!")
        else:
            self.line_error("Configuration File Already Exists!")
            return -1
