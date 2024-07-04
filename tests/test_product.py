import allure

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage


@allure.feature("Product page tests")
class TestProduct:
    @allure.story("Verify can view and add product")
    def test_view_and_product(self, login_user):
        inventory_page = InventoryPage(login_user.page)
        product_page = ProductPage(login_user.page)
        cart_page = CartPage(login_user.page)
        inventory_page.view_item("Sauce Labs Bolt T-Shirt")
        product_page.add_to_cart()
        product_page.go_back_to_products()
        inventory_page.go_to_cart()
        assert cart_page.verify_item_in_cart('Sauce Labs Bolt T-Shirt')
