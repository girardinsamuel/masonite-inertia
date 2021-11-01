import os

from masonite.tests import TestCase


class TestCommands(TestCase):
    def test_publish_config(self):
        (
            self.craft("package:publish", "inertia")
            .assertSuccess()
            .assertOutputContains("Config")
            .assertOutputContains("tests/integrations/config/inertia.py")
        )
        assert os.path.isfile("tests/integrations/config/inertia.py")
        os.remove("tests/integrations/config/inertia.py")
