from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """
    基础类，用于页面对象类的继承
    """

    login_url = "https://mail.163.com"

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):  # *loc：解包loc，接受的传参会不止一个
        return self.driver.find_element(*loc)


class LoginPage(Page):
    """
    163邮箱登录页面模型
    """

    url = '/'

    # 定位器，元组模型
    username_loc = (By.NAME, "email")
    password_loc = (By.NAME, "password")
    submit_loc = (By.ID, "dologin")

    # Action
    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    """
    测试获取的用户名和密码是否可以登录
    """
    login_page = LoginPage(driver)
    login_page.open()
    driver.implicitly_wait(10)
    driver.find_element_by_id("lbNormal").click()
    driver.switch_to.frame("")
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    driver.switch_to.default_content()


def main():
    try:
        global driver
        driver = webdriver.Firefox()
        username = '18827453452@163.com'
        password = '51testing'
        test_user_login(driver, username, password)
        text = driver.find_element_by_id("spnUid").text
        assert(text == "188****3452@163.com"), "用户名称不匹配，登录失败！"
    finally:
        # 关闭浏览器窗口
        driver.close()


if __name__ == '__main__':
    main()
