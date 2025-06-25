from selene import browser, have


def test_search_field():
    browser.open()
    browser.element('[id="store_search_link"]').click()
    browser.element('[id="store_search_link"]').type('Dota 2')
    browser.element('.title').should(have.exact_text('Dota 2'))