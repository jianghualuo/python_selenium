import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from models.function import get_screenshot
from selenium.webdriver.common.by import By
from time import sleep


class TestQrLogin(MyTest):
    """测试扫码快捷登录"""

    def test_qr_is_dispalyed(self):
        """测试二维码存在"""
        pass

    def test_qr_failure(self):
        """测试二维码是否会失效"""
        pass

    def test_qr_info_link(self):
        """测试手机QQ链接地址跳转是否正确"""
        pass
