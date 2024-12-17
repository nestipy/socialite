from typing import List

from .abstract import OAuthProvider


class InstagramOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://api.instagram.com/oauth/authorize",
            token_url="https://api.instagram.com/oauth/access_token",
            user_info_url="https://graph.instagram.com/me?fields=id,username,account_type",
            scope=scopes or ["user_profile", "user_media"]
        )
