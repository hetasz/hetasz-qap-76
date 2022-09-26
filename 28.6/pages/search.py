from pages.base import WebPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


search_xpath = "//input[contains(@class, 'SearchInput__input')]"
search_button_xpath = "//button[contains(@class, 'SearchSection__searchButton')]"
result_count_xpath = "//span[contains(@class, 'SearchBreadcrumbs__resultsCount')]"
error_message_xpath = "//span[contains(@class, 'SearchWrap_SearchError__wordsWrap')]"
request_xpath = "//h1"
product_xpath = "//div[contains(@class, 'SearchProductFeed__productFeed')]/div/div[contains(@class, " \
                "'product-snippet_ProductSnippet__container')] "


class SearchPage(WebPage):
    def __init__(self, web_driver, url=''):
        if url == '':
            url = 'https://aliexpress.ru/wholesale'
        super().__init__(web_driver, url)

    def search_button(self, search):
        self._web_driver.find_element(By.XPATH, search_xpath).send_keys(search)
        self._web_driver.find_element(By.XPATH, search_button_xpath).click()

    def search_enter(self, search):
        self._web_driver.find_element(By.XPATH, search_xpath).send_keys(search)
        self._web_driver.find_element(By.XPATH, search_xpath).send_keys(Keys.ENTER)
        self.wait_page_loaded()

    def get_request(self):
        return self._web_driver.find_element(By.XPATH, request_xpath).text

    def get_error_message(self):
        return self._web_driver.find_element(By.XPATH, error_message_xpath).text

    def get_result_count(self):
        split = self._web_driver.find_element(By.XPATH, result_count_xpath).text.split()
        return int(split[0].replace('(', ''))

    def get_product_count(self):
        elements = WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, product_xpath))
            )
        return len(elements)
