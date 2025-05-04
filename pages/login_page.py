from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        # self.username_input = page.locator("#username")
        # self.password_input = page.locator("#password")
        # self.login_button = page.locator("button[type='submit']")

    # def login(self, username, password):
    #     self.username_input.fill(username)
    #     self.password_input.fill(password)
    #     self.login_button.click()
    def goto(self, url):
        return self.page.goto(url)
