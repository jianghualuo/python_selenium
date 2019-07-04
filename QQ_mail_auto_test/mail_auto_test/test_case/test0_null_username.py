import unittest
from time import sleep
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.page_login import PageLogin


class TestNullUsername(MyTest):
    """登录测试"""

    text = "你还没有输入账号！"

    def test_null_username(self):
        """测试空户名和空密码登录"""
        pl = PageLogin(self.driver)
        pl.test_login("", "")
        sleep(3)
        self.assertEqual(pl.login_error(), "你还没有输入帐号！")


if __name__ == '__main__':
    unittest.main()

