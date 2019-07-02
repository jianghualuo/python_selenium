# 浏览器驱动、测试URL、打开测试页面、断言打开的页面是否正确、页面元素定位方法
from selenium import webdriver


class PageBase(object):
    """
    定义所有页面基础类
    """
    base_url = 'https://mail.qq.com'

    # 定义初始化参数：浏览器驱动，基础url、超时时间
    def __init__(self, selenium_driver, base_url=base_url):
        self.driver = selenium_driver
        self.base_url = base_url
        self.timeout = 30

    # 判断当前登录页面是否和预期页面URL一致
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    # 打开测试页面
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert(self.on_page()), "没有登录到%s" % url

    def open(self):
        self._open(self.url)

    # 定位界面单个元素
    def find_element(self, *loc):
        return self.driver.find_element()

    # 定位页面多个元素
    def find_elements(self, *loc):
        return self.driver.find_elements()
