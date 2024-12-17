from nestipy.dynamic_module import ConfigurableModuleBuilder
from .config import SocialiteConfig

ConfigurableClassBuilder, SOCIALITE_CONFIG = ConfigurableModuleBuilder[SocialiteConfig]().build()
