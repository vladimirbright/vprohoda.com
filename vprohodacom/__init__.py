# -*- coding: utf-8 -*-


from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound


from vprohodacom.resources import Root


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.include('pyramid_jinja2')


    config.add_view('vprohodacom.views.index',
                    context='vprohodacom:resources.Root',
                    renderer='vprohodacom:templates/index.jinja2')


    config.add_route('sitelist', '/sitelist.in.html')
    config.add_view('vprohodacom.views.sitelist',
                    context='vprohodacom:resources.Root',
                    renderer='vprohodacom:templates/sitelist.in.jinja2',
                    route_name='sitelist')


    config.add_view('vprohodacom.views.http_404',
                    context=HTTPNotFound,
                    renderer="vprohodacom:templates/404.jinja2")

    config.add_static_view('static', 'vprohodacom:static', cache_max_age=3600)

    return config.make_wsgi_app()
