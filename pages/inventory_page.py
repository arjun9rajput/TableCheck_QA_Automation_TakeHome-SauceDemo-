import allure

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_items = page.locator('.inventory_item')
        self.cart_button = page.locator('.shopping_cart_link')
        self.continue_shopping = page.locator('#continue-shopping')

    @allure.step("View item: {item_name}")
    def view_item(self, item_name: str):
        item = self.page.locator(f'text={item_name}')
        item.click()

    @allure.step("Add item to cart: {item_name}")
    def add_item_to_cart(self, item_name: str):
        item = self.page.locator(f'text={item_name}').locator('..').locator('button')
        item.click()

    @allure.step("Go to cart")
    def go_to_cart(self):
        self.cart_button.click()

    @allure.step("Got back to inventory")
    def got_back_to_inventory(self):
        self.continue_shopping.click()