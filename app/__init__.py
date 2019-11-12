import os
from pyramid.config import Configurator

from .utils import expandvars_dict

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings = expandvars_dict(settings)
    with Configurator(settings=settings) as config:
        config.include('pyramid_jwt')
        config.include('.models')
        config.include('.config')
        config.include('.routes')
        config.include("pyramid_openapi3")
        config.pyramid_openapi3_spec(os.path.join(os.path.dirname(__file__), 'openapi.yaml'))
        config.pyramid_openapi3_add_explorer(route='/v1/docs')
        config.scan()
    return config.make_wsgi_app()
