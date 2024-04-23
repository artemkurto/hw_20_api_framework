from pytest import mark

from core.api_service.django_app.assertations.create_user_validation_assert import \
    assert_user_created_validation
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO
from core.api_service.django_app.utils.validations_messages import *
from test.api_tests.djnago_app.conftest import django_ctrl


@mark.parametrize('user_name, error_text',
                  [
                      (None, REQUIRED_FIELD),
                      ('', EMPTY_FIELD),
                      ('a', USERNAME_VALIDATION),
                      ('as', USERNAME_VALIDATION),
                      ([1, 2, 3], USERNAME_VALIDATION),
                  ],
                  ids=['None', 'empty', '1 char(3 min)', '2 chars(3 min)', 'list'])
def test_create_users_wrong_username(user_name, error_text):
    user_data = PayloadDjangoUserDTO.random(username=user_name)
    resp = django_ctrl.create_user(body=user_data.serialize(), expected_status_code=400)

    assert_user_created_validation(resp, error_text, 'username')


@mark.parametrize('property_value, error_text',
                  [
                      (None, REQUIRED_FIELD),
                      ('', EMPTY_FIELD),
                  ],
                  ids=['None', 'empty'])
@mark.parametrize('property_name', ['username', 'password', 'email'])
def test_create_users_wrong_data_for_properties(property_value, error_text, property_name):
    user_data = PayloadDjangoUserDTO.random().serialize()

    user_data[property_name] = property_value
    resp = django_ctrl.create_user(body=user_data, expected_status_code=400)

    assert_user_created_validation(resp, error_text, property_name)


@mark.parametrize('password',
                  [
                      'aA1', 'aAAA1', 'a' * 6, 'A' * 6, 555558, [1, 2, 3],
                  ],
                  ids=['3 char(6 min)', '5 chars(6 min)',
                       'only small', 'only capital', 'only numbers', 'list'])
def test_create_users_wrong_password(password):
    user_data = PayloadDjangoUserDTO.random(password=password)
    resp = django_ctrl.create_user(body=user_data.serialize(), expected_status_code=400)

    assert_user_created_validation(resp, PASSWORD_VALIDATION, 'password')
