from dataclasses import dataclass
from faker import Faker


@dataclass
class PayloadDjangoRoleDTO:
    name: str = None

    def serialize(self):
        return self.__dict__

    @classmethod
    def random(cls, **kwargs):
        faker = Faker()

        data = {
            'name': faker.name(),
            **kwargs
        }

        return cls(**data)
