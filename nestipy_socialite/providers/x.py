from typing import List

from .abstract import OAuthProvider


class XOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://twitter.com/i/oauth2/authorize",
            token_url="https://api.twitter.com/oauth2/token",
            user_info_url="https://api.twitter.com/2/me",
            scope=scopes or ["tweet.read", "users.read", "follows.read"]
        )
