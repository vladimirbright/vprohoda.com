# -*- coding: utf-8 -*-


from jinja2.exceptions import TemplateNotFound
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound
from pyramid.renderers import render_to_response


# Default context
class Root(object):
    def __init__(self, request):
        self.request = request


# Views
dummy = lambda _: {}


def template_view(request):
    return render_to_response(
        'vprohodacom:templates/%s.jinja2' % request.matchdict["template"],
        {},
        request=request
    )


def http_404(request):
    request.response.status_int = 404
    return {}


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.include('pyramid_jinja2')


    config.add_view(dummy, renderer='vprohodacom:templates/index.jinja2')

    config.add_route('pure_template', '{template}.html')
    config.add_view(template_view, route_name='pure_template')

    config.add_view(http_404, context=HTTPNotFound, renderer="vprohodacom:templates/404.jinja2")
    config.add_view(http_404, context=TemplateNotFound, renderer="vprohodacom:templates/404.jinja2")

    config.add_static_view('static', 'vprohodacom:static', cache_max_age=3600)

    return config.make_wsgi_app()

