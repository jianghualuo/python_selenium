import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # 定义存放路径
    fp = open('./result.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况')
    runner.run(discover)
    fp.close()  # 关闭报告文件
