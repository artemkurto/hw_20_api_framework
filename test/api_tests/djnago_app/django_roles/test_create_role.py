from pytest import mark
from core.api_service.django_app.assertations.create_role_assert import *
from core.api_service.django_app.controller.roles_api import DjangoRolesAPI
from core.api_service.django_app.dtos.payload_role_dto import PayloadDjangoRoleDTO
django_role_ctrl = DjangoRolesAPI()


def test_create_role():
    role_data = PayloadDjangoRoleDTO.random()
    resp = django_role_ctrl.post_create_role(data=role_data.serialize())
    assert_role_was_created_or_changed(expected_role=role_data, role_id=resp.id_)
    django_role_ctrl.post_delete_role(resp.id_)


@mark.parametrize('name', ['', None,])
def test_create_role_negative(name):
    expected_response = {'error': 'Name is required'}
    role_data = PayloadDjangoRoleDTO.random(name=name)
    resp = django_role_ctrl.post_create_role(data=role_data.serialize(), expected_status_code=400)
    assert_role_created_validation(resp, expected_response)

