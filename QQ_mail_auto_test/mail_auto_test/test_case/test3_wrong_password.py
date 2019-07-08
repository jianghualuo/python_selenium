import unittest
from time import sleep
import random
import sys
sys.path.append("./modles")
sys.path.append("./page_obj")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from models.function import get_screenshot

class TestWrongPassword(MyTest):
    """登录测试"""

    num = str(random.randint(0, 199))

    def test_wrong_password(self):
        """错误密码登录测试"""

        pl = PageLogin(self.driver)
        pl.test_login(self.num + "1414710823@qq.com", self.num*3)
        sleep(3)
        get_screenshot(self.driver, "./mail_auto_test/report/img/wrong_password_login.jpg")
        self.assertEqual(pl.login_error(), "你输入的帐号或密码不正确，请重新输入。")


if __name__ == '__main__':
    unittest.main()

