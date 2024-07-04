from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield Browser(page)
        context.close()
        browser.close()


class Browser:
    def __init__(self, page):
        self.page = page
