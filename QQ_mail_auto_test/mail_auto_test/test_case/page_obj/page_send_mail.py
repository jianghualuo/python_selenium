from .Page import PageBase
from selenium.webdriver.common.by import By
from time import sleep


class PageSendMail(PageBase):
    """
    定义邮件发送模型
    """
    receiver_loc = (By.ID, "toAreaCtrl")
    subject_loc = (By.ID, "subject")
    send_loc = (By.ID, "subject")

    def type_receiver(self, *args):
        for add in args:
            self.find_element(*self.receiver_loc).send_keys(add)

    def type_subject(self, text):
        self.find_element(*self.subject_loc).send_keys(text)

    def type_send(self):
        self.find_element(*self.send_loc).click()
