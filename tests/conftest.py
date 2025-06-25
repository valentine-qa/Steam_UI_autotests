import time

import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.driver_name = 'chrome'
    browser.config.window_width = '1800'
    browser.config.window_height = '1000'
    browser.config.base_url = 'https://store.steampowered.com'
    yield

    time.sleep(3)
    browser.quit()