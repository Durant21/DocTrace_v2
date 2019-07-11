from pyramid.config import Configurator
from DocTrace2.data.db_factory import DbSessionFactory
from pyramid.renderers import JSON
from DocTrace2.Domain.Document import Document

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')

        configure_renderers(config)

        config.add_route('main','/main')
        config.add_route('trace','/trace')
        config.add_route('document','/document')
        config.add_route('documents_api','/api/get_documents')
        config.scan()

        # with Configurator(settings=settings) as config:
        #     init_db(config)

    return config.make_wsgi_app()



def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

    DbSessionFactory.global_init(db_file)


def configure_renderers(config):
    json_renderer = JSON(indent=4)
    json_renderer.add_adapter(Document, lambda d, _: d.to_dict())
    config.add_renderer('json',json_renderer)
