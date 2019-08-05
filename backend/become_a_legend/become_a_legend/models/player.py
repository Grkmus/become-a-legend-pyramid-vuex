from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    JSON,
    FLOAT,
    ForeignKey,
)
print('OLAYLAAAR')
from sqlalchemy.orm import relationship, validates
import bcrypt
from .meta import Base
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True, nullable=False)
    name = Column(Text)
    surname = Column(Text)
    email = Column(Text, nullable=False)
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
    password_hash = Column(Text)

    # def __init__(self, request, id, username, name, surname, email, imageURL, team_id, age, weight, height, location, telephone, ratings_by_Own, rating_evaluation, credit, rolePreference):
    #     self.request = request
    #     self.id = id
    #     self.username = username
    #     self.name = name
    #     self.surname = surname
    #     self.email = email
    #     self.imageurl = imageURL
    #     self.team_id = team_id
    #     self.age = age
    #     self.weight = weight
    #     self.height = height
    #     self.location = location
    #     self.telephone = telephone
    #     self.ratings_by_own = ratings_by_own
    #     self.rating_evaluation = rating_evaluation
    #     self.credit = credit
    #     self.role_preference = rolePreference


    def to_json(self):
        return dict(
            id = self.id,
            name = self.name,
            surname = self.surname,
            email = self.email,
            imageurl = self.imageurl,
            team_id = self.team_id,
            age = self.age,
            weight = self.weight,
            height = self.height,
            location = self.location,
            telephone = self.telephone,
            ratings_by_own = self.ratings_by_own,
            rating_evaluation = self.rating_evaluation,
            credit = self.credit,
            role_preference = self.role_preference,
            events = self.events
        )
        
    def set_password(self, pw):
        if len(pw) < 6:
            raise Exception('Password can not be less then 6 char long.')
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False
    
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        return email
    
    def check_token_set_user(self):
        authHeader = self.request.authorization.params
        return authHeader
    
    # @property    
    # def to_json(self):
    #     dict_json = {}
    #     for field in dir(self):
    #         if not field.startswith('_'):
    #             dict_json.update({field:str(getattr(self,field))})
    #     return dict_json

Index('player_index', Player.id, unique=True, mysql_length=255)

# name: String,
#     surname: String,
#     email: String,
#     imageURL: String,
#     age: Number,
#     weight: Number,
#     height: Number,
#     location: String,
#     telephone: String,
#     ratingsByOwn: {
#         power: Number,
#         speed: Number,
#         stamina: Number,
#         handling: Number,
#         offense: Number,
#         defense: Number,
#         teamplay: Number,
#         individualSkill: Number,
#     },
#     ratingEvaluation: Number,
#     credit: Number,
#     rolePreference: Array