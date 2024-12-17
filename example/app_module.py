import os

from dotenv import load_dotenv
from nestipy.common import Module

from app_controller import AppController
from app_service import AppService
from nestipy_socialite import SocialiteModule, SocialiteConfig
from nestipy_socialite import GoogleOAuthProvider, FacebookOAuthProvider

load_dotenv()


@Module(
    imports=[
        SocialiteModule.register(
            SocialiteConfig(
                providers={
                    "google": GoogleOAuthProvider(
                        client_id=os.environ.get("GOOGLE_CLIENT_ID"),
                        client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
                        redirect_uri=os.environ.get("GOOGLE_REDIRECT_URI")
                    ),
                    "facebook": FacebookOAuthProvider(
                        client_id=os.environ.get("FACEBOOK_CLIENT_ID"),
                        client_secret=os.environ.get("FACEBOOK_CLIENT_SECRET"),
                        redirect_uri=os.environ.get("FACEBOOK_REDIRECT_URI")
                    )
                }
            )
        )
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
