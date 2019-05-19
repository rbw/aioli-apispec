# -*- coding: utf-8 -*-

from aioli import Package
from .controller import HttpController
from .service import ApiSpecService

__version__ = '0.1.0'

export = Package(
    name='aioli-apispec',
    description='OpenAPI specification generator',
    controllers=[HttpController],
    services=[ApiSpecService],
    models=[],
)
