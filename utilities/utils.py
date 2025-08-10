import os
from datetime import datetime

def capture_screenshot(driver, name):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(filepath)
    print(f"\nScreenshot saved to: {filepath}")