from pyramid.view import ( view_config, view_defaults )
from pyramid.httpexceptions import (HTTPFound, HTTPNotFound, HTTPForbidden)
from pyramid.response import Response
from sqlalchemy.orm import ( sessionmaker, load_only, joinedload)
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from pyramid.security import (
    remember,
    forget,
    )
import json
from .. import models
from marshmallow import pprint
from become_a_legend.services.utils import ( PlayerSchema, EventSchema )

@view_config(route_name='home', renderer='json')
def landing(request):
    return {'one': 'one', 'project': 'Become A Legend'}

@view_defaults(route_name='player', renderer='json')
class PlayerView(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='get_all_players')
    def get_all_players(self):
        if self.request.user:
            players = self.request.dbsession.query(models.Player.id, models.Player.name, models.Player.surname).all()
            players_list = []
            for i in players:
                player = dict(id=i.id, name=i.name, surname=i.surname)
                players_list.append(player)
            return players_list
        return Response("Un-Authorized request", status=403)

    @view_config(route_name='get_all_players_o')    
    def get_all_players_o(request):
        return {}

    @view_config(route_name='get_player')
    def get_player(self):
        if self.request.user:
            try:
                player_id = self.request.matchdict['id']
                player = self.request.dbsession.query(models.Player).options(joinedload('events')).filter_by(id=player_id).first()
                if player is None:
                    raise HTTPNotFound
                player_schema = PlayerSchema()
                output = player_schema.dump(player).data
                pprint(output, indent=2)
                return Response('OK', status=200, json=output)    
            except DBAPIError as identifier:
                return Response(db_err_msg, content_type='text/plain', status=500)
        return Response("Un-Authorized request", status=403)
    
    @view_config(route_name='get_player_o')    
    def get_player_o(request):
        return {}

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
        if self.request.user:
            events = self.request.dbsession.query(models.Event).all()
            events_list = []
            event_schema = EventSchema()
            for event in events:
                output = event_schema.dump(event).data
                events_list.append(output)
            pprint(output, indent=2)
            return Response('OK', status=200, json=events_list)
        return Response("Un-Authorized request", status=403)

    @view_config(route_name='get_all_events_o')
    def get_all_events_o(self):
        return {}

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