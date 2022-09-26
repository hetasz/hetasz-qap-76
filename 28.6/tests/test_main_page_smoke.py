

import pytest

import conftest
from pages.main_page import MainPage


def test_logo_click(get_webdriver):
    """ #04 Is logo link works fine. """
    page = MainPage(get_webdriver)
    page.logo_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:22] == 'https://aliexpress.ru/'


def test_top_banner_click(get_webdriver):
    """ #05 Is top_banner link works fine. """
    page = MainPage(get_webdriver)
    page.top_banner_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:32] == 'https://campaign.aliexpress.com/'


def test_application_click(get_webdriver):
    """ #06 Is application link works fine. """
    page = MainPage(get_webdriver)
    page.application_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:32] == 'https://promotion.aliexpress.ru/'


def test_seller_click(get_webdriver):
    """ #07 Is seller link works fine. """
    page = MainPage(get_webdriver)
    page.seller_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:29] == 'https://seller.aliexpress.ru/'


def test_close_cookie_bar_click(get_webdriver):
    """ #08 Is cookie bar close works fine. """
    page = MainPage(get_webdriver)
    cookie_bar = page.close_cookie_bar_click()
    page.wait_page_loaded()
    assert cookie_bar == []


def test_smartphones_menu_click(get_webdriver):
    """ #09 Is seller link works fine. """
    page = MainPage(get_webdriver)
    page.smartphones_menu_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:51] == 'https://aliexpress.ru/category/202001195/cellphones'


def test_show_more_click(get_webdriver):
    """ #10 Is 'show more' button works fine. """
    page = MainPage(get_webdriver)
    first_count = page.count_item_box_elements()
    page.show_more_click()
    page.wait_page_loaded()
    second_count = page.count_item_box_elements()
    assert first_count < second_count


def test_new_user_click(get_webdriver):
    """ #11 Is new user button works fine """
    page = MainPage(get_webdriver)
    page.new_user_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:42] == 'https://sale.aliexpress.ru/ru/__pc/Newuser'


def test_bad_link_click(get_webdriver):
    """ #12 Is 404 redirect works fine """
    page = MainPage(get_webdriver, 'https://aliexpress.ru/j')
    page.wait_page_loaded()
    assert page.get_current_url()[:43] == 'https://www.aliexpress.com/p/error/404.html'


def test_get_copyright(get_webdriver):
    """ #13 Is copyright available """
    page = MainPage(get_webdriver)
    _copyright = page.get_copyright()
    assert 'AliExpress.ru. Все права защищены.' in _copyright


@pytest.mark.parametrize("_request", ['power', conftest.generate_string(255)], ids=['power', '255 symbols'])
def test_search_button_click(get_webdriver, _request):
    """ #14 Is search button works fine. """
    page = MainPage(get_webdriver)
    page.do_search(_request)
    page.wait_page_loaded()
    assert page.get_current_url()[:50] == 'https://aliexpress.ru/wholesale?catId=&SearchText='


def test_robots_txt(get_webdriver):
    """ #15 Is robots.txt available """
    page = MainPage(get_webdriver, 'https://aliexpress.ru/robots.txt')
    page.wait_page_loaded()
    assert len(page.get_google_bot()) > 1
