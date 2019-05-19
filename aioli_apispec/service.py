# -*- coding: utf-8 -*-

from aioli.package.service import BaseService
from aioli.package.controller import BaseHttpController

from ._apispec import ApiSpec


class ApiSpecService(BaseService):
    schemas = {}

    def on_ready(self):
        self._generate_specs()

    def _generate_specs(self):
        for name, pkg in self.pkgs:
            if not pkg.path:
                continue

            spec = ApiSpec(pkg)

            for ctrl in pkg.controllers:
                if not isinstance(ctrl, BaseHttpController):
                    continue

                for route_stack in ctrl.stacks:
                    spec.consume_stack(*route_stack)

            self.schemas[name] = spec.schema

    async def get_pkgs(self):
        return self.pkgs.values()

    async def get_pkg(self, name):
        return self.pkgs[name]
