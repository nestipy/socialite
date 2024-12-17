from typing import List

from .abstract import OAuthProvider


class FacebookOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://www.facebook.com/v21.0/dialog/oauth",
            token_url="https://graph.facebook.com/v21.0/oauth/access_token",
            user_info_url="https://graph.facebook.com/me?fields=id,name,email,picture",
            scope=scopes or ["public_profile"]
        )
