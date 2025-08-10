# tests/test_remove_from_cart.py

import pytest
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestRemoveFromCart:
    def test_remove_item_from_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        time.sleep(1)

        inventory_page = InventoryPage(driver)
        inventory_page.add_first_item_to_cart()
        time.sleep(1)
        inventory_page.remove_first_item_from_cart()
        time.sleep(1)

        assert inventory_page.get_cart_count() is None, "Cart should be empty after removing item"