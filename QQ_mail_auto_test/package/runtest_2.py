import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

test_dir = './'
report_dir = 'D:\\Git_lib\\python_selenium\\QQ_mail_auto_test\\mail_auto_test\\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


# 定义邮件发送
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, "html", "uft-8")
    msg["subject"] = Header("自动化测试报告", "utf-8")

    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("1414710823@qq.com", "ejgqcjukfjmggjai")
    smtp.sendmail("1414710823@qq.com", "18827453452@163.com", msg.as_string())
    smtp.quit()
    print("email has send out")


# 定义查找最新的测试报告文件
def report_new(report_dir):
    lists = os.listdir(report_dir)
    # 对文件名按时间进行排序(升序)，获取最新的report
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + "\\" + fn))
    # 返回最新result的路径及文件名称
    file_new = os.path.join(report_dir, lists[-1])
    return file_new

if __name__ == '__main__':
    # 定义存放路径
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    fp_name = "D:\\Git_lib\\python_selenium\\QQ_mail_auto_test\\mail_auto_test\\report\\" + now + "result.html"
    fp = open(fp_name, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况')
    runner.run(discover)
    fp.close()  # 关闭报告文件
    file_new = report_new(report_dir)
    send_mail(file_new)
