from typing import List

from marshmallow import Schema, fields, post_load

from dataclasses import dataclass


class DjangoRoleWithUsersSchema(Schema):

    id_ = fields.Int(data_key='id')
    name = fields.Str()
    users = fields.List(fields.Int())

    @post_load
    def get_object(self, data, **kwargs):
        return DjangoRoleWithUsersDTO(**data)


@dataclass
class DjangoRoleWithUsersDTO:
    id_: int
    name: str
    users: List[int]