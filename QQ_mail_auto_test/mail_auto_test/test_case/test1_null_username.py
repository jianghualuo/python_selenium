import unittest
import random
from time import sleep
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.page_login import PageLogin


class TestNullUsername(MyTest):
    """登录测试"""

    text = "你还没有输入账号！"
    num = str(random.randint(10000000, 99999999))

    def test_null_username(self):
        """测试空户名和密码非空登录"""
        pl = PageLogin(self.driver)
        pl.test_login("", self.num)
        sleep(3)
        self.assertEqual(pl.login_error(), "你还没有输入帐号！")


if __name__ == '__main__':
    unittest.main()
