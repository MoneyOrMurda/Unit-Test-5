import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class TestRunner:
    def __init__(self):
        self.test_suite = unittest.TestSuite()

    def add_tests(self, tests):
        for test in tests:
            self.test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))

    def run_tests(self, browser='chrome'):
        if browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError("Unsupported browser!")

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(self.test_suite)
        driver.quit()

if __name__ == '__main__':
    from tests.test_create_category import CreateCategoryTest
    from tests.test_add_products import AddProductsTest
    from tests.test_verify_products import VerifyProductsTest
    from tests.test_delete_products import DeleteProductsTest
    from tests.test_verify_remaining_products import VerifyRemainingProductsTest

    runner = TestRunner()
    runner.add_tests([
        CreateCategoryTest,
        AddProductsTest,
        VerifyProductsTest,
        DeleteProductsTest,
        VerifyRemainingProductsTest
    ])
    
    # Запуск тестов в Chrome
    runner.run_tests(browser='chrome')

    # Запуск тестов в Firefox
    runner.run_tests(browser='firefox')
