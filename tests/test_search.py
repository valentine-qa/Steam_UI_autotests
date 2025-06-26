import allure
from allure_commons.types import Severity
from selene import browser, have

from steam_ui_autotests.pages.main_page import main_page
from steam_ui_autotests.pages.search_page import search_page

@allure.epic('Search')
@allure.feature('Search field')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestSearch:
    @allure.title('Find game via search field')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('Owner', 'valentine-qa')
    def test_search_field(self):
        game_name = 'Dota 2'

        main_page.open_main_page()

        search_page.click_on_search_field()
        search_page.find_game_via_title(game_name)
        search_page.open_first_game_in_search_row(game_name)

        search_page.check_game_title(game_name)