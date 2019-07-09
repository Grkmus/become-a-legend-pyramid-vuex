from pyramid.httpexceptions import (HTTPFound, HTTPForbidden)
from pyramid.response import Response
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy.exc import DBAPIError, SQLAlchemyError

from pyramid.security import (
    remember,
    forget,
    )
from pyramid.view import (
    forbidden_view_config,
    view_config,
)

from ..models import Player
from ..services.common_service import to_json
import jwt
import re

@view_config(route_name='get_register_form')
def get_register_form(request):
    return Response('ok', status=200)

@view_config(route_name='post_register_form')
def post_register_form(request):
    name = request.json['name']
    surname = request.json['surname']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    # we should validate our data!!!

    try:
        # check if username exist in the database
        if request.dbsession.query(Player).filter_by(username=username).first():
            return Response('This username is already taken', status=406)
        player = Player(name=name, surname=surname, username=username, email=email)
        player.set_password(password)
        request.dbsession.add(player)
        request.dbsession.flush()
        token = jwt.encode({ 'username': player.username, 'id': player.id }, 'secret', algorithm='HS256')
        return Response('OK', status=200, json={ 'token': token.decode('utf-8'), 'user_id': player.id })
    except DBAPIError:
        return Response(DBAPIError.args[0], content_type='text/plain', status=500)
    except Exception as err:
        print(err)
        return Response(body=err.args[0], status=406)

@view_config(route_name='post_login_form', renderer='json')
def post_login_form(request):
    username = request.json['username']
    password = request.json['password']
    player = request.dbsession.query(Player).filter_by(username=username).first()
    if player is not None and player.check_password(password):
        token = jwt.encode({ 'username': player.username, 'id': player.id }, 'secret', algorithm='HS256')
        response = Response('ok', status=200, json_body={ 'token': token.decode('utf-8'), 'user_id': player.id })
        return response
    message = 'Failed login1'
    return Response(HTTPForbidden)

@view_config(route_name='get_login_form', renderer='json')
def get_login_form(request):
    if not request.user:
        return Response('ok', status=200)

@view_config(route_name='get_login_form_o', renderer='json')
def get_login_form_o(request):
    return {}

# @forbidden_view_config()
# def forbidden_view(request):
#     next_url = request.route_url('login', _query={'next': request.url})
#     return HTTPFound(location=next_url)