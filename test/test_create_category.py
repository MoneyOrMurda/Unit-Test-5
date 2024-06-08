import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_dashboard_page import AdminDashboardPage
from page_objects.admin_category_page import AdminCategoryPage

class CreateCategoryTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.admin_login_page = AdminLoginPage(self.driver)
        self.admin_dashboard_page = AdminDashboardPage(self.driver)
        self.admin_category_page = AdminCategoryPage(self.driver)
        self.admin_login_page.go_to_site()
        self.admin_login_page.login('admin', 'password')

    def test_create_category(self):
        self.admin_dashboard_page.go_to_categories()
        self.admin_category_page.add_new_category('Devices', 'Devices Meta Tag')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
