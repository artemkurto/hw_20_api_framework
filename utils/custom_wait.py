import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def custom_wait(driver, locator: tuple[str, str], el_numbers=1, interval=0.5, timeout: int = 3):
    wait = WebDriverWait(driver, timeout)
    els_is_found = False
    start_time = time.time()

    while not els_is_found:
        els = wait.until(EC.presence_of_all_elements_located(locator))

        if len(els) >= el_numbers:
            return els
        time.sleep(interval)
        if time.time() - start_time > timeout:
            raise TimeoutError(f'can not fine {el_numbers} elements for locator {locator}')