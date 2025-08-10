from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class InventoryPage:
    add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
    cart_icon = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = ("id", "add-to-cart-sauce-labs-backpack")  # <- correct locator
     
    def add_to_cart_by_product_id(self, product_id):
        print(f"[InventoryPage] Adding to cart: {product_id}")
        self.driver.find_element("id", f"add-to-cart-{product_id}").click()
    
    def add_to_cart_backpack(self):
        print("[InventoryPage] Adding backpack to cart...")
        self.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()

    def add_first_item_to_cart(self):
        print("[InventoryPage] Adding first item to cart...")
        self.driver.find_element(*self.add_to_cart_button).click()
    

    
    def get_cart_count(self):
       print("[InventoryPage] Getting cart count...")
       try:
           return self.driver.find_element(*self.cart_icon).text
       except NoSuchElementException:
        return None 
    
    def remove_first_item_from_cart(self):
        remove_button = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove_button.click()