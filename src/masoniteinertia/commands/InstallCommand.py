"""A InstallCommand Command."""
from cleo import Command
import os
import shutil


package_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def create_if_not_exists(location, name=False):
    if name:
        file_name = name
    else:
        file_name = os.path.basename(location)

    # import it into the config directory
    config_directory = os.path.join(os.getcwd(), "config")

    # if file does not exist
    if not os.path.isfile(config_directory + "/" + file_name):
        shutil.copyfile(location, config_directory + "/" + file_name)
        print("\033[92mConfiguration File Created!\033[0m")
    else:
        print("\033[93mConfiguration File Already Exists!\033[93m")


class InstallCommand(Command):
    """
    Install Masonite adapter for Inertia.js

    install:inertia
    """

    def handle(self):
        create_if_not_exists(os.path.join(package_root, "config/inertia.py"))
