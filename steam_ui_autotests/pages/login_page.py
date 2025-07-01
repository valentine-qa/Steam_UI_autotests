import allure
from selene import browser, have


class LoginPage:
    def click_login_button(self):
        with allure.step('Click login button'):
            browser.element('[class="global_action_link"]').click()

    def check_login_page(self):
        with allure.step('Check that login page is open'):
            browser.element('button[type="submit"]').should(have.exact_text('Sign in'))

login_page = LoginPage()