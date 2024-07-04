import allure

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator('#checkout')

    @allure.step("Remove item '{item_name}' from cart")
    def remove_from_cart(self, item_name):
        self.page.click(f"text=Remove, {item_name}")

    @allure.step("Verify item '{item_name}' is in cart")
    def verify_item_in_cart(self, item_name: str):
        item = self.page.locator(f'text={item_name}')
        return item.is_visible()

    @allure.step("Proceed to checkout")
    def checkout(self):
        self.checkout_button.click()
