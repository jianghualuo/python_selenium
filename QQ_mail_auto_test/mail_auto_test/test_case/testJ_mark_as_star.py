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

    def test1_mark_as_star(self):
        """测试随机单个邮件标记为星标"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 随机勾选一个邮件
        self.driver.switch_to.frame("mainFrame")
        ree.single_check(0)
        # 标记为星标邮件
        ree.mark_as_star()
        # 验证已标记为星标
        self.driver.switch_to.default_content()
        assert(ree.star_mail_statistics() == "1"), "标记星标邮件失败"

    def test2_mark_as_star(self):
        """测试随机批量邮件标记为星标"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 随机批量勾选:暂定三个
        self.driver.switch_to.frame("mainFrame")
        ree.check_multi(0)
        # 标记为星标邮件
        ree.mark_as_star()
        # 验证已标记为星标
        self.driver.switch_to.default_content()
        assert(ree.star_mail_statistics() >= "3"), "标记星标邮件失败"

    def test3_mark_as_star(self):
        """测试按发件人姓名将邮件标记为星标"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        # 按发件人姓名勾选
        self.driver.switch_to.frame("mainFrame")
        ree.check_by_sender("18827453452", 0)
        # 标记为星标邮件
        ree.mark_as_star()
        # 验证已标记为星标，并对处理提示框：取消创建
        self.driver.switch_to.default_content()
        ree.prompt_confirmation(1)
        assert(ree.star_mail_statistics() >= "7"), "标记星标邮件失败"

    def test4_mark_as_star(self):
        """测试页面全部邮件标记为星标"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进入收件箱,并全选
        ree = ReceiveEmail(self.driver)
        ree.goto_inbox()
        self.driver.switch_to.frame("mainFrame")
        ree.all_check()
        # 标记为星标邮件
        ree.mark_as_star()
        # 验证已标记为星标
        self.driver.switch_to.default_content()
        assert(ree.star_mail_statistics() == "25"), "标记星标邮件失败"


if __name__ == '__main__':
    unittest.main()
