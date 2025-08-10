import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckoutStepOne:
    def test_checkout_step_one_valid_info(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login("performance_glitch_user","secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_first_item_to_cart()

        cart = CartPage(driver)
        cart.click_cart_icon()
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_checkout_info("John", "Doe", "12345")

        assert checkout.is_on_checkout_step_two()