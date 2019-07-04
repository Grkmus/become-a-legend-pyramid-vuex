from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship


from .meta import Base

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    event_id = Column(Integer, ForeignKey('events.id'))


    

Index('match_index', Match.id, unique=True, mysql_length=255)