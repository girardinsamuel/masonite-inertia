from masonite.tests import TestCase
from src.masonite.inertia import lazy


class TestLazyProps(TestCase):
    def test_can_call_lazy_props(self):
        lazy_prop = lazy(lambda x: x * 2)
        self.assertTrue(callable(lazy_prop))
        self.assertEqual(lazy_prop(2), 4)
