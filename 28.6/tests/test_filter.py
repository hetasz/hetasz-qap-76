import pytest
from pages.filter import FilterPage


def test_breadcrumb(get_webdriver):
    """ #23 Is breadcrumbs works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    page.breadcrumb()
    assert page.get_current_url()[:49] == 'https://aliexpress.ru/all-wholesale-products.html'


def test_category(get_webdriver):
    """ #24 Is category link works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    page.category()
    assert page.get_current_url()[:49] == 'https://aliexpress.ru/all-wholesale-products.html'


def test_price_low(get_webdriver):
    """ #25 Is price low edit works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.price_low()


def test_ranges(get_webdriver):
    """ #26 Is ranges works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.ranges()


def test_free_delivery(get_webdriver):
    """ #27 Is free delivery checkbox works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.free_delivery()


def test_stars_filter(get_webdriver):
    """ #28 Is stars filter checkbox works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.stars_filter()


def test_sort_by_order(get_webdriver):
    """ #29 Is sort by order works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.sort_by_order()


def test_list_view(get_webdriver):
    """ #30 Is list view works fine. """
    page = FilterPage(get_webdriver, 'https://aliexpress.ru/category/202040662/camera-drones.html?g=y')
    page.wait_page_loaded()
    assert page.list_view()


def test_pagination(get_webdriver):
    """ #31 Is pagination links works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.pagination()


@pytest.mark.parametrize("_page", ['2', '3'], ids=['second page', 'third page'])
def test_pagination_jump(get_webdriver, _page):
    """ #32 Is pagination jumping works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert page.pagination_jump(_page)


@pytest.mark.parametrize("_page", ['a', '999'], ids=['symbolic', 'overwhelming'])
def test_pagination_jump_negative(get_webdriver, _page):
    """ #33 Is pagination jumping works fine. """
    page = FilterPage(get_webdriver)
    page.wait_page_loaded()
    assert not page.pagination_jump(_page)
