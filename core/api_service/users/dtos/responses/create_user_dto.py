"""
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status
"""

from marshmallow import Schema, fields, post_load, validate
from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    email: str
    name: str
    gender: str
    status: str

    def get_dict(self):
        return self.__dict__


class UserSchema(Schema):

    id = fields.Int(strict=True)
    name = fields.Str()
    email = fields.Str(validate=validate.Email())
    gender = fields.Str(required=True)
    status = fields.Str()

    @post_load
    def get_object(self, data, **kwargs):
        return UserDTO(**data)




# class CreateUserDto:
#
#     def __init__(self, id: int, name:str , gender:str, status:str):
#         self.id = id
#         self.name = name
#         self.gender = gender
#         self.status = status


if __name__ == '__main__':
    ship = UserSchema().load({'id': 1, 'name': 'Den', 'status': 'Alive', 'gender': 'Male'})
    print(ship.gender)


