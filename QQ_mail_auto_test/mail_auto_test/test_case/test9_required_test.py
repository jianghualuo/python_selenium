import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_send_email import PageSendMail
from models.myunit import MyTest
from models.function import get_screenshot
from time import sleep


class TestRequired(MyTest):
    """测试写信必填项：收信人、主题、正文"""

    def test1_send_no_receiver(self):
        """未填写收信人直接点击发送（预期：不能发送）"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面，直接点击发送按钮
        pse.goto_letter()
        self.driver.switch_to.frame("mainFrame")
        pse.type_send()
        # 无法发送，检测提示
        self.driver.switch_to.default_content()
        assert(pse.get_message_box(0) == "请填写收件人后再发送"), "没有请填写收件人的提示"
        # 再检测页面是否发生了跳转 TODO:这个地方写的对不对，有没有必要
        try:
            self.driver.switch_to.frame("mainFrame")
            pse.send_success_hint()
        except:
            pass

    def qtest2_send_no_subject(self):
        """未添加主题点击发送（预期：会弹出提示框并确认发送）"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面，并添加收信人地址
        pse.goto_letter()
        self.driver.switch_to.frame("mainFrame")
        pse.type_receiver("18827453452@163.com;")
        # 然后直接点击发送按钮
        pse.type_send()
        # 对出现的提示框进行确认
        self.driver.switch_to.default_content()
        pse.prompt_confirmation(0)
        sleep(3)
        # 检测邮件是否发送成功
        self.driver.switch_to.frame("mainFrame")
        pse.send_success_hint()

    def qtest3_send_no_body(self):
        """未添加主题点击发送（预期：可以发送）"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面
        pse.goto_letter()
        self.driver.switch_to.frame("mainFrame")
        # 添加收信人地址，可以添加多个，请按xxxx@xxx.com;的格式添加
        pse.type_receiver("18827453452@163.com;", "1414710823@qq.com;")
        # 添加主题
        pse.type_subject("python selenium send email test subject")
        # 发送邮件
        pse.type_send()
        sleep(3)
        # 检测邮件发送或是否成功
        pse.send_success_hint()


if __name__ == '__main__':
    unittest.main()
