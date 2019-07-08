import sys
import unittest
from time import sleep
from selenium.webdriver.common.by import By
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from models.function import get_screenshot


class TestAutoLogin(MyTest):
    """测试“下次自动登录”功能"""

    text = '1414710823@qq.com'

    def test0_login_ok(self):
        """正确的用户名和密码登录测试"""
        pl = PageLogin(self.driver)
        pl.test_login()
        self.driver.switch_to.default_content()
        sleep(3)
        assert(self.text == pl.login_success_hint()), '登录失败!'
        print(self.driver.get_cookies())

    def test1_auto_login_next(self):
        """勾选【下次自动登录】登录测试"""
        pl = PageLogin(self.driver)
        pl.auto_login()
        sleep(3)
        self.driver.switch_to.default_content()
        assert(self.text == pl.login_success_hint()), '登录失败!'
        print(self.driver.get_cookies())

    # def test1_auto_login(self):
    #     """验证启用“下次自动登录”是否生效"""
    #     try:
    #         global pl
    #         pl = PageLogin(self.driver)
    #         pl.test_auto_login()
    #     except:
    #         assert (self.text == pl.login_success_hint()), '登录失败!'
    #         get_screenshot("./mail_auto_test/report/img/auto_login_ok.jpg")
    #     finally:
    #         logout_loc = (By.LINK_TEXT, "退出")
    #         pl.find_element(*logout_loc).click()
    #         sleep(1)
    #         get_screenshot("./mail_auto_test/report/img/logout.jpg")
    #
    # def test_logout(self):
    #     """退出登录后测试自动登录是否生效"""
    #     pl = PageLogin(self.driver)
    #     pl.test_auto_login()


if __name__ == '__main__':
    unittest.main()

