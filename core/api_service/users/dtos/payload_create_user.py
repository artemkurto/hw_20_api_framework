import random

from faker import Faker


class CreateUserPayload:

    faker = Faker()

    def __init__(self, name, email, gender, status):
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    @classmethod
    def random(cls, name=None, email=None, gender=None, status=None):

        return cls(
            name=name or cls.faker.name(),
            email=email or cls.faker.email(),
            gender=gender or random.choice(["male", "female"]),
            status=status or random.choice(["active", "inactive"]),

        )

    def get_dict(self):
        return self.__dict__