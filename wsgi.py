from masonite.foundation import Application, Kernel
from tests.integrations.config.providers import PROVIDERS
import os

from tests.integrations.app.AppHttpKernel import AppHttpKernel


application = Application(os.getcwd())

"""First Bind important providers needed to start the server
"""

application.register_providers(Kernel, AppHttpKernel)

application.add_providers(*PROVIDERS)
