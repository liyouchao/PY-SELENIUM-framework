from framework.base_page import BasePage
from pageobjects.baidu_news_home import NewsHomePage

class SportNewsHomePage(NewsHomePage):
    nba_link = "xpath=>//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)