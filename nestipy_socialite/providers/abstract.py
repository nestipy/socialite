from abc import ABC, abstractmethod

from requests_oauthlib import OAuth2Session


class OAuthProvider(ABC):
    def __init__(self, client_id, client_secret, redirect_uri, authorize_url, token_url, user_info_url, scope=None):
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri
        self._authorize_url = authorize_url
        self._token_url = token_url
        self._user_info_url = user_info_url
        self._scope = scope or []
        self._state = None
        self._session = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=self._scope)

    def get_authorization_url(self):
        auth_url, state = self._session.authorization_url(self._authorize_url)
        self._state = state
        return auth_url

    def _get_token_via_code(self, code: str):
        token = self._session.fetch_token(
            token_url=self._token_url,
            client_secret=self._client_secret,
            code=code
        )
        return token

    def validate_token(self, token: str):
        self._session.token = {"access_token": token}
        response = self._session.get(self._user_info_url)
        response.raise_for_status()
        return response.json()

    def get_user_info(self, token: str = None, code: str = None):
        if token:
            self._session.token = {"access_token": token}
        elif code:
            self._session.token = self._get_token_via_code(code)
        response = self._session.get(self._user_info_url)
        response.raise_for_status()
        return response.json()

    def user(self, token: str = None, code: str = None):
        return self.get_user_info(token=token, code=code)
