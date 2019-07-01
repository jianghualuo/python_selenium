from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """
    定义基础类
    """

    base_url = "https://mail.qq.com"

    def __init__(self, selenium_driver, base_url=base_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), "Dod NOT LAND ON %S" % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class PageLogin(Page):
    """
    定义登录页面对象模型
    """

    url = '/'

    username_loc = (By.ID, "u")
    password_loc = (By.ID, "p")
    submit_loc = (By.ID, "login_button")

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    pl = PageLogin(driver)
    pl.open()
    driver.implicitly_wait(10)
    driver.switch_to.frame("login_frame")
    driver.find_element_by_id("switcher_plogin").click()
    pl.type_username(username)
    pl.type_password(password)
    pl.type_submit()
    driver.switch_to.default_content()


def main():
    try:
        global driver
        driver = webdriver.Firefox()
        username = "1414710823@qq.com"
        password = "LJH-ljh@169914@"
        test_user_login(driver, username, password)
        sleep(5)
        text = driver.find_element_by_id("useraddr").text
        assert (text == "1414710823@qq.com"), "用户名称不匹配，登录失败！"
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
