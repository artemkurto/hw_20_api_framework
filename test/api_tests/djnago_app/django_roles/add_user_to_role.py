from core.api_service.django_app.controller.roles_api import DjangoRolesAPI

django_role_ctrl = DjangoRolesAPI()


def test_add_user_to_role(create_read_role, create_read_user_function_scope):
    role = create_read_role
    user = create_read_user_function_scope

    django_role_ctrl.post_add_user(role_id=role.id_, data={'user_id': user.id_})

    resp = django_role_ctrl.get_role_with_users(role.id_)

    assert user.id_ in resp.users


def test_add_user_to_role_twice(create_read_role, create_read_user_function_scope):
    role = create_read_role
    user = create_read_user_function_scope

    django_role_ctrl.post_add_user(role_id=role.id_, data={'user_id': user.id_})
    django_role_ctrl.post_add_user(role_id=role.id_, data={'user_id': user.id_}, expected_status_code=400)

