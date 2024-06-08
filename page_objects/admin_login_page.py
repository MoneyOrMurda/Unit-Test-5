from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def login(self, username, password):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()
