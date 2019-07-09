from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.pt')
def my_view(request):
    return {'project': 'DocTrace2'}


@view_config(route_name='main', renderer='../templates/main_template.pt')
def my_view1(request):
    return {'project': 'DocTrace2'}


@view_config(route_name='trace', renderer='../templates/trace_template.pt')
def trace_view1(request):
    return {'project': 'DocTrace2'}
