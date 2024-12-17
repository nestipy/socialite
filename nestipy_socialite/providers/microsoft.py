from typing import List

from .abstract import OAuthProvider


class MicrosoftOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
            token_url="https://login.microsoftonline.com/common/oauth2/v2.0/token",
            user_info_url="https://graph.microsoft.com/v1.0/me",
            scope=scopes or ["openid", "profile", "email", "User.Read"]
        )
