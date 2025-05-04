from pages.base_page import BasePage

class HomePage(BasePage ):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.home_link = "#home"

    def go_to_home(self):
        # self.home_link.click()
        self.perform_action(self.home_link, "click")
