import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_receive_email import ReceiveEmail
from models.myunit import MyTest
from models.function import get_screenshot
from time import sleep


class TestMoveToSent(MyTest):
    """测试信件移动功能（移动到已发送）"""

    def test1_move_to_sent(self):
        """测试随机勾选单个邮件移动到已发送"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 先进入已发送目录，得到初始的已发送信件数：mail_num1
        ree = ReceiveEmail(self.driver)
        mail_num1 = ree.sent_mail_statistics()
        # 进入收件箱
        ree.goto_inbox()
        # 随机勾选一个邮件
        self.driver.switch_to.frame("mainFrame")
        ree.single_check(0)
        # 移动到已发送目录，并对提示信息进行验证
        ree.move_to_sent()
        sleep(1)
        self.driver.switch_to.default_content()
        # TODO:类似这种地方是否要使用try，之后再做修改吧
        assert(ree.get_message_box() == "已将邮件成功移动 [查看] [撤销]"), "移动信件失败"
        # 进一步验证已发送目录下的信件有没有增加，获取已发送信件数量：mail_num2
        mail_num2 = ree.sent_mail_statistics()
        assert(int(mail_num2) - int(mail_num1) == 1), "信件没有移动到已发送目录"

    def test2_move_to_sent(self):
        """测试随机批量勾选邮件标移动到已发送"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 先进入已发送目录，得到初始的已发送信件数：mail_num1
        ree = ReceiveEmail(self.driver)
        mail_num1 = ree.sent_mail_statistics()
        # 进入收件箱
        ree.goto_inbox()
        # 随机批量勾选:暂定三个
        self.driver.switch_to.frame("mainFrame")
        ree.check_multi(0)
        # 移动到已发送目录，并对提示信息进行验证
        ree.move_to_sent()
        sleep(1)
        self.driver.switch_to.default_content()
        ree.prompt_confirmation(1)
        # TODO:类似这种地方是否要使用try，之后再做修改吧
        assert(ree.get_message_box() == "已将邮件成功移动 [查看] [撤销]"), "移动信件失败"
        # 进一步验证已发送目录下的信件有没有增加，获取已发送信件数量：mail_num2
        mail_num2 = ree.sent_mail_statistics()
        assert(int(mail_num2) - int(mail_num1) == 3), "信件没有移动到已发送目录"

    def test3_move_to_sent(self):
        """测试按发件人姓名勾选邮件移动到已发送"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 先进入已发送目录，得到初始的已发送信件数：mail_num1
        ree = ReceiveEmail(self.driver)
        mail_num1 = ree.sent_mail_statistics()
        # 进入收件箱
        ree.goto_inbox()
        # 按发件人姓名勾选
        self.driver.switch_to.frame("mainFrame")
        ree.check_by_sender("罗江华", 0)
        # 移动到已发送目录，先处理掉提示框，再对提示信息进行验证
        ree.move_to_sent()
        sleep(1)
        self.driver.switch_to.default_content()
        ree.prompt_confirmation(1)
        # TODO:类似这种地方是否要使用try，之后再做修改吧
        assert(ree.get_message_box() == "已将邮件成功移动 [查看] [撤销]"), "移动信件失败"
        # 进一步验证已发送目录下的信件有没有增加，获取已发送信件数量：mail_num2
        mail_num2 = ree.sent_mail_statistics()
        assert(int(mail_num2) - int(mail_num1) == 25), "信件没有移动到已发送目录"

    def test4_move_to_sent(self):
        """测试勾选当页全部邮件移动到已发送"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 先进入已发送目录，得到初始的已发送信件数：mail_num1
        ree = ReceiveEmail(self.driver)
        mail_num1 = ree.sent_mail_statistics()
        # 进入收件箱,并全选
        ree.goto_inbox()
        self.driver.switch_to.frame("mainFrame")
        ree.all_check()
        # 移动到已发送目录，对提示信息进行验证
        ree.move_to_sent()
        sleep(1)
        self.driver.switch_to.default_content()
        ree.prompt_confirmation(1)
        # TODO:类似这种地方是否要使用try，之后再做修改吧
        assert(ree.get_message_box() == "已将邮件成功移动 [查看] [撤销]"), "移动信件失败"
        # 进一步验证已发送目录下的信件有没有增加，获取已发送信件数量：mail_num2
        mail_num2 = ree.sent_mail_statistics()
        assert(int(mail_num2) - int(mail_num1) == 25), "信件没有移动到已发送目录"


if __name__ == '__main__':
    unittest.main()
