from masonite.testing import TestCase
from masonite.routes import Get


class TestPackage(TestCase):

    def setUp(self):
        super().setUp()
        # self.routes(only=[
        #     Get('/app', 'InertiaController@inertia')
        # ])

    def test_test(self):
        assert self.get('/app').hasMiddleware('inertia')
