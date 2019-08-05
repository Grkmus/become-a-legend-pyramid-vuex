from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DATE,
    TIME,
)
print('denemeleer')
from sqlalchemy.orm import relationship
from .association import player_event_table

from .meta import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, unique=True)
    date = Column(DATE)
    time = Column(TIME)
    location = Column(Text)
    type_of_event = Column(Text)
    matches = relationship('Match', backref='event')
    attendees = relationship('Player', secondary=player_event_table, backref='events', lazy='joined')

    def to_json(self):
        return dict(
            id = self.id,
            name = self.name,
            date = self.date,
            time = self.time,
            location = self.location,
            type_of_event = self.type_of_event,
            matches = self.matches,
            attendees = self.attendees
        )

    

Index('event_index', Event.id, unique=True, mysql_length=255)