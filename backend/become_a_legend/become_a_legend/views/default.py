from pyramid.view import ( view_config, view_defaults )
from pyramid.httpexceptions import (HTTPFound, HTTPNotFound, HTTPForbidden)
from pyramid.response import Response
from sqlalchemy.orm import ( sessionmaker, load_only )
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from pyramid.security import (
    remember,
    forget,
    )
import json
from .. import models
from ..services.common_service import to_json


@view_config(route_name='home', renderer='json')
def landing(request):
    return {'one': 'one', 'project': 'Become A Legend'}

@view_defaults(route_name='player', renderer='json')
class PlayerView(object):
    def __init__(self, request):
        self.request = request


    @view_config(route_name='get_all_players')
    def get_all_players(self):
        players = self.request.dbsession.query(models.Player.id, models.Player.name, models.Player.surname).all()
        players_list = []
        for i in players:
            player = dict(id=i.id, name=i.name, surname=i.surname)
            players_list.append(player)
        return players_list

    @view_config(route_name='get_player')
    def get_player(self):
        try:
            player_id = self.request.matchdict['id']
            player = self.request.dbsession.query(models.Player).filter_by(id=player_id).first()
            if player is None:
                raise HTTPNotFound
            player_json = to_json(player)
            return Response('OK', status=200, json=player_json)    
        except DBAPIError as identifier:
            return Response(db_err_msg, content_type='text/plain', status=500)

    

    @view_config(route_name='append_player_to_team', renderer='json')
    def append_player_to_team(self):
        try:
            player_id = self.request.matchdict['id']
            player = self.request.dbsession.query(models.Player).filter_by(id=player_id).first()
            player.team_id = self.request.matchdict['team_id']
            return Response('OK', status=200)
        except DBAPIError:
            return Response(db_err_msg, content_type='text/plain', status=500)

    @view_config(route_name='append_player_to_event', renderer='json')
    def append_player_to_event(self):
        try:
            player_id = self.request.matchdict['id']
            player = self.request.dbsession.query(models.Player).filter_by(id=player_id).first()
            player.events.append(self.request.matchdict['event_id'])
            event = HTTPFound(location='/event'+ self.request.matchdict['event_id'])
            return Response('OK', status=200)
        except DBAPIError:
            return Response(db_err_msg, content_type='text/plain', status=500)

    @view_config(route_name='get_all_events')
    def get_all_events(self):
        events = self.request.dbsession.query(models.Event.name, models.Event.type_of_event).all()
        events_list = []
        for i in events:
            event = dict(name=i.name, type_of_event=i.type_of_event)
            events_list.append(event)
        return events_list

@view_config(route_name='add_team', renderer='json')
def add_team(request):
    try:
        name = request.params['name']
        team = models.Team(name=name)
        request.dbsession.add(team)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    finally:
        print('mission completed')
        return Response('OK', status=200)

@view_config(route_name='get_team')
def get_team(request):
    try:
        team_id = request.matchdict['id']
        team = request.dbsession.query(models.Team).filter_by(id=team_id).first()
        return team
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

db_err_msg = 'Database error'