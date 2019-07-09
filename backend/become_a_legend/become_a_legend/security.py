from pyramid.authentication import RemoteUserAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import (
    Authenticated,
    Everyone,
)
from .models import Player
import jwt


class MyAuthenticationPolicy(RemoteUserAuthenticationPolicy):
    def authenticated_userid(self, request):
        user = request.user
        if user is not None:
            return user.id
    
    def effective_principals(self, request):
        principals = [Everyone]
        user = request.user
        if user is not None:
            principals.append(Authenticated)
            principals.append(str(user.id))
            principals.append('role:' + user.role)
        return principals





# def get_user(request):
#     player_id = request.unauthenticated_userid
#     if player_id is not None:
#         player = request.dbsession.query(Player).get(player_id)
#         return player

# def includeme(config):
    # settings = config.get_settings()
    # authn_policy = MyAuthenticationPolicy(environ_key='secret', callback=set_user)
    # config.set_authentication_policy(authn_policy)
    # config.set_authorization_policy(ACLAuthorizationPolicy())
    # config.add_request_method(get_user, 'user', reify=True)