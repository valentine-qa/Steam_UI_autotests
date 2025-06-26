from re import search

import allure
from selene import browser, have


class SearchPage:
    def click_on_search_field(self):
        with allure.step('Click on search field'):
            browser.element('[id="store_nav_search_term"]').click()

    def find_game_via_title(self, game_name):
        with allure.step(f'Enter "{game_name}" in search field'):
            browser.element('[id="store_nav_search_term"]').type(game_name).press_enter()

    def open_first_game_in_search_row(self, game_name):
        with allure.step(f'Open a first game in search results'):
            browser.element('[id="search_resultsRows"] a').click()

    def check_game_title(self, game_name):
        with allure.step(f'Check that game title is "{game_name}"'):
            browser.element('[id="appHubAppName"]').should(have.exact_text(game_name))





search_page = SearchPage()