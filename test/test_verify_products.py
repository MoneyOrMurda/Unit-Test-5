import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.home_page import HomePage

class VerifyProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.home_page.go_to_site()

    def test_verify_products(self):
        self.home_page.search_for_item('Mouse 1')
        # Add verification code
        self.home_page.search_for_item('Mouse 2')
        # Add verification code
        self.home_page.search_for_item('Keyboard 1')
        # Add verification code
        self.home_page.search_for_item('Keyboard 2')
        # Add verification code

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
