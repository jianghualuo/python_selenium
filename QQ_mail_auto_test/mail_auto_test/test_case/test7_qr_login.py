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

    def test1_qr_is_dispalyed(self):
        """测试二维码存在"""

        # 切换到扫码快捷登录
        self.driver.get("https://mail.qq.com/")
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_id("switcher_qlogin").click()
        sleep(1)

        result = self.driver.find_element_by_id("qrlogin_img").is_displayed()
        assert(result is True), "二维码不存在"
        get_screenshot(self.driver, "./mail_auto_test/report/img/qrlogin_img.jpg")

    # @unittest.skipUnless(result, "二维码不存在，跳过该测试项")
    def test2_qr_failure(self):
        """测试二维码（有效时间为125s）是否会失效"""

        # 切换到扫码快捷登录
        self.driver.get("https://mail.qq.com/")
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_id("switcher_qlogin").click()
        sleep(1)

        # sleep 125s 验证二维是否给出失效提示
        sleep(126)
        result = self.driver.find_element_by_id("qr_invalid_tips").is_displayed()
        assert(result is True), "没有二维码失效提示"
        get_screenshot(self.driver, "./mail_auto_test/report/img/qr_invalid_tips.jpg")

    def test3_qr_info_link(self):
        """测试手机QQ链接地址跳转是否正确"""

        # 切换到扫码快捷登录
        self.driver.get("https://mail.qq.com/")
        # 获取当前窗口句柄
        handle_login = self.driver.current_window_handle
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_id("switcher_qlogin").click()
        sleep(1)

        # 点击链接跳转页面，并sleep等待新窗口出现获取当前所有的窗口句柄
        self.driver.find_element_by_link_text("使用QQ手机版扫描登录").click()
        sleep(3)
        handles = self.driver.window_handles

        # 根据窗口句柄，切换到新窗口并验证跳转的界面是否正确
        for handle in handles:
            if handle != handle_login:
                self.driver.switch_to_window(handle)
                assert(self.driver.title == "I'm QQ - 每一天，乐在沟通")
                get_screenshot(self.driver, "./mail_auto_test/report/img/mobile_qq.jpg")


if __name__ == '__main__':
    unittest.main()
