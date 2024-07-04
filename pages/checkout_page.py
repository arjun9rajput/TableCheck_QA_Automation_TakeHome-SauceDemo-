import allure

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.locator('#first-name')
        self.last_name_input = page.locator('#last-name')
        self.postal_code_input = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')
        self.finish_button = page.locator('#finish')

    @allure.step("Fill address: {first_name} {last_name}, {postal_code}")
    def fill_address(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    @allure.step("Complete checkout")
    def complete_checkout(self):
        self.finish_button.click()

    def get_item_prices(self):
        # Locate all item price elements
        price_elements = self.page.locator('.inventory_item_price')
        # Extract text content from each price element and convert to float
        prices = [float(price.text_content().replace('$', '')) for price in price_elements]
        return prices

    def get_total_price(self):
        # Locate the total price element
        total_price_element = self.page.locator('.summary_total_label')
        # Extract text content from the total price element and convert to float
        total_price = float(total_price_element.text_content().replace('Total: $', ''))
        return total_price

    @allure.step("Verify total price is correct")
    def verify_total_price(self):
        # Get the sum of individual item prices
        item_prices = self.get_item_prices()
        sum_of_item_prices = sum(item_prices)

        # Get the total price displayed on the page
        displayed_total_price = self.get_total_price()

        # Compare the sum of item prices with the displayed total price
        return sum_of_item_prices == displayed_total_price
