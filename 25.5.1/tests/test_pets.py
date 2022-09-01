import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestDriver:
    def test_cards(self):
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_id('email').send_keys('vasya@mail.com')
        self.driver.find_element_by_id('pass').send_keys('12345')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()

        images = self.driver.find_elements_by_css_selector('.card-img-top')
        names = self.driver.find_elements_by_css_selector('.card-title')
        descriptions = self.driver.find_elements_by_css_selector('.card-text')

        for i in range(len(names)):
            assert images[i].get_attribute('src') != '1234'
            assert names[i].text != '1234'
            assert descriptions[i].text != '1234'
            assert ', ' in descriptions[i].text
            parts = descriptions[i].text.split(", ")
            # assert len(parts[0]) > 0
            assert len(parts[1]) > 0
        pass

    def test_table(self):
        self.driver.find_element_by_id('email').send_keys('vasya@mail.com')
        self.driver.find_element_by_id('pass').send_keys('12345')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()

        self.driver.get("https://petfriends.skillfactory.ru/my_pets")

        name = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   ".\.col-sm-4 > h2:nth-child(1)")))
        assert name.text == 'Vasya'

        button = WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     ".btn-outline-success")))
        assert button.text == 'Добавить питомца'
        pass
