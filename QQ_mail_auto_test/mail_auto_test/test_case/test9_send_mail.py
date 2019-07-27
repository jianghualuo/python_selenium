import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from models.exception import ElementNotPresent
from models.function import get_screenshot,qq_login,mouseover
from selenium.webdriver.common.by import By
from time import sleep


class TestSendMail(MyTest):
    """发送邮件测试"""

    def test1_send_mail(self):
        pl = PageLogin(self.driver)
        pl.quick_login()



if __name__ == '__main__':
    unittest.main()
