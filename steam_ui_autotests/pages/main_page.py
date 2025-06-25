import allure
from selene import browser


class MainPage:
    def open_main_page(self):
        with allure.step('Open "Steam" main page'):
            browser.open('/')


main_page = MainPage()