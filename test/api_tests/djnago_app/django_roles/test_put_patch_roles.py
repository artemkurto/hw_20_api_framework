import pytest
from core.api_service.django_app.assertations.create_role_assert import *
from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO
django_role_ctrl = DjangoRolesAPI()


def test_put_role(create_read_role):
    role_data = PayloadDjangoRoleDTO.random()
    resp_create = create_read_role
    resp_put = django_role_ctrl.put_role(role_id=resp_create.id_, data=role_data.serialize())
    assert_role_was_created_or_changed(expected_role=role_data, role_id=resp_put.id_)


def test_patch_role_negative(create_read_role):
    expected_response = {'name': ['This field may not be blank.']}
    role_data = PayloadDjangoRoleDTO.random(name='')
    resp_create = create_read_role
    resp_patch = django_role_ctrl.patch_role(role_id=resp_create.id_,
                                             data=role_data.serialize(), expected_status_code=400)
    assert_role_created_validation(resp_patch, expected_response)


@pytest.mark.xfail
def test_patch_role_negative_with_none(create_read_role):
    expected_response = {'name': ['This field may not be blank.']}
    role_data = PayloadDjangoRoleDTO.random(name=None)
    resp_create = create_read_role
    resp_patch = django_role_ctrl.patch_role(role_id=resp_create.id_,
                                             data=role_data.serialize(), expected_status_code=400)
    assert_role_created_validation(resp_patch, expected_response)
