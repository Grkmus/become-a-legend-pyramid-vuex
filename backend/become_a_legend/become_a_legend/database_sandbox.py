import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, JSON, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Table
 
Base = declarative_base()

player_event_table = Table('association', Base.metadata,
    Column('player_id', Integer, ForeignKey('players.id')),
    Column('event_id', Integer, ForeignKey('events.id')),
)

match_team_table = Table('association2', Base.metadata,
    Column('match_id', Integer, ForeignKey('matches.id')),
    Column('team_id', Integer, ForeignKey('teams.id')),
)
 
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True)
    name = Column(Text)
    surname = Column(Text)
    email = Column(Text)
    imageurl = Column(Text)
    team_id = Column(Integer, ForeignKey('teams.id'))
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    location = Column(Text)
    telephone = Column(Text)
    ratings_by_own = Column(JSON)
    rating_evaluation = Column(FLOAT)
    credit = Column(FLOAT)
    role_preference = Column(Integer)

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    players = relationship('Player', backref='team')
    matches = relationship('Match', secondary=match_team_table, backref='team')

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    event_id = Column(Integer, ForeignKey('events.id'))

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    type_of_event = Column(Text)
    matches = relationship('Match', backref='event')
    attendees = relationship('Player', secondary=player_event_table, backref='events')
 

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('postgresql://postgres:carter@localhost:5433/become_a_legend')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)