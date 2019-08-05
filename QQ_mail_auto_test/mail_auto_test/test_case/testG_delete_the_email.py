import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_receive_email import ReceiveEmail
from models.myunit import MyTest
from models.function import get_screenshot
from time import sleep


class TestDeleteTheEmail(MyTest):
    """收件箱，信件删除测试"""

    def test1_single_delete(self):
        """随机勾选一个信件进行删除"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 随机勾选一个邮件
        self.driver.switch_to.frame("mainFrame")
        ree.single_check(0)
        # 删除勾选的邮件
        ree.del_email()
        sleep(2)
        # 删除会出现提示
        self.driver.switch_to.default_content()
        assert (ree.get_message_box() == "删除成功 [撤销]"), "未删除成功"

    def test2_batch_del(self):
        """随机批量删除"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 随机批量勾选:暂定三个
        self.driver.switch_to.frame("mainFrame")
        ree.check_multi(0)
        # 删除勾选的邮件
        ree.del_email()
        sleep(2)
        # 删除会出现提示
        self.driver.switch_to.default_content()
        assert (ree.get_message_box() == "删除成功 [撤销]"), "未删除成功"

    def test3_del_by_sender(self):
        """按发件人姓名勾选删除"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 按发件人姓名勾选
        self.driver.switch_to.frame("mainFrame")
        ree.check_by_sender("罗江华", 0)
        # 删除勾选的邮件
        ree.del_email()
        sleep(1)
        # 删除会出现提示
        self.driver.switch_to.default_content()
        assert(ree.get_message_box() == "删除成功 [撤销]"), "未删除成功"

    def test4_del_all(self):
        """全部勾选删除"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 全部勾选
        self.driver.switch_to.frame("mainFrame")
        ree.all_check()
        # 删除勾选的邮件
        ree.del_email()
        sleep(1)
        # 删除会出现提示
        self.driver.switch_to.default_content()
        assert (ree.get_message_box() == "删除成功 [撤销]"), "未删除成功"


if __name__ == '__main__':
    unittest.main()
