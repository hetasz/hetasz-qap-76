from pages.base import WebPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

cookie_bar_close_btn_xpath = "//div[contains(@class, 'MainLayout')]/div/p/*[name()='svg']"

breadcrumb_xpath = "//li[contains(@class, 'BreadCrumbs__li')][1]"
coupons_xpath = "//div[contains(@class, 'coupons')]"
coupons_tooltip_xpath = "//div[contains(@class, 'tooltip-content')]"
sales_leader_xpath = "//div[contains(@class, 'ProductCard__wrapper')]"
color_picker1_xpath = "//div[contains(@class, 'SkuValueBaseItem__item')][1]"
color_picker2_xpath = "//div[contains(@class, 'SkuValueBaseItem__item')][2]"
price_xpath = "//div[@id='#content']/div[contains(@class, 'Price__container')][1]"
counter_xpath = "//div[contains(@class, 'Quantity__picker')]/span[contains(@class, 'counter')]/span"
increase_button_xpath = "//div[contains(@class, 'Quantity__picker')]/button[contains(@class, 'Button__button')][2]"
gallery_main_image_xpath = "//img[contains(@class, 'Product_Gallery__img')]"
gallery_image2_xpath = "//div[contains(@class, 'GalleryBarItem__barItem')][2]"
gallery_image3_xpath = "//div[contains(@class, 'GalleryBarItem__barItem')][3]"
categories_xpath = "(//div[contains(@class, 'StoreCategories_Category__label')])[1]"
feedback_xpath = "//div[contains(@class, 'Tabs__titles')]/div[2]"
feedback_tabs_xpath = "//div[contains(@class, 'ali-kit_Tabs__tabs')]/div[2]"
first_review_xpath = "//div[contains(@class, 'Reviews_Reviews__list')]/div[1]"
one_star_review_filter_xpath = "(//div[contains(@class, 'CustomerReviewItem__customerReviewItem')])[1]/span[2]"
my_country_checkbox_xpath = "(//div[contains(@class, 'ali-kit_Checkbox__inputWrap')])[1]"
second_page_button_xpath = "(//button[contains(@class, 'ali-kit_Pagination__page')])[2]"
first_suggestion_xpath = "//div[contains(@class, 'SimilarSuggestions_Category__wrapper')]/span/a[1]"


class ItemPage(WebPage):

    def __init__(self, web_driver, url=''):
        if url == '':
            url = 'https://aliexpress.ru/item/1005002278446127.html'
        super().__init__(web_driver, url)

    def breadcrumb(self):
        self._web_driver.find_element(By.XPATH, breadcrumb_xpath).click()
        self._wait_page_loaded()

    def coupons(self):
        self._web_driver.find_element(By.XPATH, coupons_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, coupons_tooltip_xpath))
            )
        return len(elements)

    def sales_leader(self):
        self._web_driver.find_element(By.XPATH, sales_leader_xpath).click()
        self._wait_page_loaded()

    def colors(self):
        self._web_driver.find_element(By.XPATH, color_picker1_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, price_xpath))
            )
        first_price = self._web_driver.find_element(By.XPATH, price_xpath).text
        self._web_driver.find_element(By.XPATH, color_picker2_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, price_xpath))
            )
        return first_price != self._web_driver.find_element(By.XPATH, price_xpath).text

    def counter(self):
        self._web_driver.find_element(By.XPATH, increase_button_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, counter_xpath))
            )
        return '2' == self._web_driver.find_element(By.XPATH, counter_xpath).text

    def gallery_image_change(self):
        action = ActionChains(self._web_driver)
        action.move_to_element(self._web_driver.find_element(By.XPATH, gallery_image2_xpath)).perform()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, gallery_main_image_xpath))
            )
        main_image = self._web_driver.find_element(By.XPATH, gallery_main_image_xpath)
        src = main_image.get_attribute("src")
        action.move_to_element(self._web_driver.find_element(By.XPATH, gallery_image3_xpath)).perform()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, gallery_main_image_xpath))
            )
        return src != main_image.get_attribute("src")

    def categories(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, categories_xpath))
            )
        self._web_driver.find_element(By.XPATH, categories_xpath).click()
        self.wait_page_loaded()

    def feedback(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, feedback_xpath))
            )
        self._web_driver.find_element(By.XPATH, feedback_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.visibility_of_any_elements_located((By.XPATH, first_review_xpath))
            )
        return self._web_driver.find_element(By.XPATH, first_review_xpath)

    def star_review_filter(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, first_review_xpath))
        )
        content = elements[0].text
        self._web_driver.find_element(By.XPATH, one_star_review_filter_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
                EC.visibility_of_any_elements_located((By.XPATH, first_review_xpath))
            )
        return elements[0].text != content

    def my_country_checkbox(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, first_review_xpath))
        )
        content = elements[0].text
        self._web_driver.find_element(By.XPATH, my_country_checkbox_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.visibility_of_any_elements_located((By.XPATH, first_review_xpath))
        )
        return elements[0].text != content

    def pagination(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, first_review_xpath))
        )
        content = elements[0].text
        self._web_driver.find_element(By.XPATH, second_page_button_xpath).click()
        elements = WebDriverWait(self._web_driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, first_review_xpath))
        )
        return elements[0].text != content

    def suggestions(self):
        self._web_driver.find_element(By.XPATH, cookie_bar_close_btn_xpath).click()
        WebDriverWait(self._web_driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, first_suggestion_xpath))
            )
        self._web_driver.find_element(By.XPATH, first_suggestion_xpath).click()
        self.wait_page_loaded()
