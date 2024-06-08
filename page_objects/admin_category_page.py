from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class AdminCategoryPage(BasePage):
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
    CATEGORY_NAME_INPUT = (By.ID, 'input-name1')
    META_TAG_TITLE_INPUT = (By.ID, 'input-meta-title1')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')
    CHECKBOX = (By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr[td[text()='{}']]/td/input[@type='checkbox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')

    def add_new_category(self, category_name, meta_tag_title):
        self.find_element(self.ADD_NEW_BUTTON).click()
        self.find_element(self.CATEGORY_NAME_INPUT).send_keys(category_name)
        self.find_element(self.META_TAG_TITLE_INPUT).send_keys(meta_tag_title)
        self.find_element(self.SAVE_BUTTON).click()

    def delete_category(self, category_name):
        self.find_element((By.XPATH, self.CHECKBOX.format(category_name))).click()
        self.find_element(self.DELETE_BUTTON).click()
        self.driver.switch_to.alert.accept()
