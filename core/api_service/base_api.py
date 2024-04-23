import logging

import requests


logger = logging.getLogger(__file__)


class BaseApi:

    def __execute_request(self, method, url, params=None, data=None, headers=None, expected_status_code=None,
                          schema=None):
        logger.info(f'send {method}request to {url} with params {params}\nbody = {data}')
        response = requests.request(
            method=method,
            url=url,
            params=params or {},  # None or {} = {}, {1:2} or {} = {1:2}
            data=data,
            headers=headers or {}
        )
        logger.info(f'response is {response.status_code}')
        logger.info(response.text)
        if expected_status_code:
            assert response.status_code == expected_status_code, (f'Incorrect status code for {response.url}\n'
                                                                  f'expected {expected_status_code}\n'
                                                                  f'actual {response.status_code}')
        if response.status_code < 400 and schema:
            return schema.load(response.json())
        if response.text:  # response is not empty
            return response.json()
        else:
            return response.text

    def get(self, url, params=None, headers=None, expected_status_code=None, schema=None):
        return self.__execute_request('get', url=url, params=params, headers=headers,
                                      expected_status_code=expected_status_code, schema=schema)

    def post(self, url, data=None, headers=None, expected_status_code=None, schema=None):
        return self.__execute_request('post', url=url, data=data, headers=headers,
                                      expected_status_code=expected_status_code, schema=schema)

    def put(self, url, data=None, headers=None, expected_status_code=None, schema=None):
        return self.__execute_request('put', url=url, data=data, headers=headers,
                                      expected_status_code=expected_status_code, schema=schema)

    def patch(self, url, data=None, headers=None, expected_status_code=None, schema=None):
        return self.__execute_request('patch', url=url, data=data, headers=headers,
                                      expected_status_code=expected_status_code, schema=schema)

    def delete(self, url, headers=None, expected_status_code=None):
        return self.__execute_request('delete', url=url, headers=headers,
                                      expected_status_code=expected_status_code)
