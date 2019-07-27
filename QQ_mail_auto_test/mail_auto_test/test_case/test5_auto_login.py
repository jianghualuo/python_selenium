import sys
import unittest
import pyautogui
from time import sleep
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from models.myunit import MyTest
from selenium.webdriver.common.by import By
from models.function import open_mail_web, get_screenshot


class TestAutoLogin(MyTest):
    """测试“下次自动登录”功能"""

    text = '1414710823@qq.com'

    def test1_auto_login_next(self):
        """勾选【下次自动登录】登录测试"""
        pl = PageLogin(self.driver)
        pl.auto_login()
        sleep(3)
        self.driver.switch_to.default_content()
        assert(self.text == pl.login_success_hint()), '登录失败!'

    def test2_logout(self):
        """退出登录后，再次打开QQ邮箱登录页面是否自动登录"""
        pl = PageLogin(self.driver)
        pl.auto_login()
        # 切换到最外层页面，然后点击退出按钮
        self.driver.switch_to.default_content()
        pl.find_element(By.LINK_TEXT, "退出").click()
        sleep(2)
        # 使用os和pyautogui模块打开QQ邮箱登录网页，并截屏留做验证
        open_mail_web()

    # TODO:关于验证下次自动登录的问题，目前使用的该方法不可行，尝试使用多线程是否可以成功
    # 发现通富哦webdriver打开的网页是脚本和浏览器之间的通信，关闭网页后cookie等将不会保存
    @unittest.skip("问题未解决")
    def test3_next_auto_login(self):
        # 登录邮箱并勾选“下次自动登录”
        pl = PageLogin(self.driver)
        pl.auto_login()
        sleep(3)
        # 用pyautogui关闭浏览器，不给teardown清除环境的机会
        # 然后再次使用pyautogui打开网页去验证
        pyautogui.click(1893, 11)
        open_mail_web()


if __name__ == '__main__':
    unittest.main()

