import allure
from selene import browser, have, be
from selene.support.conditions.be import not_


class CartPage:

    def add_game_to_cart(self):
        with allure.step("Add game to the cart"):
            browser.element('.btn_addtocart').click()

    def open_cart(self):
        with allure.step('Open cart'):
            browser.element('[id="cart_status_data"]').click()

    def move_to_cart(self):
        with allure.step('Move to cart'):
            browser.all('button[class*="DialogButton"]').second.click()

    def check_game_in_cart(self, game_name):
        with allure.step(f'Check that game "{game_name}" in the cart'):
            browser.all('[class="Panel Focusable"]').element_by(have.text(game_name)).should(be.visible)

    def remove_game_from_cart(self, game_name):
        with allure.step(f"Remove game '{game_name}' from cart"):
            browser.all('[class="Panel Focusable"]').element_by(have.text(game_name)).all('[role="button"]').second.click()

    def check_game_not_in_cart(self, game_name):
        with allure.step(f'Check that game "{game_name}" not in cart'):
            browser.all('[class="Panel Focusable"]').element_by(have.text(game_name)).should(not_.visible)

    def clear_cart(self):
        with allure.step("Clear cart"):
            browser.element('._12zYFuKO2U-1QfeVxlGfwF').click()

    def check_cart_is_empty(self):
        with allure.step("Check that cart is empty"):
            browser.element('[class="Panel Focusable"]').should(have.text('Your cart is empty.'))


cart_page = CartPage()