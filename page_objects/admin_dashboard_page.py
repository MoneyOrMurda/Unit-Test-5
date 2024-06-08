from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class AdminDashboardPage(BasePage):
    CATALOG_MENU = (By.ID, 'menu-catalog')
    CATEGORIES_LINK = (By.LINK_TEXT, 'Categories')

    def go_to_categories(self):
        self.find_element(self.CATALOG_MENU).click()
        self.find_element(self.CATEGORIES_LINK).click()
