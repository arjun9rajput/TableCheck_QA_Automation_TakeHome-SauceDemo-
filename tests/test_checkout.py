import allure

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


@allure.feature('Checkout')
class TestCheckout:
    @allure.story('Verify Price and Complete checkout')
    def test_complete_checkout(self, login_user):
        inventory_page = InventoryPage(login_user.page)
        cart_page = CartPage(login_user.page)
        checkout_page = CheckoutPage(login_user.page)
        inventory_page.add_item_to_cart('Sauce Labs Backpack')
        inventory_page.add_item_to_cart('Sauce Labs Bike Light')
        inventory_page.add_item_to_cart('Sauce Labs Fleece Jacket')
        inventory_page.go_to_cart()
        cart_page.checkout()
        checkout_page.fill_address('John', 'Doe', '12345')
        assert checkout_page.verify_total_price()
        checkout_page.complete_checkout()
        assert checkout_page.finish_button.is_hidden()
