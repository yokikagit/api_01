import os
import time
import unittest
import HTMLTestRunner_PY3
from BeautifulReport import BeautifulReport
from script.test_login import TestLogin

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TestLogin))
suite = unittest.TestLoader().discover(BASE_DIR + "/script/", "test*.py")

# filename = "report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# BeautifulReport(suite).report(description="TPshop登录接口测试", filename=filename, log_path=BASE_DIR + "/report/")

filename = BASE_DIR + "/report/report.html"
with open(filename, "wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, verbosity=1, title="登录接口测试", description="另一种测试报告模板")
    runner.run(suite)
