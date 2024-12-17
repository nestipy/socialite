from typing import Annotated, Optional

from nestipy.common import Injectable
from nestipy.ioc import Inject

from .config import SocialiteConfig
from .providers.abstract import OAuthProvider
from .builder import SOCIALITE_CONFIG
from .exception import ProviderNotFound


@Injectable()
class SocialiteService:
    _config: Annotated[SocialiteConfig, Inject(SOCIALITE_CONFIG)]

    def driver(self, key: str) -> Optional[OAuthProvider]:
        provider = self._config.providers.get(key)
        if provider is None:
            raise ProviderNotFound(key=key)
        return provider
