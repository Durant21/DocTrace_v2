from pyramid.config import Configurator
from DocTrace2.data.db_factory import DbSessionFactory
from pyramid.renderers import JSON
from DocTrace2.Domain.Documents import Document
from pyramid.events import NewRequest

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')

        allow_cors(config)
        init_db(config)
        configure_renderers(config)

        config.add_route('main','/main')
        config.add_route('trace','/trace')
        config.add_route('document','/document')
        config.add_route('documents_api','/api/documents')
        config.add_route('document_api','/api/document/{doc_id}')
        config.add_route('documents1_api','/api/create_document')
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


def allow_cors(config):
    def add_cors_headers_response_callback(event):
        def cors_headers(_, response):
            response.headers.update({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
                'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Max-Age': '1728000',
            })

        event.request.add_response_callback(cors_headers)

    config.add_subscriber(add_cors_headers_response_callback, NewRequest)

