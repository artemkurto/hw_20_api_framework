from marshmallow import Schema, fields, post_load, validate

from dataclasses import dataclass


@dataclass
class PilotDTO:
    name: str
    id: str


@dataclass
class StarShipDTO:
    name: str
    from_field: str
    pilots: list[PilotDTO]
    pilot: PilotDTO = None


class PilotSchema(Schema):
    name = fields.Str(validate=validate.Length(min=3, max=25))
    id = fields.Int(strict=True)

    @post_load
    def serialize(self, data, **kwarg):

        return PilotDTO(**data)


class StarShipSchema(Schema):
    name = fields.Str()
    from_field = fields.Integer(data_key='from')
    pilots = fields.List(fields.Nested(PilotSchema))
    pilot = fields.Nested(PilotSchema)

    @post_load
    def serialize(self, data, **kwarg):
        #
        # requred_fields = ['name', ...]
        # new_data = {}
        # for k in requred_fields:
        #     new_data[k] = data.get(k, None)
        #
        # for k in data:
        #     if k not in requred_fields:
        #         logger.warning(f'Unexpeced field {k}')
        # new_data = {
        #     "name": data.get('name', None),
        #     "from_field": data.get('from_field', None),
        #     "pilots": data.get('pilots', None),
        #     "pilot": data.get('pilot', None)
        # }

        return StarShipDTO(**data)


if __name__ == '__main__':
    data = [{
        'name': 'spaceship Milenium',
        'from': 10,
        'pilots': [
            {
                'id': 1,
                'name': 'Den',
            },
            {
                'id': 2,
                'name': 'Arthur',
            },
        ],
        'pilot':
            {
                'id': 1,
                'name': 'Den',
            }

    }
    ]

    starships = StarShipSchema(many=True).load(data)

    for starship in starships:
        assert starship.id < 11
        assert starship.pilot.id == 2

#
# def sum_2_num(num_1: int, num_2: int):
#     return num_1 + num_2
#
#
# print(sum_2_num(1,2))
#
# print(sum_2_num(num_1=3, num_2=4))
# print(sum_2_num(**{'num_1': 5, 'num_2': 6}))
#
# StarShipDTO(**{'name': 'asd', 'from_field': 10, 'pilots': [1,2,3]})
