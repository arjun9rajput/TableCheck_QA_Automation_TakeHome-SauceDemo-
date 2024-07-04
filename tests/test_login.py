import pytest
from pages.login_page import LoginPage
from utils.config import Config
import allure


@allure.feature('Login')
class TestLogin:
    @allure.story('Valid login')
    def test_valid_login(self, browser):
        login_page = LoginPage(browser.page)
        login_page.goto(Config.BASE_URL)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        assert login_page.get_title() == "Swag Labs"

    @allure.story('Invalid login')
    def test_invalid_login(self, browser):
        login_page = LoginPage(browser.page)
        login_page.goto(Config.BASE_URL)
        login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
        assert login_page.get_error_message() == ('Epic sadface: Username and password do not match any user in this '
                                                  'service')
