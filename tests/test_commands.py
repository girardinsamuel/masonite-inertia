from masonite.testing import TestCase
from cleo import Application
from cleo import CommandTester
from src.masonite.inertia.commands.InstallCommand import InstallCommand


class TestCommands(TestCase):
    def setUp(self):
        super().setUp()
        self.application = Application()
        self.application.add(InstallCommand())
        cmd = self.application.find("install:inertia")
        # self.install_cmd = CommandTester(InstallCommand())
        self.install_cmd = CommandTester(cmd)

    def test_install_package(self):
        self.install_cmd.execute()
