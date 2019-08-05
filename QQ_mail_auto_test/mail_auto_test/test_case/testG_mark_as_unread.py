import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_receive_email import ReceiveEmail
from models.myunit import MyTest
from models.function import get_screenshot
from time import sleep


class TestMark(MyTest):
    """测试标记功能"""

    def test1_mark_as_unread(self):
        """测试随机单个已读标记为未读"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 随机勾选一个邮件
        self.driver.switch_to.frame("mainFrame")
        ree.single_check(0)
        # 标记为未读
        ree.mark_as_read()
        sleep(2)
        # 未读邮件统计
        assert(self.driver.find_element_by_id("_ur_c").text == "1"), "标记未读失败"

    def test2_mark_as_unread(self):
        """测试随机批量已读标记为未读"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 随机批量勾选:暂定三个
        self.driver.switch_to.frame("mainFrame")
        ree.check_multi(0)
        # 标记为未读
        ree.mark_as_unread()
        sleep(2)
        # 未读邮件统计
        assert(self.driver.find_element_by_id("_ur_c").text == "4"), "标记未读失败"

    def test3_mark_as_unread(self):
        """按发件人姓名标记为未读"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 按发件人姓名勾选
        self.driver.switch_to.frame("mainFrame")
        ree.check_by_sender("18827453452", 0)
        # 标记为未读
        ree.mark_as_unread()
        sleep(2)
        # 未读邮件统计
        assert(self.driver.find_element_by_id("_ur_c").text > "4"), "标记未读失败"

    def test4_mark_as_unread(self):
        """测试页面全部已读标记为未读"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 勾选全部已读
        self.driver.switch_to.frame("mainFrame")
        ree.check_mode(2)
        # 标记为未读
        ree.mark_as_unread()
        sleep(2)
        # 未读邮件统计
        assert(self.driver.find_element_by_id("_ur_c").text == "25"), "标记未读失败"


if __name__ == '__main__':
    unittest.main()
