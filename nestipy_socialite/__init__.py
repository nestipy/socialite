from .providers.abstract import OAuthProvider
from .module import SocialiteModule
from .config import SocialiteConfig
from .builder import SOCIALITE_CONFIG
from .service import SocialiteService

from .providers.google import GoogleOAuthProvider
from .providers.facebook import FacebookOAuthProvider
from .providers.x import XOAuthProvider
from .providers.github import GitHubOAuthProvider
from .providers.instagram import InstagramOAuthProvider
from .providers.azure import AzureOAuthProvider
from .providers.microsoft import MicrosoftOAuthProvider
from .providers.spotify import SpotifyOAuthProvider
from .providers.linkedin import LinkedInOAuthProvider

__all__ = [
    "SocialiteModule",
    "SocialiteConfig",
    "SOCIALITE_CONFIG",
    "SocialiteService",
    "OAuthProvider",
    "GoogleOAuthProvider",
    "FacebookOAuthProvider",
    "XOAuthProvider",
    "GitHubOAuthProvider",
    "InstagramOAuthProvider",
    "SpotifyOAuthProvider",
    "AzureOAuthProvider",
    "MicrosoftOAuthProvider",
    "LinkedInOAuthProvider"
]
