import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email

logging.info("==================== 测试开始 =======================")

suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file,'wb') as f:
    HTMLTestRunner(stream=f, title="Dop Test", description="DOP自动化测试").run(suite)

send_email(report_file)
logging.info("==================== 测试结束 =======================")