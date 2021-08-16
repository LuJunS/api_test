import logging
import os

#请求信息

headers = {"Content-type": "application/json", "charset": "UTF-8","OpenAPI-Tenant-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Mjg1OTI5NTUsImluZm8iOnsiaWQiOiJhZjJiNjQ1NC1jYTZmLTQwZTAtOTU5OC0yY2MwMThjNGIzYWYifX0.-HDVbYymVRSaGklMG3KMnSKYhICA6Z_jMEbVGPtifYE8"}

#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath('pythonProject/DOP_API')))
data_path = os.path.join(prj_path, 'data')
test_path = os.path.join(prj_path, 'test')

log_file = os.path.join(prj_path, 'log', 'log.txt')
report_file = os.path.join(prj_path, 'report', 'report.html')


#log配置
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 日志输出文件

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '741928012@qq.com'
smtp_password = 'vheyiztrdytwbdei'

sender = smtp_user  # 发件人
receiver = 'lujun.song@daocloud.io'  # 收件人
subject = '接口测试报告'  # 邮件主题

