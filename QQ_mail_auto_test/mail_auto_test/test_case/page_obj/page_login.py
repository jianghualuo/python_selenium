from .Page import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageLogin(PageBase):
    """
    定义qq邮箱页面登录模型
    """

    url = '/'
    # 定位器
    username_loc = (By.ID, "u")
    password_loc = (By.ID, "p")
    submit_loc = (By.ID, "login_button")
    auto_login_loc = (By.ID, "p_low_login_enable")

    # actions
    def type_username(self, username):
        # PageLogin(PageBase).find_element(*self.username_loc).clear() 如此写没有传入参数“driver”
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 统一的登录测试方法,默认用户名和密码
    def test_login(self, username="1414710823@qq.com", password="LJH-ljh@169914@"):
        self.open()
        self.driver.switch_to.frame("login_frame")

        self.type_username(username)
        self.type_password(password)
        self.type_submit()
        sleep(1)

    def auto_login(self, username="1414710823@qq.com", password="LJH-ljh@169914@"):
        self.open()
        self.driver.switch_to.frame("login_frame")

        self.type_username(username)
        self.type_password(password)
        self.find_element(*self.auto_login_loc).click()
        self.type_submit()
        sleep(1)

    def test_auto_login(self):
        self.open()

    login_error_loc = (By.ID, "err_m")
    login_success_loc = (By.ID, "useraddr")

    # 正确的用户名和密码登录成功：text = "1414710823@qq.com"
    def login_success_hint(self):
        return self.find_element(*self.login_success_loc).text

    # 空密码登录：text = "你还没有输入密码"
    # 空用户名和密码登录：text = "你还没有输入账号"
    # 错误的密码登录：text = "你输入的账号或密码不正确,请重新输入"
    def login_error(self):
        return self.find_element(*self.login_error_loc).text

    # 判断元素是否可见
    def is_displayed(self, *loc):
        return self.find_element(*loc).is_displayed()
