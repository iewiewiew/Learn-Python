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


def send_multiple_reports(senderMail, authCode, receiverMail, basePath):
    subject = 'JMeter测试报告'

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        print('成功连接到邮件服务器')
        server.login(senderMail, authCode)
        print('成功登录邮箱')

        for filename in os.listdir(basePath):
            if filename.startswith('result') and filename.endswith('.tar.gz'):
                filepath = os.path.join(basePath, filename)
                # filepath = basePath + 'result_20240408142600.tar.gz'

                msgRoot = MIMEMultipart('related')
                msgRoot['Subject'] = subject + filename
                msgRoot['From'] = senderMail
                msgRoot['To'] = receiverMail

                msgAtv = MIMEMultipart('alternative')
                msgRoot.attach(msgAtv)

                html_content = '''
                    <p>请下载附件查收 JMeter 测试报告</p>
                '''
                html = MIMEText(html_content, 'html', 'utf-8')
                msgAtv.attach(html)

                with open(filepath, 'rb') as file:
                    tar_gz_content = file.read()

                annex = MIMEBase('application', 'x-gzip')
                annex.set_payload(tar_gz_content)
                encoders.encode_base64(annex)

                annex.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filepath))
                annex.add_header('Content-Type', 'application/x-gzip')

                msgRoot.attach(annex)

                server.sendmail(senderMail, receiverMail, msgRoot.as_string())
                print('邮件发送成功: {}'.format(filename))

        print('所有测试报告已发送')
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
    basePath = '/Users/menghuawei/PycharmProjects/my-project/Learn-Python/.gitee/tmp/'
    # basePath = '/root/gitee-performance-testing/result/'
    send_multiple_reports(senderMail, authCode, receiverMail, basePath)
