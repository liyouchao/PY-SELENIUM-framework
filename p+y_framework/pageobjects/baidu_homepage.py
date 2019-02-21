from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_bth = "xpath=>//*[@id='su']"
    new_link = "xpath=>//*[@id='u1']/a[1]"


    def type_search(self,text):
        self.type(self.input_box,text)

    def send_submit_btn(self):
        self.click(self.search_submit_bth)

    def click_news(self):
        self.click(self.new_link)
        self.sleep(2)

