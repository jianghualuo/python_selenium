import os

# 定义查找文件目录路径
report_dir = "D:\\Git_lib\\python_selenium\\QQ_mail_auto_test\\mail_auto_test\\report"

# 返回目录下所有文件名
lists = os.listdir(report_dir)

# 对文件名按时间进行排序(升序)，获取最新的report
lists.sort(key=lambda fn: os.path.getmtime(report_dir + "\\" + fn))

print("最新的文件为：" + lists[-1])
# 返回最新result的路径及文件名称
file = os.path.join(report_dir, lists[-1])
print(file)
