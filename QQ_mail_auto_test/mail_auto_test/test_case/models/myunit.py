from selenium import webdriver
import unittest
from .driver import browser


class MyTest(unittest.TestCase):
    """
    unit测试框架
    """
    # 如下错误做法：在unittest的setUp初始化函数外定义驱动，导致第一个测试用例执行完毕环境被清除，之后没有再次定义驱动。
    # driver = webdriver.Firefox()  # 错误1：
    # driver = browser()            # 错误2：

    def setUp(self):
        # self.driver = browser()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        # quit：退出驱动并关闭所有关联的窗口
        self.driver.quit()
