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

    # actions
    def type_username(self, username):
        PageLogin(PageBase).find_element(*self.username_loc).clear()
        PageLogin(PageBase).find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        PageLogin(PageBase).find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        PageLogin(PageBase).find_element(*self.submit_loc).clck()

    # 统一的登录测试方法,默认用户名和密码
    def test_login(self, username="1414710823@qq.com", password="LJH-ljh@169914@"):
        self.open()
        self.driver.switch_to.frame()

        self.type_username(username)
        self.type_password(password)
        self.type_submit()
        sleep(1)

        self.driver.switch_to.default_content()

    login_error_loc = (By.ID, "err_m")
    login_success_loc = (By.ID, "useraddr")

    # 正确的用户名和密码登录成功：text = "1414710823@qq.com"
    def login_success_hint(self):
        return self.find_element(*self.login_success_loc).text

    # 空用户名和密码登录：text = "你还没有输入密码"
    def login_null_(self):
        return self.find_element(*self.login_error_loc).text

    # 空密码登录：text = "你还有输入账号"
    def login_no_password(self):
        return self.find_element(*self.login_error_loc).text

    # 错误的密码登录：text = "你输入的账号和密码不正确"
    def login_wrong_password(self):
        return self.find_element(*self.login_error_loc).text
