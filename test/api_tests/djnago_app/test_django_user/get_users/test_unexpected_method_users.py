from pytest import mark

from test.api_tests.djnago_app.conftest import django_ctrl


@mark.parametrize('method', ['delete', 'put', 'patch'])
def test_unexpected_method_all_users_with_params(method):
    # getattr(django_ctrl.api_executor, method)  ==  django_ctrl.api_executor."method"

    getattr(django_ctrl.api_executor, method)(url=django_ctrl.users_url, expected_status_code=405)
