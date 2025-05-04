import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context_args(args):
    return {**args, "ignore_https_errors": True}

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        new_page = context.new_page()
        yield new_page
        browser.close()
