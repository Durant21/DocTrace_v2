from pyramid.config import Configurator
from DocTrace2.data.db_factory import DbSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.add_route('main','/main')
        config.add_route('trace','/trace')
        config.scan()

        # with Configurator(settings=settings) as config:
        #     init_db(config)

    return config.make_wsgi_app()



def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

    DbSessionFactory.global_init(db_file)
