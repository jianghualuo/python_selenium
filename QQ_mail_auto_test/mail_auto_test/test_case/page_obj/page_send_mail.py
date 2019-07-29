from .Page import PageBase
from selenium.webdriver.common.by import By


class PageSendMail(PageBase):
    """
    定义邮件发送模型
    """
    receiver_loc = (By.ID, "toAreaCtrl")
    subject_loc = (By.ID, "subject")
    send_loc = (By.XPATH, "//div[@id='toolbar' and @class='clear']/div/a[1]")
    send_success_loc = (By.ID, "sendinfomsg")
    errmsg_loc = (By.CLASS_NAME, "errmsg")

    def type_receiver(self, *args):
        # 添加收件人地址
        for add in args:
            self.find_element(*self.receiver_loc).send_keys(add)

    def type_subject(self, text):
        # 添加主题
        self.find_element(*self.subject_loc).send_keys(text)

    def type_mail_body(self):
        # TODO:待做
        # 添加邮件正文
        pass

    def type_send(self):
        # 点击邮件正文下方发送按钮
        self.find_element(*self.send_loc).click()

    def send_success_hint(self):
        # 检测邮件是否发送成功，检测提示信息
        text = self.find_element(*self.send_success_loc).text
        assert(text == "您的邮件已发送"), "邮件没有发送成功!"

    def errmsg(self):
        # 检测报错提示信息
        errmsg = self.find_element(*self.errmsg_loc).text
        assert(errmsg == "请填写收件人后再发送"), "未检测到填写收信人的提示语"

    def accept_alert(self):
        # 提示框确认
        self.driver.switch_to_alert().accept()

    def dismiss_alert(self):
        # 提示框取消
        self.driver.switch_to_alert().dismiss()

    def send_to_alert(self, keys):
        # 像提示框发送关键字
        self.driver.switch_to_alert().send_keys(keys)


