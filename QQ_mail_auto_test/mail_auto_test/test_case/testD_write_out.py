import unittest
import sys
import time
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_send_email import PageSendMail
from models.myunit import MyTest
from models.function import get_screenshot


class TestWriteOut(MyTest):
    """关闭写信页面测试"""

    def test1_write_out(self):
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
        time.sleep(1)
        # 通过页面的title来验证页面是否跳转了
        assert(self.driver.title == "QQ邮箱"), "写信未关闭"

    def test2_write_out(self):
        """添加了邮件主题或正文，关闭写信页面，且不将改动存为草稿"""
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
        # 关闭写信
        pse.type_exit()
        time.sleep(2)
        # 对提示框进行选择：否
        self.driver.switch_to.default_content()
        pse.select_leave_tip(2)
        time.sleep(1)
        # 通过页面的title来验证页面是否跳转了
        assert(self.driver.title == "QQ邮箱"), "写信未关闭"

    def test3_write_out(self):
        """添加了邮件主题或正文，关闭写信页面，且将改动存为草稿"""
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
        # 关闭写信
        pse.type_exit()
        time.sleep(2)
        # 对提示框进行选择：是
        self.driver.switch_to.default_content()
        pse.select_leave_tip(1)
        time.sleep(1)
        # 是否保存为草稿
        text = self.driver.find_element_by_xpath("//div[@id='msgBoxDIV']/span").text
        now = time.strftime("%H:%M")
        assert(text == now + " 邮件成功保存到草稿箱"), "未保存成功"
        time.sleep(1)
        # 通过页面的title来验证页面是否跳转了
        assert(self.driver.title == "QQ邮箱"), "写信未关闭"


if __name__ == '__main__':
    unittest.main()
