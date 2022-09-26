from pages.base import WebPage
from pages.elements import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

whoops_xpath = '//div/div/p'
cookie_bar_close_btn_xpath = "//div[contains(@class, 'MainLayout')]/div/p/*[name()='svg']"

container_xpath = "//div[contains(@class, 'ProductSnippet__container')][last()]"
add_to_cart_button_xpath = "//div[contains(@class, 'Tooltip__wrapper')][2]/button[1]"
go_to_cart_xpath = "//div[contains(@class, 'CartPopupHeader')]/a"
# cart_positions_xpath = "//div[contains(@class, 'SnowShoppingcartProductList_Product')]/div[contains(@class, 'item')]"
cart_positions_xpath = "//div[contains(@class, 'productContainer')]"
# check_all_check_box_xpath = "//label[contains(@class, 'Checkbox')]"
check_all_check_box_xpath = "//div[contains(@class, 'listHeader')]/div/label[contains(@class, 'Checkbox')]"
sum_label_xpath = "//h4[contains(@class, 'OrderTotal')][2]"
incremental_button_xpath = "//button[contains(@class, 'NumActionGroup')][2]"
butterfly_loader_xpath = "//div[contains(@class, 'ButterflyLoader')]"
delete_button_xpath = "//button[contains(@class, 'ControlActionGroup')][2]"
ok_button_xpath = "//div[contains(@class, 'btnBlock')]/button[1]"
purchase_button_xpath = "//button[contains(text(), 'Купить')]"
modal_popup_xpath = "//div[contains(@class, '_ModalPopup__popup')]"

shopcart_button_xpath = "//a[contains(@class, 'Header_ShopCart__linkImage')]"


class ShopcartPage(WebPage):

    def __init__(self, web_driver, url=''):
        if url == '':
            url = 'https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail.htm'
        super().__init__(web_driver, url)

    whoops_label = WebElement(xpath='//div/h1')
    whoops_label2 = WebElement(xpath=whoops_xpath)

    def close_cookie_bar_click(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        return self._web_driver.find_elements(By.XPATH, cookie_bar_close_btn_xpath)

    def add_random_stuff_to_cart(self):
        main_window_handle = self._web_driver.current_window_handle
        self._web_driver.get('https://aliexpress.ru/category/202002105/other-kitchen-tools-gadgets.html')
        self._web_driver.find_element(By.XPATH, container_xpath).click()
        WebDriverWait(self._web_driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self._web_driver.window_handles:
            if window_handle != main_window_handle:
                self._web_driver.switch_to.window(window_handle)
                break
        self.wait_page_loaded()
        self.close_cookie_bar_click()
        self._web_driver.find_element(By.XPATH, add_to_cart_button_xpath).click()
        self.wait_page_loaded()
        self._web_driver.find_element(By.XPATH, go_to_cart_xpath).click()

    def cart_positions_count(self):
        elements = WebDriverWait(self._web_driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, cart_positions_xpath))
            )
        return len(elements)

    def calculate_shopcart(self):
        self.wait_page_loaded()
        self._web_driver.find_element(By.XPATH, check_all_check_box_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, butterfly_loader_xpath))
            )
        return self._web_driver.find_element(By.XPATH, sum_label_xpath).text

    def increment_item(self):
        _sum = self.calculate_shopcart()
        time.sleep(1)
        self._web_driver.find_element(By.XPATH, incremental_button_xpath).click()
        time.sleep(1)
        self.wait_page_loaded()
        return self._web_driver.find_element(By.XPATH, sum_label_xpath).text != _sum

    def delete_item(self):
        self.wait_page_loaded()
        self._web_driver.find_element(By.XPATH, delete_button_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, ok_button_xpath))
            )
        self._web_driver.find_element(By.XPATH, ok_button_xpath).click()
        self.wait_page_loaded()
        elements = self._web_driver.find_element(By.XPATH, whoops_xpath)
        if elements:
            whoops2 = self._web_driver.find_element(By.XPATH, whoops_xpath).text
        else:
            whoops2 = ''
        return whoops2

    def purchase(self):
        self.calculate_shopcart()
        self.wait_page_loaded()
        self._web_driver.find_element(By.XPATH, purchase_button_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, modal_popup_xpath))
            )
        return len(elements)

    def oper_shopcart(self):
        self._web_driver.find_element(By.XPATH, shopcart_button_xpath).click()
        self.wait_page_loaded()
