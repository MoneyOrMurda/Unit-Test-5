from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="button"]')

    def search_for_item(self, item_name):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(item_name)
        self.find_element(self.SEARCH_BUTTON).click()
