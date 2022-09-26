from pages.base import WebPage
from selenium.webdriver.common.by import By

email_id = 'email'
password_id = 'password'
login_btn_xpath = '//form/button'
bad_pass_message_xpath = '//form/div[3]/span'
bad_login_message_xpath = '//form/div[2]/span'


class AuthPage(WebPage):
    def __init__(self, web_driver):
        url = 'https://login.aliexpress.ru/'
        super().__init__(web_driver, url)

    def set_email(self, email):
        self._web_driver.find_element(By.ID, email_id).send_keys(email)

    def set_pass(self, password):
        self._web_driver.find_element(By.ID, password_id).send_keys(password)

    def login_click(self):
        self._web_driver.find_element(By.XPATH, login_btn_xpath).click()

    def check_invalid_password_message(self):
        message = self._web_driver.find_element(By.XPATH, bad_pass_message_xpath).text
        return message

    def check_invalid_login_message(self):
        message = self._web_driver.find_element(By.XPATH, bad_login_message_xpath).text
        return message
