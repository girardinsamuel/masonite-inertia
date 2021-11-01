from masonite.notification.providers import NotificationProvider
from masonite.providers import (
    AuthenticationProvider,
    AuthorizationProvider,
    BroadcastProvider,
    CacheProvider,
    EventProvider,
    ExceptionProvider,
    FrameworkProvider,
    HashServiceProvider,
    HelpersProvider,
    MailProvider,
    QueueProvider,
    RouteProvider,
    SessionProvider,
    StorageProvider,
    ViewProvider,
    WhitenoiseProvider,
)
from masonite.scheduling.providers import ScheduleProvider
from masonite.validation.providers import ValidationProvider
from src.masonite.inertia import InertiaProvider

PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    NotificationProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    ScheduleProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    HashServiceProvider,
    AuthenticationProvider,
    AuthorizationProvider,
    ValidationProvider,
    InertiaProvider,
]
