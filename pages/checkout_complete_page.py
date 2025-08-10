from selenium.webdriver.common.by import By

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.back_home_button = (By.ID, "back-to-products")

    def get_complete_header_text(self):
        return self.driver.find_element(*self.complete_header).text

    def is_back_home_button_displayed(self):
        return self.driver.find_element(*self.back_home_button).is_displayed()