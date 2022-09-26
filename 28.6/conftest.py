
import pytest
# import uuid
from selenium import webdriver
import selenium.webdriver.firefox.options


@pytest.fixture
def get_firefox_options():
    options = selenium.webdriver.firefox.options.Options()
    options.add_argument('-foreground')
    options.set_preference('browser.anchor_color', '#FF0000')
    return options


@pytest.fixture
def get_webdriver(get_firefox_options):
    options = get_firefox_options
    driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe', options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def generate_string(num):
    return "x" * num
