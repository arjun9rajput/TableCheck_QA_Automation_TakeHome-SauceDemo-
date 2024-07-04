import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.add_to_cart_button = page.locator(".btn_inventory")
        self.back_to_products_button = page.locator("#back-to-products")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_button = page.locator("#logout_sidebar_link")

    @allure.step("Add product to cart")
    def add_to_cart(self):
        self.add_to_cart_button.click()

    @allure.step("Go back to products")
    def go_back_to_products(self):
        self.back_to_products_button.click()

    @allure.step("logs user out")
    def logout(self):
        self.menu_button.click()
        self.logout_button.click()
