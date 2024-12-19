from typing import List
from .abstract import OAuthProvider


class AzureOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, tenant_id: str, redirect_uri: str, scopes: List[str] = None):
        base_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0"
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url=f"{base_url}/authorize",
            token_url=f"{base_url}/token",
            user_info_url="https://graph.microsoft.com/v1.0/me",
            scope=scopes or ["openid", "profile", "email", "User.Read"]
        )

    def user(self, token: str = None, code: str = None):
        return self.get_user_info(token=token, code=code)
