from masonite.utils.structures import data_get

from ..core.InertiaResponse import InertiaResponse

NOT_FOUND = "#inertia1234567890"


class InertiaTest:
    def __init__(self, component, url, props={}, root_view="app", version=""):
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
        corresponding_value = data_get(self._props, key, NOT_FOUND)
        assert corresponding_value != NOT_FOUND

        if value:
            assert corresponding_value == value

        return self

    def hasCount(self, key, count=None):
        corresponding_value = data_get(self._props, key, NOT_FOUND)
        assert corresponding_value != NOT_FOUND
        if count:
            assert len(corresponding_value) == count
        return self

    def missing(self, key):
        corresponding_value = data_get(self._props, key, NOT_FOUND)
        assert corresponding_value == NOT_FOUND
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
        import pytest

        self.dump()
        pytest.fail("Inertia: test stopped when calling dd()")
        return self


class InertiaTestingResponse:
    @property
    def _inertia_response(self):
        """Get InertiaResponse instance."""
        return self.response.original

    def assertIsInertia(self):
        assert isinstance(self._inertia_response, InertiaResponse)
        return self

    def assertInertiaComponent(self, component):
        assert self._inertia_response.component == component
        return self

    def assertInertiaHasProp(self, key, value=None):
        corresponding_value = data_get(self._inertia_response.props, key, NOT_FOUND)
        assert corresponding_value != NOT_FOUND

        if value:
            assert corresponding_value == value
        return self

    def assertInertiaMissingProp(self, key):
        corresponding_value = data_get(self._inertia_response.props, key, NOT_FOUND)
        assert corresponding_value == NOT_FOUND
        return self

    def assertInertiaPropCount(self, key, count):
        corresponding_value = data_get(self._inertia_response.props, key, NOT_FOUND)
        assert corresponding_value != NOT_FOUND
        if count:
            assert len(corresponding_value) == count
        return self

    def assertInertiaVersion(self, version):
        assert self._inertia_response.version == version
        return self

    def assertInertiaRootView(self, view):
        assert self._inertia_response.root_view == view
        return self

    def withInertia(self):
        """This will ensure that response is inertia and returns a special object on which
        Inertia handy assertions can be made."""
        self.assertIsInertia()
        inertia_response = self.response.original
        return InertiaTest(
            inertia_response.component,
            self.request.get_path(),
            inertia_response.props,
            inertia_response.root_view,
            inertia_response.version,
        )
