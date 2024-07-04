import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.allure_utils import take_screenshot
from utils.config import Config
from utils.browser import browser


@pytest.fixture(scope="function")
def login_user(browser):
    login_page = LoginPage(browser.page)
    product_page = ProductPage(browser.page)

    login_page.goto(Config.BASE_URL)
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

    assert product_page.get_title() == "Swag Labs"

    yield browser

    # Logout the user after each test
    product_page.logout()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        take_screenshot(item.funcargs["browser"].page, item.name)
