
from pages.shopcart import ShopcartPage


def test_empty_shopcart(get_webdriver):
    """ #16 Is empty shopcart shows whoops message. """
    page = ShopcartPage(get_webdriver)
    page.wait_page_loaded()
    # assert page.whoops_label.get_text() == 'Ой, пусто!'
    assert page.whoops_label2.get_text()[:18].lower() == 'Ваша корзина пуста'.lower()


def test_adding_to_shopcart(get_webdriver):
    """ #17 Is shopcart can collect items. """
    page = ShopcartPage(get_webdriver)
    page.wait_page_loaded()
    page.add_random_stuff_to_cart()
    assert page.cart_positions_count() > 0


def test_calculate_shopcart(get_webdriver):
    """ #18 Is shopcart calculate sum correctly. """
    page = ShopcartPage(get_webdriver)
    page.wait_page_loaded()
    page.add_random_stuff_to_cart()
    assert page.calculate_shopcart() != '0,00 руб.'


def test_increment_item(get_webdriver):
    """ #19 Is increment item count works fine. """
    page = ShopcartPage(get_webdriver)
    page.wait_page_loaded()
    page.add_random_stuff_to_cart()
    assert page.increment_item()


def test_delete_item(get_webdriver):
    """ #20 Is delete item works fine. """
    page = ShopcartPage(get_webdriver)
    page.wait_page_loaded()
    page.add_random_stuff_to_cart()
    assert page.delete_item()[:18].lower() == 'Ваша корзина пуста'.lower()


def test_purchase(get_webdriver):
    """ #21 Is purchase button works fine. """
    page = ShopcartPage(get_webdriver)
    page.wait_page_loaded()
    page.add_random_stuff_to_cart()
    assert page.purchase() > 0


def test_open_shopcart(get_webdriver):
    """ #22 Is shopcart button works fine. """
    page = ShopcartPage(get_webdriver, "https://aliexpress.ru/")
    page.wait_page_loaded()
    page.oper_shopcart()
    assert page.get_current_url()[:62] == 'https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail.htm'
