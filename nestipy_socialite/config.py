from dataclasses import dataclass, field
from .providers.abstract import OAuthProvider


@dataclass
class SocialiteConfig:
    providers: dict[str, OAuthProvider] = field(default_factory=lambda: {})
