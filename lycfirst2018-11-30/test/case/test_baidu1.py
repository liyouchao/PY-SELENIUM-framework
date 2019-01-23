import os,time
import  unittest
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from test.page.baidu_result_page import BaiDuResultPage,BaiDuMainPage #继承后有全部的方法

class Testbaidu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH +'/baidu.xlsx'

    def sub_setUp(self):  #self  本身的意思     setup开始的时候先执行   一次
        #初始页面main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL)

    def sub_tearDown(self):   #tesrdown    结束的时候执行一次
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
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

