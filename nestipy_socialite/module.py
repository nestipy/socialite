from nestipy.common import Module
from .builder import ConfigurableClassBuilder
from .service import SocialiteService


@Module(
    is_global=True,
    providers=[
        SocialiteService,
    ]
)
class SocialiteModule(ConfigurableClassBuilder):
    pass
