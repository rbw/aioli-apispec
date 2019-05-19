# -*- coding: utf-8 -*-

from aioli.utils.http import jsonify
from aioli.package.controller import BaseHttpController, route
from .service import ApiSpecService


class HttpController(BaseHttpController):
    def __init__(self):
        self.service = ApiSpecService()

    @route('/', 'GET')
    async def packages_get(self, _):
        return jsonify(await self.service.get_pkgs())

    @route('/<package_name>', 'GET')
    async def package_get(self, _, package_name):
        return jsonify(await self.service.get_pkg(package_name))

