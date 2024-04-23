from dataclasses import dataclass
from faker import Faker


@dataclass
class PayloadDjangoUserDTO:
    password: str = None
    username: str = None
    email: str = None

    def serialize(self):
        return self.__dict__

    @classmethod
    def random(cls, **kwargs):
        faker = Faker()

        data = {
            'username': faker.name()[:10],
            'password': 'Password11',
            'email': faker.email(),
            **kwargs
        }

        return cls(**data)
