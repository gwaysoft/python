#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.ebaotech.com"  # 设置服务器
mail_user = "MISAD"  # 用户名
mail_pass = "dt_P6NbY"  # 口令

sender_default = 'misad@ebaotech.com'
receiver_default = 'oa@ebaotech.com'
receivers_default = [receiver_default]

subject_default = "from python"
message_default = "from python"


def sendEmail(sender=sender_default, receiver=receiver_default, subject=subject_default, content=message_default):
    # print(sender, receiver, subject, content)
    retStr = "send email successfully"
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    # message['From'] = Header("oa", 'utf-8')  # 发送者
    # message['To'] = Header("oa", 'utf-8')  # 接收者

    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, [receiver], message.as_string())
    except smtplib.SMTPException:
        retStr = "send email failed"
    return retStr


def sendEmails(sender=sender_default, receivers=receivers_default, subject=subject_default, content=message_default):
    # print(sender,receivers,subject,content)
    retStr = "send email successfully"

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    # message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
    # message['To'] = Header("测试", 'utf-8')  # 接收者

    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        retStr = "send email failed"
    return retStr


def main():
    print(sendEmail(sender="silei.yang@ebaotech.com", receiver="david.wei@ebaotech.com", subject="hello"))
    print(sendEmails(receivers=["david.wei@ebaotech.com"]))


if __name__ == '__main__':
    main()
    pass
