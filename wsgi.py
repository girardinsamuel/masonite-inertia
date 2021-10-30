from masonite.foundation import Application, Kernel
from tests.integrations.config.providers import PROVIDERS
from tests.integrations.Kernel import Kernel as AppKernel

application = Application("tests/integrations/")

"""First Bind important providers needed to start the server
"""

application.register_providers(Kernel, AppKernel)

application.add_providers(*PROVIDERS)
