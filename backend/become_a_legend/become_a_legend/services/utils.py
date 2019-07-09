from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from become_a_legend.models import ( Player, Event )



class EventSchema(ModelSchema):
    class Meta:
        model = Event
        # optionally attach a Session
        # to use for deserialization

class PlayerSchema(ModelSchema):
    events = fields.Nested(EventSchema, many=True)
    class Meta:
        model = Player