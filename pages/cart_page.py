# pages/cart_page.py

from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_item = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_item_name(self):
        # Return the name of the item in cart
        return self.driver.find_element(*self.cart_item).text

    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    checkout_button = (By.ID, "checkout")

    def click_cart_icon(self):
        print("[CartPage] Clicking on cart icon...")
        self.driver.find_element(*self.cart_icon).click()

    def click_checkout(self):
        print("[CartPage] Clicking on checkout button...")
        self.driver.find_element(*self.checkout_button).click()