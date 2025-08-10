import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestAddToCart:
    def test_add_item_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        time.sleep(1)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(1)

        inventory_page = InventoryPage(driver)
        inventory_page.add_first_item_to_cart()
        time.sleep(1)

        assert inventory_page.get_cart_count() == "1"
        time.sleep(1) 