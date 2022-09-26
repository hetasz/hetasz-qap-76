import pytest


@pytest.mark.xfail(reason="view doesn't work")
def test_view(get_webdriver):
    """ # Удаляются символы из адресной строки при переключении вида (лист-список) в категориях """


@pytest.mark.xfail(reason="categorie's cart counter doesn't work")
def test_categories_cart_counter(get_webdriver):
    """ # Не отображается количество товара в корзине в категориях """


@pytest.mark.xfail(reason="deleting cart counter doesn't work")
def test_deleting_cart_counter(get_webdriver):
    """ # Не меняется наклейка счетчика количество товара на ярлыке иконки корзины в корзине при удалении позиции """
