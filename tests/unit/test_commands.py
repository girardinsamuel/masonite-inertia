import os
from masonite.tests import TestCase


class TestCommands(TestCase):
    def test_install(self):
        (
            self.craft("install:inertia")
            .assertSuccess()
            .assertOutputContains("Configuration File Created!")
        )
        os.remove("tests/integrations/config/inertia.py")
