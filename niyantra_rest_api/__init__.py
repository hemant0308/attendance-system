from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jwt')
        config.include('.models')
        config.include('.config')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
