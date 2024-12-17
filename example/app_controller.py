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
        print(req.query_params)
        print(code)
        return self.socialite.driver(driver).user(code=code)
