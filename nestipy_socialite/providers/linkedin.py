from typing import List

from .abstract import OAuthProvider


class LinkedInOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://www.linkedin.com/oauth/v2/authorization",
            token_url="https://www.linkedin.com/oauth/v2/accessToken",
            user_info_url="https://api.linkedin.com/v2/me",
            scope=scopes or ["r_liteprofile", "r_emailaddress"]
        )
