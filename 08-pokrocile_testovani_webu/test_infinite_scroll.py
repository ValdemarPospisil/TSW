from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_infinite_scroll():
    driver = webdriver.Firefox()
    try:
        driver.get(
            "https://infinite-scroll.com/demo/full-page/"
        )  # Changed to basic demo which works better
        time.sleep(2)

        # Get initial count of items
        items = driver.find_elements(By.CSS_SELECTOR, ".item")
        initial_count = len(items)
        print(f"Initial count: {initial_count}")

        # Scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for loading

        # Get new count
        items = driver.find_elements(By.CSS_SELECTOR, ".article")
        new_count = len(items)
        print(f"New count: {new_count}")

        assert (
            new_count > initial_count
        ), f"Expected more items after scroll ({new_count} > {initial_count})"
        print("Test prošel - načetly se nové položky po scrollování.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_infinite_scroll()
