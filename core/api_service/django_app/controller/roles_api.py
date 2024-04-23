from core.api_service.django_app.controller.base_api import DjangoAPIBase
from core.api_service.django_app.dtos.response_create_roles import DjangoRoleSchema, DjangoRoleDTO
from core.api_service.django_app.dtos.response_role_with_users import DjangoRoleWithUsersSchema, DjangoRoleWithUsersDTO
from core.utils.dtos_ustils import MessageSchema, MessageDTO


class DjangoRolesAPI(DjangoAPIBase):

    def __init__(self):
        self.roles_url = f"{self.base_url}api/roles/"

    def get_role_with_users(self, role_id, query_params=None) -> DjangoRoleWithUsersDTO:
        url = f'{self.roles_url}{role_id}/list_users/'
        return self.api_executor.get(url=url, params=query_params, expected_status_code=200,
                                     schema=DjangoRoleWithUsersSchema())

    def post_add_user(self, role_id, data=None, expected_status_code=201) -> MessageDTO:
        url = f'{self.roles_url}{role_id}/add_user/'
        return self.api_executor.post(url=url, data=data, expected_status_code=expected_status_code,
                                      schema=MessageSchema())

    def post_create_role(self, data=None, expected_status_code=201) -> DjangoRoleDTO:
        return self.api_executor.post(url=self.roles_url, data=data, expected_status_code=expected_status_code,
                                      schema=DjangoRoleSchema())

    def post_delete_role(self, role_id) -> DjangoRoleDTO:
        url = f'{self.roles_url}{role_id}/'

        return self.api_executor.delete(url=url, expected_status_code=204)

    def get_role(self, role_id, query_params=None) -> DjangoRoleDTO:
        url = f'{self.roles_url}{role_id}/'
        return self.api_executor.get(url=url, params=query_params, expected_status_code=200, schema=DjangoRoleSchema())

    def put_role(self, role_id, data=None, expected_status_code=200) -> DjangoRoleDTO:
        url = f'{self.roles_url}{role_id}/'
        return self.api_executor.put(url=url, data=data,
                                     expected_status_code=expected_status_code, schema=DjangoRoleSchema())

    def patch_role(self, role_id, data=None, expected_status_code=200) -> DjangoRoleDTO:
        url = f'{self.roles_url}{role_id}/'
        return self.api_executor.patch(url=url, data=data,
                                       expected_status_code=expected_status_code, schema=DjangoRoleSchema())