import os,time
from selenium import webdriver
import  unittest
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test.page.baidu_result_page import BaiDuResultPage,BaiDuMainPage

class Testbaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH +'/baidu.xlsx'


    def sub_setUp(self):  #self  本身的意思     setup开始的时候先执行   一次
		self.page = BaiDuResultPage(browser_type='chrome').get(self.URL,maximize_windows=False)

    def sub_tearDown(self):   #tesrdown    结束的时候执行一次
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.serch(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)#跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    # unittest.main(verbosity=2)   #执行用例
    report = REPORT_PATH +'\\peport.html'
    with open(report,'wb')as f:
        runner = HTMLTestRunner(f,verbosity=2,title='lyc开始',description='lyc修改报告')
        runner.run(Testbaidu('test_search'))
    # e = Email(title='百度测试报告',
    #           message='这个是今天的测试报告，请查收！',
    #           receiver='757515065@qq.com',
    #           server='smtp.exmail.qq.com',
    #           sender='liyouchao@u-road.com',
    #           password='d42ega9qheaGrEjc',
    #           path = report
    #           )
    # e.send()

