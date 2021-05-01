import pytest
from masonite.utils.structures import Dot


class InertiaTest:

    not_found = "inertia1234567890"

    def __init__(self, component, url, props={}, version=""):
        self._component = component
        self._url = url
        self._props = props
        self._version = version

    def component(self, component, lookup=False):
        assert self._component == component
        if lookup:
            # TODO: check component existence
            pass
        return self

    def has(self, key, value=None):
        # assert key in self._props
        corresponding_value = Dot().dict_dot(key, self._props, self.not_found)
        assert corresponding_value != self.not_found

        if value:
            assert corresponding_value == value

        return self

    def contains(self, key, count=None):
        corresponding_value = Dot().dict_dot(key, self._props, self.not_found)
        assert corresponding_value != self.not_found
        if count:
            assert len(corresponding_value) == count
        return self

    def missing(self, key):
        corresponding_value = Dot().dict_dot(key, self._props, self.not_found)
        assert corresponding_value == self.not_found
        return self

    def url(self, url):
        assert self._url == url
        return self

    def version(self, version):
        assert self._version == version
        return self

    def dump(self):
        from pprint import pprint
        pprint(vars(self))
        return self

    def dd(self):
        self.dump()
        pytest.fail("test stopped because of die and dump call dd()")
        return self


class InertiaTestingResponse:

    def assertInertiaComponent(self, component):
        return self

    def assertInertiaHasProp(self, prop, value=None):
        # TODO with nested props too
        return self

    def assertInertiaMissingProp(self, prop):
        return self

    def assertInertiaPropsExact(self, props):
        return self

    def assertIsInertia(self):
        self.assertViewHas("page.component")
        self.assertViewHas("page.props")
        self.assertViewHas("page.url")
        self.assertViewHas("page.version")
        return self

    def assertInertiaPropCount(self, prop, count):
        return self

    def assertInertia(self):
        """This will ensure that response is inertia and returns a special object on which
        Inertia specific assertions can be made."""
        self.assertIsInertia()
        data = self.response.original.dictionary["page"]
        return InertiaTest(
            data["component"],
            self.request.get_path(),
            data["props"],
            data["version"]
        )
