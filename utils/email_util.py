# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/7/10 14:03
@description  发送邮件
"""
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# 发送简单邮件
def send_simple_email(senderMail, authCode, receiverMail):
    # 邮件主题
    subject = '简单邮件测试'
    # 邮件内容
    content = 'hello email'
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = senderMail
    msg['To'] = receiverMail

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        print('成功连接到邮件服务器')
        server.login(senderMail, authCode)
        print('成功登录邮箱')
        server.sendmail(senderMail, receiverMail, msg.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送异常')
    finally:
        server.quit()


# 发送复杂邮件
def send_complex_email(senderMail, authCode, receiverMail):
    # 邮件主题
    subject = '复杂邮件测试'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = senderMail
    msgRoot['To'] = receiverMail

    msgAtv = MIMEMultipart('alternative')
    msgRoot.attach(msgAtv)
    # html
    html_content = '''
    <p>知乎：</p>
    <p><a href='https://www.zhihu.com/'>点击进入知乎</a></p>
    <p>图像：</p>
    <p><img src="cid:image"></p>
    '''
    html = MIMEText(html_content, 'html', 'utf-8')
    msgAtv.attach(html)
    f = open('../docs/测试工程师技能图谱.png', 'rb')
    msgImage = MIMEImage(f.read())
    f.close()
    msgImage.add_header('Content-ID', '<image>')
    msgRoot.attach(msgImage)

    # 附件
    annex = MIMEText(open('../file/txt/test.txt', 'rb').read(), 'base64', 'utf-8')
    annex['Content-Type'] = 'application/octet-stream'
    annex['Content-Disposition'] = 'attachment; filename="test.txt"'
    msgRoot.attach(annex)

    # 读取 test.tar.gz 文件内容
    tar_gz_path = '../file/tar/test.tar.gz'
    with open(tar_gz_path, 'rb') as file:
        tar_gz_content = file.read()

    # 创建 MIMEBase 对象
    annex = MIMEBase('application', 'x-gzip')
    annex.set_payload(tar_gz_content)
    encoders.encode_base64(annex)

    # 设置附件的文件名和文件类型
    annex.add_header('Content-Disposition', 'attachment', filename=os.path.basename(tar_gz_path))
    annex.add_header('Content-Type', 'application/x-gzip')

    # 将附件添加到消息的根部
    msgRoot.attach(annex)

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        print('成功连接到邮件服务器')
        server.login(senderMail, authCode)
        print('成功登录邮箱')
        server.sendmail(senderMail, receiverMail, msgRoot.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送异常')
    finally:
        server.quit()


if __name__ == '__main__':
    # 发送者邮箱地址
    senderMail = '1010293890@qq.com'
    # 发送者 QQ 邮箱授权码
    authCode = 'wiigqubmdactbbbd'
    # 接收者邮箱地址
    receiverMail = '1425615649@qq.com'

    send_simple_email(senderMail, authCode, receiverMail)
    send_complex_email(senderMail, authCode, receiverMail)
