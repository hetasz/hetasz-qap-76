

from pages.auth_page import AuthPage


def test_bad_pass_authorization(get_webdriver):
    """ #01 Is bad pass authorization works fine. """
    page = AuthPage(get_webdriver)
    page.set_email('a@a.ru')
    page.set_pass('a')
    page.login_click()
    page.wait_page_loaded()
    assert page.check_invalid_password_message() == 'Ваши учетное имя или пароль неправильные.'


def test_bad_login_authorization(get_webdriver):
    """ #02 Is bad login authorization works fine. """
    page = AuthPage(get_webdriver)
    page.set_email('a')
    page.set_pass('a')
    page.login_click()
    page.wait_page_loaded()
    assert page.check_invalid_login_message() == 'Почта должна быть формата username@domain.ru'


def test_authorization(get_webdriver):
    """ #03 Is authorization works fine. """
    page = AuthPage(get_webdriver)
    page.set_email('qwerty@yandex.ru')
    page.set_pass('qwerty')
    page.login_click()
    page.wait_page_loaded()
    assert page.get_current_url()[:22] == 'https://aliexpress.ru/'
