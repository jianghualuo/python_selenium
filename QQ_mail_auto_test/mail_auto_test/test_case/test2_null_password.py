import unittest
import random
from time import sleep
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.page_login import PageLogin


class TestNullPassword(MyTest):
    """登录测试"""

    text = "你还没有输入密码！"
    num = str(random.randint(0, 199))

    def test_null_password(self):
        """测试空密码登录"""
        pl = PageLogin(self.driver)
        pl.test_login(self.num + "1414710823@qq.com", "")
        sleep(3)
        assert(self.text == pl.login_error()), "你还没有输入密码!"


if __name__ == '__main__':
    unittest.main()
