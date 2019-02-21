import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngin(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriver.exe'

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser = config.get('browserType','browserName')
        logger.info('you had select %s browser.' % browser)
        url = config.get('testServer','URL')
        logger.info('the test server url is : %s'% url)

        if browser =='Firefox':
            driver = webdriver.Firefox()
            logger.info('starting Firefox browser.')
        elif browser == 'chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('starting chrome browser.')
        elif browser == 'IE':
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info('starting ie borwser')

        driver.get(url)
        logger.info('open url : %s' % url)
        driver.maximize_window()
        logger.info('maximize the current window.')
        driver.implicitly_wait(10)
        logger.info('set implicitly wait 10 seconds.')
        return driver
    def quit_browser(self):
        logger.info('now close and quit thw browser.')
        self.driver.quit()
