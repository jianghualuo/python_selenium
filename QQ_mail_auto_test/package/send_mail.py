import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtp_server = "smtp.qq.com"

# 发送邮箱用户名和密码
user = "1414710823@qq.com"
password = "ejgqcjukfjmggjai"

# 发送邮箱
sender = "1414710823@qq.com"

# 接受邮箱
receiver = "18827453452@163.com"

# 发送邮件主题
subject = "Python email test"

# 编写HTML类型的邮件正文
msg = MIMEText("<html><h1>你好！</h1></html>", "html", "utf-8")
msg["subject"] = Header(subject, "utf-8")

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

