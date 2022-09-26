from pages.base import WebPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logo_xpath = "//div/a[contains(@class, 'Header_Logo')]"
top_banner_xpath = "//div/a[contains(@class, 'TopBanner')]"
application_xpath = "//div[contains(@class, 'topBarItem')]/div/a[contains(@href, 'download')]"
wrapper_xpath = "//span[contains(@class, 'wrapper')]/div[1]"
seller_xpath = "//span[contains(@class, 'wrapper')]/div[1]/div[2]/ul/li[1]"

cookie_bar_close_btn_xpath = "//div[contains(@class, 'MainLayout')]/p/*[name()='svg']"

menu_xpath = "//ul[contains(@class, 'categoriesList')]/li[1]"
smartphones_menu_xpath = "//ul[contains(@class, 'categoriesList')]/li[1]/div[2]/div/div[1]/div/ul/li[1]/a"
item_box_xpath = "//li[contains(@data-role, 'item-box')]"
show_more_xpath = "//div[contains(@class, 'bottomBlock')]/div"
new_user_xpath = "//div[contains(@class, 'sideBarContainer')]/div[1]/div[1]/a/div"
copyright_xpath = "//div[contains(@class, 'copyright')]/span"
search_edit_xpath = "//input[@name='SearchText']"
search_button_xpath = "//button[contains(@class, 'searchButton')]"

robots_xpath = "//*[contains(text(), 'Googlebot')]"


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if url == '':
            url = 'https://aliexpress.ru/'
        super().__init__(web_driver, url)

    def logo_click(self):
        self._web_driver.find_element(By.XPATH, logo_xpath).click()

    def top_banner_click(self):
        self._web_driver.find_element(By.XPATH, top_banner_xpath).click()

    def application_click(self):
        self._web_driver.find_element(By.XPATH, application_xpath).click()

    def seller_click(self):
        action = ActionChains(self._web_driver)
        action.move_to_element(self._web_driver.find_element(By.XPATH, wrapper_xpath)).perform()
        self._web_driver.find_element(By.XPATH, seller_xpath).click()

    def close_cookie_bar_click(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        return self._web_driver.find_elements(By.XPATH, cookie_bar_close_btn_xpath)

    def smartphones_menu_click(self):
        action = ActionChains(self._web_driver)
        action.move_to_element(self._web_driver.find_element(By.XPATH, menu_xpath)).perform()
        self._web_driver.find_element(By.XPATH, smartphones_menu_xpath).click()

    def count_item_box_elements(self):
        elements = WebDriverWait(self._web_driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, item_box_xpath))
            )
        return len(elements)

    def show_more_click(self):
        self._web_driver.find_element(By.XPATH, show_more_xpath).click()

    def new_user_click(self):
        main_window_handle = self._web_driver.current_window_handle
        self._web_driver.find_element(By.XPATH, new_user_xpath).click()
        WebDriverWait(self._web_driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self._web_driver.window_handles:
            if window_handle != main_window_handle:
                self._web_driver.switch_to.window(window_handle)
                break
        WebDriverWait(self._web_driver, 10).until(EC.title_is("Подарки новичкам"))

    def get_copyright(self):
        return self._web_driver.find_element(By.XPATH, copyright_xpath).text

    def do_search(self, request):
        self._web_driver.find_element(By.XPATH, search_edit_xpath).send_keys(request)
        self._web_driver.find_element(By.XPATH, search_button_xpath).click()

    def get_google_bot(self):
        return self._web_driver.find_element(By.XPATH, robots_xpath).text
