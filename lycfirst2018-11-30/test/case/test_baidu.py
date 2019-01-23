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
    # base_path = os.path.dirname(os.path.abspath(__file__) ) + '\..' #获取当前文件夹路径+\..
    # driver_path = os.path.abspath(base_path + '\driver\chromedriver.exe') #拼接谷歌ide位置绝对路径
   # locator_kw = (By.ID, 'kw')
   # locator_su = (By.ID, 'su')
    #locator_result = (By.XPATH,'//div[contains(@class,"result")]/h3/a') #xpath 搜索结果

    def sub_setUp(self):  #self  本身的意思     setup开始的时候先执行   一次
        #self.driver = webdriver.Chrome(executable_path = DRIVER_PATH + '\chromedriver.exe')  #执行路径（drive.path）文件
       # self.driver.get(self.URL)
        #初始页面main page，传入浏览器类型打开浏览器
        self.page = BaiDuResultPage(browser_type='chrome').get(self.URL,maximize_windows=False)

    def sub_tearDown(self):   #tesrdown    结束的时候执行一次
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                #self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                #self.driver.find_element(*self.locator_su).click()
                self.page.serch(d['search'])
                time.sleep(2)
                #links = self.driver.find_elements(*self.locator_result)
                self.page = BaiDuResultPage(self.page)#跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


#     def test_search_0(self):   #执行一次测试方法  算是测试用例
#         self.driver.find_element(*self.locator_kw).send_keys('selenium ') #  *是  把参数列表分开传
# # driver.find_element(*locator_su).send_keys("selenium 灰蓝")
#         self.driver.find_element(*self.locator_su).click()
#         time.sleep(5)
#         links = self.driver.find_elements(*self.locator_result)  #找多个要加s   elements
#         for link in links:
#             # print(link.text)
#             logger.info(link.text)
#     def test_search_1(self):   #执行一次测试方法  算是测试用例了
#         self.driver.find_element(*self.locator_kw).send_keys('自动化')
#         self.driver.find_element(*self.locator_su).click()
#         time.sleep(3)
#         links = self.driver.find_elements(*self.locator_result)
#         for link in links:
#             # print(link.text)
#             logger.info(link.text)
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


# print(*locator_kw)
# print(locator_kw)

