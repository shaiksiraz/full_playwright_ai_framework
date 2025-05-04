from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_success(page):
    homepage=HomePage(page)
    login = LoginPage(page)
    # basepage = BasePage(page)
    # BasePage.goto("https://qa-automation-practice.netlify.app/")
    login.goto("https://qa-automation-practice.netlify.app/")
    homepage.go_to_home()
    # login.login("user", "pass")
    assert "qa-automation-practice" in page.url.lower()
