import json
import os
from src.masonite.inertia.commands.DemoCommand import DemoCommand
from masonite.testing import TestCase
from cleo import Application
from cleo import CommandTester
from src.masonite.inertia.commands.InstallCommand import InstallCommand
from src.masonite.inertia.commands.DemoCommand import DemoCommand


class TestCommands(TestCase):
    def setUp(self):
        super().setUp()
        self.application = Application()
        self.application.add(InstallCommand())
        self.application.add(DemoCommand())
        cmd = self.application.find("install:inertia")
        self.install_cmd = CommandTester(cmd)
        cmd = self.application.find("inertia:demo")
        self.demo_cmd = CommandTester(cmd)

    def test_install_package(self):
        # TODO: clean after test
        self.install_cmd.execute()

    def test_scaffold_demo(self):
        # TODO: clean after test
        self.demo_cmd.execute()
        assert os.path.exists("resources/js/inertia_demo.js")
        assert os.path.exists("resources/js/pages")
        assert os.path.exists("resources/templates/inertia_demo.html")
        with open(os.path.realpath("package.json"), "r+") as f:
            packages = json.load(f)
            assert "@inertiajs/inertia" in packages["devDependencies"]
        os.remove("resources/js/inertia_demo.js")
        os.remove("resources/templates/inertia_demo.html")
        # os.rmdir("resources/js/pages")