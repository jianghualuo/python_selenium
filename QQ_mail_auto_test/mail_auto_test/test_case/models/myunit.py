from selenium import webdriver
import unittest


class MyTest(unittest.TestCase):
    """
    unit测试框架
    """

    driver = webdriver.Firefox()

    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
