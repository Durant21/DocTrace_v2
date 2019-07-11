from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/orig_template.pt')
def my_view(request):
    return {'project': 'DocTrace2'}


@view_config(route_name='main', renderer='../templates/main_template.pt')
def my_view1(request):
    return {'project': 'DocTrace2'}


@view_config(route_name='trace', renderer='../templates/trace_template.pt')
def trace_view1(request):
    return {'project': 'DocTrace2'}


@view_config(route_name='document', renderer='../templates/document_template.pt')
def trace_view2(request):
    return {'project': 'DocTrace2'}

# @view_config(route_name='documents_api', renderer='../templates/document_template.pt')
# def trace_view3(request):
#     return {'project': 'DocTrace2'}
