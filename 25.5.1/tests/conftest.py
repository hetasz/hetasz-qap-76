import pytest
from selenium import webdriver
import selenium.webdriver.firefox.options


@pytest.fixture
def get_firefox_options():
    options = selenium.webdriver.firefox.options.Options()
    # options.binary_location = 'C:\geckodriver.exe'
    options.add_argument('-foreground')
    options.set_preference('browser.anchor_color', '#FF0000')
    return options


@pytest.fixture
def get_webdriver(get_firefox_options):
    options = get_firefox_options
    driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe', options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'http://petfriends.skillfactory.ru/login'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
