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
        main_page.open_main_page()
        search_page.click_on_search()
        search_page.find_game(game_name='Dota 2')
        search_page.check_search_result(game_name='Dota 2')