import allure

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.config import Config


@allure.feature('Cart')
class TestCart:
    @allure.story('Add and verify items in cart')
    def test_add_items_to_cart(self, login_user):
        inventory_page = InventoryPage(login_user.page)
        cart_page = CartPage(login_user.page)
        inventory_page.add_item_to_cart('Sauce Labs Backpack')
        inventory_page.go_to_cart()
        assert cart_page.verify_item_in_cart('Sauce Labs Backpack')

    @allure.story('Verify items can be removed from cart')
    def test_verify_items_in_cart(self, login_user):
        cart_page = CartPage(login_user.page)
        cart_page.remove_from_cart('Sauce Labs Backpack')
        assert not cart_page.verify_item_in_cart('Sauce Labs Backpack')

    @allure.story('Verify can go back to inventory page after adding item to cart')
    def test_verify_can_go_back_to_inventory_page(self, login_user):
        inventory_page = InventoryPage(login_user.page)
        cart_page = CartPage(login_user.page)
        inventory_page.add_item_to_cart('Sauce Labs Backpack')
        inventory_page.go_to_cart()
        assert cart_page.verify_item_in_cart('Sauce Labs Backpack')
        inventory_page.got_back_to_inventory()
        inventory_page.add_item_to_cart("Sauce Labs Bike Light")
        inventory_page.go_to_cart()
        assert cart_page.verify_item_in_cart("Sauce Labs Bike Light")
