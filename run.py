import sys,time,os
import re
import unittest
from dep import HTMLTestRunner
from run_switch import run_switch
from comnon import open_broswer


def create_suite():
    '''在case包下，获取测试用例'，并添加早测试套件'''
    test_dir = 'case'
    test_unit = unittest.TestSuite()
    tests = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py',top_level_dir=None)
    for test_suit in tests:
        for test in test_suit:
            p = re.compile(r'<unittest.suite.TestSuite tests=\[<(APP|PC|displayboard)\.(.*?)\.')
            search = p.search(str(test))
            if search and search.groups(0):
                case_name = search.groups(0)[1]
                if hasattr(run_switch, case_name) and getattr(run_switch, case_name) == 1:
                    test_unit.addTest(test)
    print(test_unit)
    return test_unit


'''执行用例，生成测试报告'''
test_report = './report/'
time = time.strftime('%Y_%m_%d_%H_%M_%S')
report_name = test_report+time+'_result.html' #定义报告存放路径
fp = open(report_name, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream = fp, \
                        title=u'智能会议测试报告', description=u'用例执行情况：') #定义测试报告
runner.run(create_suite()) #运行测试用例
fp.close()

'''用例执行完，自动在浏览器中打开测试报告'''
cwd_path = os.getcwd()
file_url = 'file:////' + cwd_path + report_name[1:]
report = open_broswer.WebClient(file_url)
report.run_chrome()