from core.api_service.django_app.controller.base_api import DjangoAPIBase
from core.api_service.django_app.dtos.payload_user_dto import PayloadDjangoUserDTO
from core.api_service.django_app.dtos.response_user_dto import DjangoUserDTO, DjangoUserSchema


class DjangoUsersAPIUsers(DjangoAPIBase):

    def __init__(self):
        self.users_url = f"{self.base_url}api/users/"

    def get_all_users(self, query_params=None) -> [DjangoUserDTO]:

        return self.api_executor.get(url=self.users_url, params=query_params, expected_status_code=200,
                                     schema=DjangoUserSchema(many=True))

    def get_user(self, user_id) -> DjangoUserDTO:

        return self.api_executor.get(url=self.users_url + f'{user_id}',
                                     expected_status_code=200,
                                     schema=DjangoUserSchema())

    def create_user(self, body: PayloadDjangoUserDTO, expected_status_code=201) -> DjangoUserDTO:

        return self.api_executor.post(
            url=self.users_url,
            data=body,
            expected_status_code=expected_status_code,
            schema=DjangoUserSchema()
        )

    def update_user(self, body: PayloadDjangoUserDTO, expected_status_code=201) -> DjangoUserDTO:

        return self.api_executor.put(
            url=self.users_url,
            data=body,
            expected_status_code=expected_status_code,
            schema=DjangoUserSchema()
        )

    def delete_user(self, user_id, expected_status_code=204) -> None:

        self.api_executor.delete(
            url=self.users_url + f'{user_id}/',
            expected_status_code=expected_status_code
        )
