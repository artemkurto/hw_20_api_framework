from core.api_service.django_app.assertations.all_users_assert import assert_user_was_created
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO
from test.api_tests.djnago_app.conftest import django_ctrl


def test_create_users():
    user_data = PayloadDjangoUserDTO.random()
    resp = django_ctrl.create_user(body=user_data.serialize())
    assert_user_was_created(expected_user=user_data, user_id=resp.id_)

