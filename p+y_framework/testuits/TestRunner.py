import unittest
import os
import HTMLTestRunner
import time
from testuits.test_get_page_title import GetPageTitle
from  testuits.baidu_search import BaiduSearch

report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))

HtmlFile = report_path + now + 'HTMLtemplate.html'
fp = open(HtmlFile,'wb')
# suite = unittest.TestSuite()
# # suite.addTest(BaiduSearch('test_baidu_search'))#一个一个用例明去加
# # suite.addTest(GetPageTitle('test_get_title'))
# suite =  unittest.TestSuite(unittest.makeSuite(BaiduSearch))#加载类下的所有用例
# suite(unittest.makeSuite(GetPageTitle))
suite = unittest.TestLoader().discover('testuits')#加载包下的所有测试用例

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='testreport',description='testqingkuang')
    runner.run(suite)
