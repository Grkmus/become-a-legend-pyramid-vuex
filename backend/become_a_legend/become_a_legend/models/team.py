from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base
from .association import match_team_table

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    players = relationship('Player', backref='team')
    matches = relationship('Match', secondary=match_team_table, backref='team')
    

Index('team_index', Team.id, unique=True, mysql_length=255)