import sys
import unittest
from time import sleep
# 错误观点：从其他包导入模块时，目标包相对当前目录路径有几层，需要在导入的包前面加几个“.”，表示层级关系
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from models.function import get_screenshot


class TestLoginOk(MyTest):
    """登录测试"""

    text = '1414710823@qq.com'

    def test_login_ok(self):
        """正确的用户名和密码登录测试"""
        pl = PageLogin(self.driver)
        pl.test_login()
        self.driver.switch_to.default_content()
        sleep(3)
        get_screenshot(self.driver, "./mail_auto_test/report/img/login_ok.jpg")
        assert(self.text == pl.login_success_hint()), '登录失败!'


if __name__ == '__main__':
    unittest.main()
