from typing import List

from .abstract import OAuthProvider


class GoogleOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://accounts.google.com/o/oauth2/auth",
            token_url="https://oauth2.googleapis.com/token",
            user_info_url="https://www.googleapis.com/oauth2/v3/userinfo",
            scope=scopes or [
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email",
                "openid"]
        )
