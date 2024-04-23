import json


class ConfigManager:

    with open('F:\Tests_0324\config_ui_test.json') as f:
        _data = f.read()

    _data = json.loads(_data)

    url = _data.get('BASE_URL')
    user_name = _data.get('BASE_USER')
    user_pass = _data.get('BASE_PASSWORD')
    browser = _data.get('BROWSER')


