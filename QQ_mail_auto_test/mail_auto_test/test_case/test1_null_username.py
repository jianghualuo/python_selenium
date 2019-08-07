import unittest
from time import sleep
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.page_login import PageLogin
from models.function import get_screenshot


class TestNullUsername(MyTest):
    """登录测试"""

    def test_null_username(self):
        """测试空户名和正确密码登录"""
        pl = PageLogin(self.driver)
        pl.test_login("", "xxxxxxx")
        sleep(3)
        get_screenshot(self.driver, "./mail_auto_test/report/img/null_username_login2.jpg")
        self.assertEqual(pl.login_error(), "你还没有输入帐号！")


if __name__ == '__main__':
    unittest.main()
