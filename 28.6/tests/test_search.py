
from pages.search import SearchPage


def test_search_button(get_webdriver):
    """ #46 Is search button works fine. """
    page = SearchPage(get_webdriver)
    page.wait_page_loaded()
    page.search_button('search')
    assert 'SearchText=search' in page.get_current_url()


def test_search_enter(get_webdriver):
    """ #47 Is search by ENTER key works fine. """
    page = SearchPage(get_webdriver)
    page.wait_page_loaded()
    page.search_enter('search')
    assert 'SearchText=search' in page.get_current_url()


def test_search_grammar_mistakes(get_webdriver):
    """ #48 Is search with grammar mistakes works fine. """
    page = SearchPage(get_webdriver)
    page.wait_page_loaded()
    page.search_button('windaws cleener')
    assert 'windows cleaner' == page.get_request()


def test_search_wrong_keyboard_layout(get_webdriver):
    """ #49 Is search with wrong keyboard layout works fine. """
    page = SearchPage(get_webdriver)
    page.wait_page_loaded()
    page.search_button('цштвщцы сдуфтук')
    assert 'windows cleaner' == page.get_request()


def test_search_no_item(get_webdriver):
    """ #50 Is search with hard request works fine. """
    page = SearchPage(get_webdriver)
    page.wait_page_loaded()
    page.search_button('лодка бочка очки призрак затычка телефон')
    assert 'мы не нашли товаров по Вашему запросу' in page.get_error_message()


def test_results_count(get_webdriver):
    """ #51 Is search results count works fine. """
    page = SearchPage(get_webdriver)
    page.wait_page_loaded()
    page.search_button('AQUAMARINA BLUE DRIVE POWER FIN')
    assert page.get_result_count() == page.get_product_count()
