from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver

    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def enter_first_name(self, first_name):
        print("[CheckoutStepOnePage] Entering first name...")
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        print("[CheckoutStepOnePage] Entering last name...")
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        print("[CheckoutStepOnePage] Entering postal code...")
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    def click_continue(self):
        print("[CheckoutStepOnePage] Clicking Continue button...")
        self.driver.find_element(*self.continue_button).click()