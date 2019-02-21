from framework.base_page import BasePage
from pageobjects.baidu_homepage import HomePage

class NewsHomePage(HomePage):
    sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[7]/a"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
