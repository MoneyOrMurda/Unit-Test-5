import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_dashboard_page import AdminDashboardPage
from page_objects.admin_category_page import AdminCategoryPage

class AddProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_dashboard_page = AdminDashboardPage(self.driver)
        self.admin_category_page = AdminCategoryPage(self.driver)
        self.admin_login_page.go_to_site()
        self.admin_login_page.login('admin', 'password')

    def test_add_products(self):
        self.admin_dashboard_page.go_to_categories()
        self.admin_category_page.add_new_category('Mouse 1', 'Mouse 1 Meta Tag')
        self.admin_category_page.add_new_category('Mouse 2', 'Mouse 2 Meta Tag')
        self.admin_category_page.add_new_category('Keyboard 1', 'Keyboard 1 Meta Tag')
        self.admin_category_page.add_new_category('Keyboard 2', 'Keyboard 2 Meta Tag')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
