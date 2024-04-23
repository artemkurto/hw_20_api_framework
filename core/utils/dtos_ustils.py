from marshmallow import Schema, fields, post_load

from dataclasses import dataclass


class MessageSchema(Schema):
    message = fields.Str()

    @post_load
    def get_object(self, data, **kwargs):
        return MessageDTO(**data)


@dataclass
class MessageDTO:
    message: str
