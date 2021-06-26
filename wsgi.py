import os

from masonite.foundation import Application, Kernel
from tests.integrations.app.Kernel import Kernel as AppKernel
from tests.integrations.config.providers import PROVIDERS

application = Application(os.getcwd())

"""First Bind important providers needed to start the server
"""

application.register_providers(Kernel, AppKernel)

application.add_providers(*PROVIDERS)
