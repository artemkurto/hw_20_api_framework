from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options


class DriverFactory:

    def __init__(self, driver_type: str):
        self._driver_type = driver_type

    def get_driver(self):
        if self._driver_type.lower() == 'chrome':
            options = Options()
            # options.add_argument('--headless')
            return webdriver.Chrome(options=options)
        elif self._driver_type.lower() == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError(f'Unknown browser: {self._driver_type}')
