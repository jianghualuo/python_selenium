from time import sleep
from .Page import PageBase
from selenium.webdriver.common.by import By
import pyautogui
import os


class PageSendMail(PageBase):
    """
    定义邮件发送模型
    """
    letter_loc = (By.ID, "composebtn")
    receiver_loc = (By.XPATH, "//div[@id='toAreaCtrl']/div[2]/input")
    subject_loc = (By.ID, "subject")
    send_loc = (By.XPATH, "//div[@id='toolbar' and @class='clear']/div/a[1]")
    time_send_loc = (By.XPATH, "//div[@id='toolbar' and @class='clear']/div/a[2]")
    save_draft_loc = (By.XPATH, "//div[@id='toolbar' and @class='clear']/div/a[3]")
    exit_loc = (By.XPATH, "//div[@id='toolbar' and @class='clear']/div/a[4]")
    upload_attachment_loc = (By.XPATH, "//span[@id='AttachFrame']/span/input")
    send_success_loc = (By.ID, "sendinfomsg")
    errmsg_loc = (By.CLASS_NAME, "errmsg")
    frame_2_loc = (By.XPATH, "//div[@id='QMEditorArea']/table/tbody/tr[2]/td/iframe")
    body_loc = (By.TAG_NAME, "body")

    def goto_letter(self):
        # 进入“写信”页面
        self.find_element(*self.letter_loc).click()
        sleep(2)

    def type_receiver(self, *arg):
        # 添加收件人地址
        self.find_element(*self.receiver_loc).send_keys(*arg)

    def type_subject(self, text):
        # 添加主题
        self.find_element(*self.subject_loc).send_keys(text)

    def upload_attachment(self):
        # 添加附件
        # 该input标签不能够使用click方法点击，
        # 可以定位到input标签后，使用send_keys直接将要上传文件的路径发过去，这种方法比较可靠。
        # self.find_element(*self.upload_attachment_loc).send_keys(file)
        # sleep(3)

        # 可以尝试使用pyautogui模拟鼠标点击
        pyautogui.click(310, 354)
        os.system("F:\\Git_lib\\python_selenium\\QQ_mail_auto_test\\package\\upfiles.exe")

    def type_mail_body(self, body_text):
        # 添加邮件正文
        # 正文区域是第二层嵌套页面，这里直接定位到第二层嵌套里，定位第一层不在这里做处理
        f = self.find_element(*self.frame_2_loc)
        self.driver.switch_to.frame(f)
        # 输入正文
        self.find_element(*self.body_loc).click()
        self.find_element(*self.body_loc).send_keys(body_text)
        # 切换到上一层表单页面
        self.driver.switch_to.parent_frame()

    def type_send(self):
        # 发送
        self.find_element(*self.send_loc).click()

    def type_time_send(self):
        # 定时发送
        self.find_element(*self.time_send_loc).click()

    def type_save_draft(self):
        # 存草稿
        self.find_element(*self.save_draft_loc)

    def type_exit(self):
        # 退出
        self.find_element(*self.exit_loc)

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


