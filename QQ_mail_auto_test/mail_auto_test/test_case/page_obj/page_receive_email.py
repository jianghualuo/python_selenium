from .Page import PageBase
from selenium.webdriver.common.by import By
from time import sleep
import random

class ReceiveEmail(PageBase):
    """
    定义收取邮件模型
    """

    inbox_loc = (By.ID, "readmailbtn_link")
    errmsg_loc = (By.CLASS_NAME, "errmsg")
    del_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/a[1]")
    completely_del_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/a[2]")
    forward_email_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/a[3]")
    report_spam_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/a[4]")
    setall_readed_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/a[5]")
    # 标记为已读
    mark_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/span/a")
    read_loc = (By.ID, "select_QMMenu__menuitem_read")
    unread_loc = (By.ID, "select_QMMenu__menuitem_unread")
    star_loc = (By.ID, "select_QMMenu__menuitem_star")
    unstar_loc = (By.ID, "select_QMMenu__menuitem_unstar")
    newtag_loc = (By.ID, "select_QMMenu__menuitem_newtag")
    # 移动到
    move_loc = (By.XPATH, "//form[@id='frm']/div/div[2]/span[2]/a")
    fid_1_loc = (By.ID, "select_QMMenu__menuitem_fid_1")
    fid_3_loc = (By.ID, "select_QMMenu__menuitem_fid_3")
    fid_130_loc = (By.ID, "select_QMMenu__menuitem_fid_130")
    new_loc = (By.ID, "select_QMMenu__menuitem_new")

    checkbox_loc = (By.CSS_SELECTOR, "[type='checkbox'][unread='false']")

    def goto_inbox(self):
        self.find_element(*self.inbox_loc).click()
        sleep(2)

    def errmsg(self):
        text = self.driver.find_elemnent(*self.errmsg_loc).text
        assert(text == "未选中任何邮件"), "没有检测到为勾选的提示语"

    def all_check(self):
        # 勾选所有邮件
        self.find_elements(*self.checkbox_loc).click()

    def single_check(self):
        # 随机选择一个信件，一页最多显示25封信
        checkbox = self.find_elements(*self.checkbox_loc)
        checkbox[random.randint(0, 24)].click()

    def check_multi(self):
        # 随机选择多个邮件，一页最多显示25封信
        checkbox = self.find_elements(*self.checkbox_loc)
        for i in range(3):
            checkbox[random.randint(0, 24)].click()

    def check_by_sender(self, sender_name):
        # 按发件人的姓名勾选邮件
        checkbox = self.find_elements(*self.checkbox_loc)
        for i in checkbox:
            if i.get_attribute("fn") == sender_name:
                i.click()

    def check_mode(self, n):
        # 页面提供的快捷选择邮件的方式
        # 0：全部；1：无；2：已读；3：未读；
        loc = [(By.LINK_TEXT, "全部"), (By.LINK_TEXT, "无"), (By.LINK_TEXT, "已读"), (By.LINK_TEXT, "未读")]
        self.find_element(*loc[n]).click()

    def del_email(self):
        # 删除
        self.find_element(*self.del_loc).click()

    def completely_del_email(self):
        # 彻底删除
        self.find_element(*self.completely_del_loc).click()

    def forward_email(self):
        # 转发
        self.find_element(*self.forward_email_loc).click()

    def report_spam(self):
        # 举报垃圾邮件
        self.find_element(*self.report_spam_loc).click()

    def set_all_readed(self):
        # 全部标记为已读
        self.find_element(*self.setall_readed_loc).click()

    def mark_as_read(self):
        # 标记为已读
        # TODO:验证方法未写
        self.find_element(*self.mark_loc).click()
        self.find_element(*self.read_loc).click()

    def mark_as_unread(self):
        # 标记为未读
        # TODO:验证方法未写
        self.find_element(*self.mark_loc).click()
        self.find_element(*self.unread_loc).click()

    def mark_as_star(self):
        # 标记为星标
        # TODO:验证方法未写
        self.find_element(*self.mark_loc).click()
        self.find_element(*self.star_loc).click()

    def mark_as_unstar(self):
        # 取消星标
        # TODO:验证方法未写
        self.find_element(*self.mark_loc).click()
        self.find_element(*self.unstar_loc).click()

    def newtag(self):
        # 新建标签
        # TODO:验证方法未写
        self.find_element(*self.mark_loc).click()
        self.find_element(*self.unstar_loc).click()

    def move_to_inbox(self):
        # 移动到收件箱
        # TODO:验证方法未写
        self.find_element(*self.move_loc).click()
        self.find_element(*self.fid_1_loc).click()

    def move_to_sent(self):
        # 移动到已发送
        # TODO:验证方法未写
        self.find_element(*self.move_loc).click()
        self.find_element(*self.fid_3_loc).click()

    def move_to_subscription(self):
        # 移动到订阅
        # TODO:验证方法未写
        self.find_element(*self.move_loc).click()
        self.find_element(*self.fid_130_loc).click()

    def new_folder(self):
        # 新建文件夹
        # TODO:验证方法未写
        self.find_element(*self.move_loc).click()
        self.find_element(*self.new_loc).click()

    def accept_alert(self):
        # 提示框确认
        self.driver.switch_to_alert().accept()

    def dismiss_alert(self):
        # 提示框取消
        self.driver.switch_to_alert().dismiss()

    def send_to_alert(self, keys):
        # 像提示框发送关键字
        self.driver.switch_to_alert().send_keys(keys)
