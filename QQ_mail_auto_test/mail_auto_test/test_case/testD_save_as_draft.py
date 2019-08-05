import unittest
import sys
import re
import time
sys.path.append("./page_obj")
sys.path.append("./models")
from page_obj.page_login import PageLogin
from page_obj.page_send_email import PageSendMail
from models.myunit import MyTest
from models.function import get_screenshot


class TestSaveAsDraft(MyTest):
    """发送邮件测试"""

    def test_save_as_draft(self):
        """写信存为草稿测试"""
        # 快捷登录网页
        pl = PageLogin(self.driver)
        pl.quick_login()
        # 进行email发送操作
        pse = PageSendMail(self.driver)
        # 进入写信页面
        pse.goto_letter()
        # 定位到“草稿箱”，并获取到初始数字
        text_1 = self.driver.find_element_by_id("folder_4").text
        num_1 = re.search("\d+", text_1).group()
        # 切换到iframe表单mainFrame
        self.driver.switch_to.frame("mainFrame")
        # 点击“存草稿”按钮
        pse.type_save_draft()
        time.sleep(1)
        # 第一种验证根据页面提示
        # self.driver.switch_to.default_content()
        # now = time.strftime("%H:%M")
        # assert(pse.get_message_box() == now + " 邮件成功保存到草稿箱"), "未保存成功"

        # 第二种验证根据左侧导航列表“草稿箱”后面的数字做判断，在添加草稿前就要获取一次然后存为操作后再次获取一次，判断是否增加。此种验证可以用到正则表达式去获取数字
        # 再次定位“草稿箱”，并获取数字
        self.driver.switch_to.default_content()
        text_2 = self.driver.find_element_by_id("folder_4").text
        num_2 = re.search("\d+", text_2).group()
        assert(num_2 > num_1), "未保存成功"


if __name__ == '__main__':
    unittest.main()
