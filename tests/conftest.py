import os

import pytest
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene import browser

from steam_ui_autotests.utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://store.steampowered.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    # attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
































# import time
#
# import pytest
# from selene import browser
#
#
# @pytest.fixture(scope='function', autouse=True)
# def browser_config():
#     browser.config.driver_name = 'chrome'
#     browser.config.window_width = '1800'
#     browser.config.window_height = '1000'
#     browser.config.base_url = 'https://store.steampowered.com'
#     yield
#
#     time.sleep(3)
#     browser.quit()