from selenium import webdriver
from selenium.webdriver.common.by import By


def test_example_domain():
    driver = webdriver.Firefox()
    try:
        driver.get("https://example.com")
        h1_text = driver.find_element(By.TAG_NAME, "h1").text
        assert h1_text == "Example Domain"
        print("Test prošel.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_example_domain()
