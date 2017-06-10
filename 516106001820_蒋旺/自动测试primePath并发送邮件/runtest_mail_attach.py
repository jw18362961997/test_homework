from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


#=====================定义发送邮件====================
def send_mail (file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = '18362961997@163.com'
    password = '18362961997JW'
    sender = '18362961997@163.com'
    receiver = '1111@qq.com'
    subject = 'primerPath的unit test自动化测试报告'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')                      
    msgRoot['From'] = sender
    msgRoot['To'] = receiver

    msgRoot.attach(MIMEText('这是蒋旺的primerPath的unit test测试报告!', 'plain', 'utf-8'))

    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="jw_report.html"'
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print ('email has send out !')


#=====查找测试报告目录，找到最新生产的测试报告文件========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print ('文件相对路径：' + file_new)
    return file_new


if __name__ == '__main__':
    
    test_dir = 'test_case'
    test_report = 'report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = test_report + '/蒋旺unit_test-' + now + '-result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,              
                        title='primePath unit test测试报告',               
                        description='测试结果：') 
    runner.run(discover)   
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)   # 发送测试报告
