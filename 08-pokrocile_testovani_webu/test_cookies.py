from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cookies():
    driver = webdriver.Firefox()
    try:
        driver.get("https://example.com")

        # Add a cookie
        driver.add_cookie(
            {"name": "test_cookie", "value": "12345", "domain": "example.com"}
        )

        # Refresh page
        driver.refresh()

        # Verify cookie exists
        test_cookie = driver.get_cookie("test_cookie")
        assert test_cookie is not None
        assert test_cookie["value"] == "12345"

        print("Test prošel.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_cookies()
