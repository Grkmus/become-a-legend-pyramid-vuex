from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship
from .association import player_event_table

from .meta import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, unique=True)
    type_of_event = Column(Text)
    matches = relationship('Match', backref='event')
    attendees = relationship('Player', secondary=player_event_table, backref='events')


    

Index('event_index', Event.id, unique=True, mysql_length=255)