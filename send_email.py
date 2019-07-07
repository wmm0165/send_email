# -*- coding: utf-8 -*-
# @Time : 2019/7/7 17:07
# @Author : wangmengmeng
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


def send_email():
    #   打开报告文件读取文件内容
    # filename = './report/'+ time.strftime('%Y-%m-%d %H_%M_%S')
    # f = open(filename, 'r')
    # file_msg = f.read()
    file_msg = '<html><h1> python test send imail</h1></html>'
    # print(filename)
    # print(file_msg)
    # f.close()
    #   邮件服务器
    smtpserver = 'smtp.qq.com'
    #   发件人用户名和密码
    user = '2548558583@qq.com'
    password = 'gzrbuvesszycdifb'  # 授权码
    #   发件人
    sender = '2548558583@qq.com'
    #   收件人
    receiver = '2548558583@qq.com'
    #   邮件主题
    subject = 'Python test send email'
    #   邮件设置
    msg = MIMEText(file_msg, 'html', 'utf-8')
    msg['subject'] = Header(subject, 'utf-8')
    msg['from'] = sender
    #   连接服务器，登录服务器，发送邮件
    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpserver, 465)
    smtp.login(user, password)
    try:
        smtp.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print('send failed', e)
    else:
        print('send success！')
    smtp.quit()  # 结束SMTP会话
    print('send email success!')


if __name__ == '__main__':
    send_email()
