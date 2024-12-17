from typing import List

from .abstract import OAuthProvider


class SpotifyOAuthProvider(OAuthProvider):
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str] = None):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            authorize_url="https://accounts.spotify.com/authorize",
            token_url="https://accounts.spotify.com/api/token",
            user_info_url="https://api.spotify.com/v1/me",
            scope=scopes or ["user-read-private", "user-read-email"]
        )
