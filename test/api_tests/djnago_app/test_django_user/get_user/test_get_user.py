from core.api_service.django_app.assertations.all_users_assert import assert_user
from test.api_tests.djnago_app.conftest import django_ctrl


def test_get_user(create_read_user):
    resp = django_ctrl.get_user(create_read_user.id_)
    assert_user(resp, create_read_user)