from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.dtos.response_create_roles import DjangoRoleDTO
from assertpy import soft_assertions, assert_that

django_ctrl = DjangoRolesAPI()


def assert_role(actual_role: DjangoRoleDTO, expected_role: DjangoRoleDTO):
    with soft_assertions():
        assert_that(actual_role.name, 'username').is_equal_to(expected_role.name)


def assert_role_was_created_or_changed(expected_role: DjangoRoleDTO, role_id: int):
    api_role = django_ctrl.get_role(role_id)
    assert_role(api_role, expected_role)


def assert_role_created_validation(response, expected_text,):
    assert_that(response).is_equal_to(expected_text)
