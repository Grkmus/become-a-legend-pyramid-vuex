from .meta import Base
from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey
)

player_event_table = Table('player_event', Base.metadata,
    Column('player_id', Integer, ForeignKey('players.id')),
    Column('event_id', Integer, ForeignKey('events.id'))
)

match_team_table = Table('match_team', Base.metadata,
    Column('match_id', Integer, ForeignKey('matches.id')),
    Column('team_id', Integer, ForeignKey('teams.id'))
)

