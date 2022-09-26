from pages.base import WebPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


load_overlay_xpath = "//div[contains(@class, 'loadOverlay')]"
prices_xpath = "//div[contains(@class, 'snow-price_SnowPrice__container')]"

breadcrumb_xpath = "//li[contains(@class, 'breadcrumb')][1]"
category_xpath = "//ul[contains(@class, 'SearchCategories__pathList')]/li[1]"
price_low_edit_xpath = "//input[contains(@class, 'PriceRangeInput__input')][1]"
price_low_set_button_xpath = "//button[contains(@class, 'PriceRangeInput__button')]"
central_range_xpath = "//ul[contains(@class, 'priceRanges')]/div[3]"
free_delivery_checkbox_xpath = "//div[contains(@class, 'SearchMainFilters_FeaturesFilter__tag')][1]/label/span[1]"
stars_filter_checkbox_xpath = "//div[contains(@class, 'SearchMainFilters_FeaturesFilter__tag')][2]/label/span[1]"
sort_by_order_xpath = "//div[contains(@class, 'SearchMainFilters_SearchMainFilters__sortContainer')]/div/div/button[2]"
list_view_xpath = "//div[contains(@class, 'SearchMainFilters_SearchMainFilters__sortContainer')]/span/*[@id='iconlist']"
pagination_xpath = "//div[contains(@class, 'pagination')]/a[3]"
pagination_input_xpath = "//div[contains(@class, 'pagination')]/form/input"
pagination_button_xpath = "//div[contains(@class, 'pagination')]/form/button"


class FilterPage(WebPage):

    def __init__(self, web_driver, url=''):
        if url == '':
            url = 'https://aliexpress.ru/category/202040662/camera-drones.html'
        super().__init__(web_driver, url)

    def breadcrumb(self):
        self._web_driver.find_element(By.XPATH, breadcrumb_xpath).click()

    def category(self):
        self._web_driver.find_element(By.XPATH, category_xpath).click()

    def price_low(self):
        self._web_driver.find_element(By.XPATH, price_low_edit_xpath).send_keys('10000')
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, price_low_set_button_xpath))
        )
        self._web_driver.find_element(By.XPATH, price_low_set_button_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        if elements:
            whoops2 = self._web_driver.find_element(By.XPATH, prices_xpath).text
        else:
            whoops2 = ''
        return whoops2[:9].strip(' ,') > '1000000'

    def ranges(self):
        self._web_driver.find_element(By.XPATH, central_range_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        if elements:
            whoops2 = self._web_driver.find_element(By.XPATH, prices_xpath).text
        else:
            whoops2 = ''
        return whoops2[:9].strip(' ,') > '100000'

    def free_delivery(self):
        self._web_driver.find_element(By.XPATH, free_delivery_checkbox_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        url = self.get_current_url()
        return 'isFreeShip=y' in url

    def stars_filter(self):
        self._web_driver.find_element(By.XPATH, stars_filter_checkbox_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        url = self.get_current_url()
        return 'isFavorite=y' in url

    def sort_by_order(self):
        self._web_driver.find_element(By.XPATH, sort_by_order_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        url = self.get_current_url()
        return 'SortType=total_tranpro_desc' in url

    def list_view(self):
        self._web_driver.find_element(By.XPATH, list_view_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        url = self.get_current_url()
        return 'g=n' in url

    def pagination(self):
        self._web_driver.find_element(By.XPATH, pagination_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        url = self.get_current_url()
        return 'page=2' in url

    def pagination_jump(self, _page):
        self._web_driver.find_element(By.XPATH, pagination_input_xpath).send_keys(_page)
        self._web_driver.find_element(By.XPATH, pagination_button_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, prices_xpath))
        )
        url = self.get_current_url()
        return 'page=' in url
