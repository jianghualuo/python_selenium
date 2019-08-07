import unittest
from time import sleep
import random
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.page_login import PageLogin


class TestLogin(MyTest):
    """登录测试"""

    def test1_null_username(self):
        """测试空户名和空密码登录"""
        pl = PageLogin(self.driver)
        pl.test_login("", "")
        sleep(3)
        self.assertEqual(pl.login_error(), "你还没有输入帐号！")

    def test2_null_username(self):
        """测试空户名和密码非空登录"""
        pl = PageLogin(self.driver)
        pl.test_login("", "xxxxxxxxx")
        sleep(3)
        self.assertEqual(pl.login_error(), "你还没有输入帐号！")

    def test3_null_password(self):
        """测试空密码登录"""
        num = str(random.randint(0, 199))
        pl = PageLogin(self.driver)
        pl.test_login(num + "1414710823@qq.com", "")
        sleep(3)
        self.assertEqual(pl.login_error(), "你还没有输入密码！")

    def test4_wrong_password(self):
        """错误密码登录测试"""
        num = str(random.randint(0, 199))
        pl = PageLogin(self.driver)
        pl.test_login(num + "1414710823@qq.com", num*3)
        sleep(3)
        self.assertEqual(pl.login_error(), "你输入的帐号或密码不正确，请重新输入。")

    def test5_login_ok(self):
        """正确的用户名和密码登录测试"""
        text = '1414710823@qq.com'
        pl = PageLogin(self.driver)
        pl.test_login()
        self.driver.switch_to.default_content()
        sleep(3)
        assert(text == pl.login_success_hint()), '登录失败!'


if __name__ == '__main__':
    unittest.main()
