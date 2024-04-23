from core.api_service.base_api import BaseApi


class DjangoAPIBase:

    api_executor = BaseApi()
    base_url = "http://localhost:8000/"
