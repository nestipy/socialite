<p align="center">
  <a target="_blank"><img src="https://raw.githubusercontent.com/nestipy/nestipy/release-v1/nestipy.png" width="200" alt="Nestipy Logo" /></a></p>
<p align="center">
    <a href="https://pypi.org/project/nestipy">
        <img src="https://img.shields.io/pypi/v/nestipy?color=%2334D058&label=pypi%20package" alt="Version">
    </a>
    <a href="https://pypi.org/project/nestipy">
        <img src="https://img.shields.io/pypi/pyversions/nestipy.svg?color=%2334D058" alt="Python">
    </a>
    <a href="https://github.com/tsiresymila1/nestipy/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/tsiresymila1/nestipy" alt="License">
    </a>
</p>

## Description

<p>Nestipy is a Python framework built on top of FastAPI that follows the modular architecture of NestJS</p>
<p>Under the hood, Nestipy makes use of <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a>, but also provides compatibility with a wide range of other libraries, like <a href="https://fastapi.tiangolo.com/" target="_blank">Blacksheep</a>, allowing for easy use of the myriad of third-party plugins which are available.</p>

## Getting started

```cmd
    pip install nestipy-socialite
```

`app_module.py`

```python
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

```

`app_controller.py`

```python
from typing import Annotated

from nestipy.common import Controller, Get, Post, Response, Request
from nestipy.ioc import Inject, Param, Res, Req

from nestipy_socialite import SocialiteService


@Controller('auth')
class AppController:
    socialite: Annotated[SocialiteService, Inject()]

    @Get('/{driver}/login')
    async def get(self, driver: Annotated[str, Param('driver')], res: Annotated[Response, Res()]) -> Response:
        redirect_url = self.socialite.driver(driver).get_authorization_url()
        print(redirect_url)
        return await res.redirect(redirect_url)

    @Get('/{driver}/callback')
    async def callback(
            self,
            req: Annotated[Request, Req()],
            res: Annotated[Response, Res()],
            driver: Annotated[str, Param('driver')],
    ) -> dict:
        code = req.query_params.get('code')
        return self.socialite.driver(driver).user(code=code)

```

## Support

Nestipy is an MIT-licensed open source project. It can grow thanks to the sponsors and support from the amazing backers.
If you'd like to join them, please [read more here].

## Stay in touch

- Author - [Tsiresy Mila](https://tsiresymila.vercel.app)

## License

Nestipy is [MIT licensed](LICENSE).
