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


class TestQuickLogin(MyTest):
    """测试PC端登录QQ后，邮箱网页的快捷登录功能"""

    def test1_img_nick_is_displayed(self):
        """检测登录控件是否会有快捷登录的相关信息并且显示是否正确"""
        qq_login()

        self.driver.get("https://mail.qq.com/")
        sleep(3)
        self.driver.switch_to.frame("login_frame")
        result_1 = self.driver.find_element_by_id("img_out_1414710823").is_displayed()
        result_2 = self.driver.find_element_by_id("nick_1414710823").is_displayed()
        if result_1 and result_2:
            # qq昵称显示是否正确
            text = self.driver.find_element_by_id("nick_1414710823").text
            self.assertEqual(text, "老④")
            # 截图查看快捷登录按钮的图片以及鼠标悬浮显示的账号是否有异常
            loc = (By.ID, "img_out_1414710823")
            mouseover(self.driver, *loc)
            get_screenshot(self.driver, "./mail_auto_test/report/img/quick_login.jpg")

    def test2_quick_login(self):
        """点击快捷登录控件的QQ头像是否能登陆成功"""
        self.driver.get("https://mail.qq.com/")
        sleep(3)
        self.driver.switch_to.frame("login_frame")
        result = self.driver.find_element_by_id("img_out_1414710823").is_displayed()
        if result:
            self.driver.find_element_by_id("img_out_1414710823").click()
            self.driver.switch_to.default_content()
            sleep(5)
            assert("1414710823@qq.com" == PageLogin(self.driver).login_success_hint()), "点击头像，快捷登录失败"
        else:
            raise ElementNotPresent("定位的元素不存在")

    def test3_quick_login(self):
        """点击快捷登录控件的QQ昵称是否能登陆成功"""
        self.driver.get("https://mail.qq.com/")
        sleep(3)
        self.driver.switch_to.frame("login_frame")
        # 检测元素是否存在，不存在则
        result = self.driver.find_element_by_id("nick_1414710823").is_displayed()
        if result:
            self.driver.find_element_by_id("nick_1414710823").click()
            self.driver.switch_to.default_content()
            sleep(5)
            PageLogin(self.driver)
            assert("1414710823@qq.com" == PageLogin(self.driver).login_success_hint()), "点击昵称，快捷登录失败"
        else:
            raise ElementNotPresent("定位的元素不存在")


if __name__ == '__main__':
    unittest.main()
