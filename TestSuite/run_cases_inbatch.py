import unittest
import os
from report import HTMLTestRunner_PY3
#查询测试用例路径
case_path = os.path.join(os.getcwd())
print(os.getcwd())
print(case_path)
def allcases():
    rule = "case*.py"
    pa = "F:\\xiecheng_UI_auto\\TestSuite"
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    report_dir = "F:\\xiecheng_UI_auto\\TestSuite\\test_report.html"
    fp = open(report_dir,"wb")
    runCaseReport = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp,title="测试报告",description="输出测试用例执行结果")
    runCaseReport.run(allcases())
