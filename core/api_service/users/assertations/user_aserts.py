from assertpy import assert_that, soft_assertions

from core.api_service.users.dtos.payload_create_user import CreateUserPayload
from core.api_service.users.dtos.responses.create_user_dto import UserDTO


class UserAsserts:

    @staticmethod
    def assert_created_user(expected_body: CreateUserPayload, actual_body: UserDTO):

        assert_that(expected_body.name, 'name').is_equal_to(actual_body.name)
        assert_that(expected_body.gender, 'name').is_equal_to(actual_body.gender)
        assert_that(expected_body.email, 'name').is_equal_to(actual_body.email)

        actual_body = actual_body.get_dict()
        expected_body = expected_body.get_dict()
        with soft_assertions():
            for k in expected_body:
                assert_that(expected_body[k], k).is_equal_to(actual_body[k])


