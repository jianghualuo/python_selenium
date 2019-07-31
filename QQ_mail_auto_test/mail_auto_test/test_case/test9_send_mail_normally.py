import unittest
import sys
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_send_email import PageSendMail
from models.myunit import MyTest
from models.function import get_screenshot
from time import sleep


class TestSendMail(MyTest):
    """发送邮件测试"""

    def test_send_mail(self):
        """发送邮件的最基本流程测试"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面
        pse.goto_letter()
        # 切换到iframe表单mainFrame
        self.driver.switch_to.frame("mainFrame")
        # 添加收信人地址，可以添加多个，请按xxxx@xxx.com;的格式添加
        pse.type_receiver("18827453452@163.com;", "1414710823@qq.com;")
        # 添加主题
        pse.type_subject("python selenium send email test subject")
        # 添加正文
        body_text = "hello! this is email test!" \
                    "thanks"
        pse.type_mail_body(body_text)
        # 发送邮件
        pse.type_send()
        sleep(3)
        # 检测邮件发送或是否成功
        get_screenshot(self.driver, "./mail_auto_test/report/img/login_ok.jpg")
        pse.send_success_hint()


if __name__ == '__main__':
    unittest.main()
