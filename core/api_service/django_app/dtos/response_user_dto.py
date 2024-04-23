from marshmallow import Schema, fields, post_load

from dataclasses import dataclass


class DjangoUserSchema(Schema):

    id_ = fields.Int(data_key='id')
    username = fields.Str()
    email = fields.Email()

    @post_load
    def get_object(self, data, **kwargs):
        return DjangoUserDTO(**data)


@dataclass
class DjangoUserDTO:
    id_: int
    username: str
    email: str