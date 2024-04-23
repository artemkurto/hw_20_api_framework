import pytest
from core.api_service.django_app.controller.users_api import DjangoUsersAPIUsers
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO

django_ctrl = DjangoUsersAPIUsers()
created_users = []


@pytest.fixture(scope='session', autouse=True)
def create_read_user():
    user_data = PayloadDjangoUserDTO.random()
    resp = django_ctrl.create_user(user_data.serialize())
    created_users.append(resp.id_)
    yield resp
    django_ctrl.delete_user(resp.id_)


# @pytest.fixture(scope='session', autouse=True)
# def delete_user_function_scope():
#     yield
#     for k in created_users:
#         django_ctrl.delete_user(k.id_)
