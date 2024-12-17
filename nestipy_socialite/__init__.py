from .providers.abstract import OAuthProvider
from .module import SocialiteModule
from .config import SocialiteConfig
from .builder import SOCIALITE_CONFIG
from .service import SocialiteService

from .providers.google import GoogleOAuthProvider
from .providers.facebook import FacebookOAuthProvider
from .providers.x import XOAuthProvider
from .providers.github import GitHubOAuthProvider

__all__ = [
    "SocialiteModule",
    "SocialiteConfig",
    "SOCIALITE_CONFIG",
    "SocialiteService",
    "OAuthProvider",
    "GoogleOAuthProvider",
    "FacebookOAuthProvider",
    "XOAuthProvider",
    "GitHubOAuthProvider"
]
