# 声明一个测试套件
import unittest

import HTMLTestRunner

from unnitest_test import DemoTests
from 爬虫.Pyquery_test import get_novel

suite = unittest.TestSuite()
# 添加测试用例到测试套件
suite.addTest(DemoTests('test_01'))
suite.addTest(DemoTests('test_02'))
suite.addTest(DemoTests('test_03'))
suite.addTest(DemoTests("test_04"))
suite.addTest(DemoTests('test_05'))
# 创建一个新的测试结果文件
buf = open("D:\\result.html", "wb")

runner = HTMLTestRunner.HTMLTestRunner(stream=buf,
                                       title="411 Test Result",
                                       description="Test Case Run Result")
# 运行测试，并且将结果生成为HTML
runner.run(suite)

# 关闭文件输出

buf.close()
