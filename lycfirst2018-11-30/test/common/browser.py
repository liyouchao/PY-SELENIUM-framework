import time,os
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH

#可以根据传入的参数选择浏览器的driver去打开对应浏览器，并加一一个保存截图的方法，可以保存png到report目录下

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + 'phantomjs.exe'

TYPES = {'firefox':webdriver.Firefox,'chrome':webdriver.Chrome,'ie':webdriver.Ie,'phantomjs':webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox':'wires','chrome':CHROMEDRIVER_PATH,'ie':IEDRIVER_PATH,'phantomjs':PHANTOMJSDRIVER_PATH}

class UnSupportBrowserTypeError(Exception): #找不到浏览器类型的错误
    pass

class Browser(object):
    def __init__(self,browser_type='firefox'):  #初始化数据
        self._type = browser_type.lower()  #变小数
        if self._type in TYPES:
            self.browser = TYPES[self._type]  #拿到webriver.firfox
        else:
            raise UnSupportBrowserTypeError('仅支持%S!'%','.join(TYPES.keys()))
            #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
            #近支持字典中的值，如：仅支持webdriver.firefox，webdriver.chrome，...
        self.driver = None  #定义为空

    def get(self,url,maximize_window = True,implicitly_wait = 30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self,name='screen_shot'):
        day = time.strftime('%Y%m%d',time.localtime(time.time())) #以定义的格式生成，time.localtime(time.time())拆分当前时间（2018,12,21.。。）
        screenshot_path = REPORT_PATH + '\screenshot_%s'% day #存放路径加时间
        if not os.path.exists(screenshot_path): #如果不存在就创建
            os.makedirs(screenshot_path) #创建路径

        tm = time.strftime('%H%M%S',time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name,tm))#格式日期\\时间.png
        return screenshot

    def closs(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()