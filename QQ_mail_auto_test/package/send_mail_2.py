import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.qq.com"

sender = "1414710823@qq.com"
receiver = "18827453452@163.com"

user = "1414710823@qq.com"
password = "ejgqcjukfjmggjai"

subject = "python send mail test"

send_file = open("./2019-06-28 11-17-01result.html", "rb").read()

att = MIMEText(send_file, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment; filename='2019-06-28 11-17-01result.html'"

msgRoot = MIMEMultipart("related")
msgRoot["subject"] = subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
