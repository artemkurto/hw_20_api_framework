from enum import Enum


class Enviroments(Enum):

    DEV = 'dev'
    STAGE = 'stage'
    PROD = 'prod'


class UserNames(Enum):

    VALID_NAME = 'Den'
    INVALID_NAME = 23
    NONE_NAME = None


class AuthTokenInvalid(Enum):

    INVALID_STRING = 'asdasd'
    INVALID_TYPE = 'Base 3242477d83cfc80363eb54ba6d030a851202f93fedaa3c05ae2ecc0449b2831d'
    EMPTY_TOKEN = ''