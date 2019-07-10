from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.response import Response
from pyramid.httpexceptions import (HTTPFound, HTTPNotFound, HTTPForbidden)


def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': 'http://localhost:8081',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Accept, Set-Cookie, Content-Type, Authorization',
            'Content-Type':'application/json; charset=UTF-8',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)

from pyramid.events import NewRequest
from .models.player import Player
import jwt

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        # config.include('.security')
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)
        config.add_request_method(get_user, 'user', property=True)
        config.scan()
    return config.make_wsgi_app()

def get_user(request):
    # import pdb; pdb.set_trace()
    if request.authorization is not None:
        print(request.authorization)
        if request.authorization.params == 'undefined' or request.authorization.params == '':
            print(request.authorization)
            raise HTTPForbidden
        else:  
            token = request.authorization.params
            user = jwt.decode(token, 'secret', algorithms='HS256')
            if user:
                return user

