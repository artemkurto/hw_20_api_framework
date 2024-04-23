from marshmallow import Schema, fields, post_load

from dataclasses import dataclass


class DjangoRoleSchema(Schema):

    id_ = fields.Int(data_key='id')
    name = fields.Str()

    @post_load
    def get_object(self, data, **kwargs):
        return DjangoRoleDTO(**data)


@dataclass
class DjangoRoleDTO:
    id_: int
    name: str