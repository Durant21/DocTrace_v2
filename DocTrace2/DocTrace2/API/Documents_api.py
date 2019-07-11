from pyramid.view import view_config
from DocTrace2.BLL.Documents import BLL_Documents


@view_config(route_name='documents_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_documents(_):
    docs = BLL_Documents.get_documents()

    return docs