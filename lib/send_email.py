import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header
from config.config import *
import sys
sys.path.append('..')
def send_email(report_file):

#   编写邮件内容
#with open('report.html',encoding='utf-8') as f: # 打开html报告
#     email_body = f.read()    # 读取报告内容
    msg = MIMEMultipart()       # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

#   组装Email头（发件人，收件人，主题）
    msg['From'] = '鹿鹿鹿'                                                     # 发件人
    msg['To'] = 'lujun.song@daocloud.io'                                      # 收件人
    msg['Subject'] = Header(subject,'utf-8')                                  # 中文邮件主题，指定utf-8编码

#  构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8')          # 二进制格式打开
    att1['Content-Type'] = 'application/octe-tream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)       # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        # 4. 连接smtp服务器并发送邮件
        smtp = smtplib.SMTP_SSL(smtp_server)                                   # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user, smtp_password)                                    # 用户名和密码
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送成功")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()



