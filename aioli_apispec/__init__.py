# -*- coding: utf-8 -*-

from aioli import Package
from .controller import Controller
from .service import APISpecService

__version__ = '0.1.0'

export = Package(
    name='apispec',
    description='OpenAPI specification generator',
    controller=Controller,
    services=[APISpecService],
    models=[],
)
