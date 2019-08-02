import unittest
import sys
from time import sleep
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_send_email import PageSendMail
from models.myunit import MyTest
from models.function import get_screenshot


class TestWriteOut(MyTest):
    """关闭写信页面测试"""

    def aest1_write_out(self):
        """未添加任何邮件内容，关闭写信页面"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面
        pse.goto_letter()
        # 点击关闭
        self.driver.switch_to.frame("mainFrame")
        pse.type_exit()
        sleep(1)
        # 通过页面的title来验证页面是否跳转了
        assert(self.driver.title == "QQ邮箱"), "写信未关闭"

    def test2_write_out(self):
        """添加了邮件主题或正文，关闭写信页面，对提示框的处理"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面
        pse.goto_letter()
        # 切换到iframe表单mainFrame
        self.driver.switch_to.frame("mainFrame")
        # 添加主题
        pse.type_subject("python selenium send email test")
        # 点击关闭
        pse.type_exit()
        # 接收并确认警告
        pse.accept_alert()


if __name__ == '__main__':
    unittest.main()
