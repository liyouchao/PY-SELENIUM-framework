import time,unittest
from framework.browser_engine import BrowserEngin
from  pageobjects.baidu_homepage import HomePage
from  pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportNewsHomePage

class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngin(self)
        self.driver = browse.open_browser(self)


    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
                # time.sleep(2)
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        try:
            assert 'selenium' in self.driver.title
            print('test pass.')
        except Exception as e:
            print('test fail.',format(e))
    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(5)
    # def test_view_nba_views(self):
    #     baiduhome = HomePage(self.driver)
    #     baiduhome.click_news()
    #
    #     # self.driver.find_element_by_xpath("//*[@id='u1']/a[1]").click()
    #
    #     newshome = NewsHomePage(self.driver)
    #     # self.driver.find_element_by_xpath("//*[@id='channel-all']/div/ul/li[7]/a").click()
    #     newshome.click_sports()
    #
    #
    #     sportnewhome = SportNewsHomePage(self.driver)
    #     sportnewhome.click_nba_link()
    #     # self.driver.find_element_by_xpath("//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a").click()
    #     sportnewhome.get_window_img()

if __name__ == '__main__':
    unittest.main()