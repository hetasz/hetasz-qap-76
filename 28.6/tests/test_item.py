from pages.item import ItemPage


def test_breadcrumb(get_webdriver):
    """ #34 Is breadcrumbs works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    page.breadcrumb()
    assert page.get_current_url()[:65] == 'https://aliexpress.ru/category/202000014/security-protection.html'


def test_coupons(get_webdriver):
    """ #35 Is coupons works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.coupons() > 0


def test_sales_leader(get_webdriver):
    """ #36 Is sales leader link works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    page.sales_leader()
    assert page.get_current_url()[:48] != 'https://aliexpress.ru/item/1005002278446127.html'


def test_colors(get_webdriver):
    """ #37 Is colors works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.colors()


def test_counter(get_webdriver):
    """ #38 Is counter works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.counter()


def test_gallery_image_change(get_webdriver):
    """ #39 Is gallery image change works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.gallery_image_change()


def test_categories(get_webdriver):
    """ #40 Is categories link works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    page.categories()
    assert page.get_current_url()[:48] != 'https://aliexpress.ru/item/1005002278446127.html'


def test_feedback(get_webdriver):
    """ #41 Is feedback button works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.feedback()


def test_one_star_review_filter(get_webdriver):
    """ #42 Is star review filter works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.star_review_filter()


def test_my_country_checkbox(get_webdriver):
    """ #43 Is my country checkbox works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.my_country_checkbox()


def test_pagination(get_webdriver):
    """ #44 Is pagination links works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    assert page.pagination()


def test_suggestions(get_webdriver):
    """ #45 Is suggestions link works fine. """
    page = ItemPage(get_webdriver)
    page.wait_page_loaded()
    page.suggestions()
    assert page.get_current_url()[:48] != 'https://aliexpress.ru/item/1005002278446127.html'
