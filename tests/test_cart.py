import allure
from allure_commons.types import Severity

from steam_ui_autotests.pages.cart_page import cart_page
from steam_ui_autotests.pages.main_page import main_page
from steam_ui_autotests.pages.search_page import search_page


@allure.epic('Cart')
@allure.feature('Add and Remove games from Cart')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestCart:
    @allure.title('Add game to cart')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('Owner', 'valentine-qa')
    def test_add_game_to_cart(self, local_browser_config):
        game_name = 'Outlast'

        main_page.open_main_page()

        search_page.click_on_search_field()
        search_page.find_game_via_title(game_name)
        search_page.open_first_game_in_search_row(game_name)

        cart_page.add_game_to_cart()
        cart_page.move_to_cart()
        cart_page.check_game_in_cart(game_name)

    @allure.title('Remove game from cart')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('Owner', 'valentine-qa')
    def test_remove_game_from_cart(self):
        game_name = 'Outlast'

        main_page.open_main_page()

        search_page.click_on_search_field()
        search_page.find_game_via_title(game_name)
        search_page.open_first_game_in_search_row(game_name)

        cart_page.add_game_to_cart()
        cart_page.move_to_cart()
        cart_page.remove_game_from_cart(game_name)

        cart_page.check_game_not_in_cart(game_name)

    @allure.title('Clear cart')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('Owner', 'valentine-qa')
    def test_clear_cart(self):
        game_name_one = 'Outlast'
        game_name_two = 'Outlast 2'

        main_page.open_main_page()

        search_page.click_on_search_field()
        search_page.find_game_via_title(game_name_one)
        search_page.open_first_game_in_search_row(game_name_one)
        cart_page.add_game_to_cart()

        search_page.click_on_search_field()
        search_page.find_game_via_title(game_name_two)
        search_page.open_first_game_in_search_row(game_name_two)
        cart_page.add_game_to_cart()
        cart_page.move_to_cart()

        cart_page.clear_cart()
        cart_page.check_cart_is_empty()