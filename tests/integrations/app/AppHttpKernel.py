from masonite.foundation import HttpKernel

from src.masonite.inertia import InertiaMiddleware


class AppHttpKernel(HttpKernel):
    http_middleware = [InertiaMiddleware]
