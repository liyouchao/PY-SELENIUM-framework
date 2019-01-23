import unittest
from utils.config import Config,REPORT_PATH
from utils.client import HTTPclient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import asserHTTPCode

class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPclient(url=self.URL,method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        #self.assertIn('百度一下，你就知道',res.text)  #断言
        asserHTTPCode(res,[500])
        self.assertIn('百度er下，你就知道！',res.text)

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='超哥接口测试',description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))