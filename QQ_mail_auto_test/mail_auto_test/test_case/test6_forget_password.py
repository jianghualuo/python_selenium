import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from models.function import get_screenshot
from selenium.webdriver.common.by import By
from time import sleep


class TestForgetPassword(MyTest):
    """测试登录界面“忘了密码”功能"""

    def test_forget_password(self):
        """测试点击“忘了密码”后页面跳转是否正确"""
        # 打开登录页面，并获取窗口句柄:handle1
        self.driver.get("https://mail.qq.com/")
        handle1 = self.driver.current_window_handle

        # 打开忘记密码窗口，并获取所有窗口的句柄handles
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_id('forgetpwd').click()
        sleep(3)  # 这个地方必须加睡眠时间，给新窗口打开预留时间，不然马上执行下面的代码结束测试
        handles = self.driver.window_handles

        # 筛选窗口句柄切换到忘记密码窗口，并判断页面是否正确
        for handle in handles:
            if handle != handle1:
                self.driver.switch_to_window(handle)
                text = self.driver.title
                assert(text == "重置密码 - QQ安全中心")
                sleep(1)
                get_screenshot(self.driver, "./mail_auto_test/report/img/forget_password.jpg")


if __name__ == '__main__':
    unittest.main()
