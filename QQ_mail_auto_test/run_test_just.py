import unittest
import time
from HTMLTestRunner import HTMLTestRunner

test_dir = "./mail_auto_test/test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test7*.py')


if __name__ == '__main__':
    # 定义存放路径
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    fp_name = "./mail_auto_test/report/" + now + "result.html"
    fp = open(fp_name, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况')
    runner.run(discover)
    fp.close()  # 关闭报告文件
