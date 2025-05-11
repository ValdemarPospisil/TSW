from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_storage():
    driver = webdriver.Firefox()
    try:
        driver.get("https://example.com")
        
        # Test sessionStorage
        driver.execute_script("sessionStorage.setItem('test_key', '42');")
        session_value = driver.execute_script("return sessionStorage.getItem('test_key');")
        assert session_value == "42"
        
        # Test localStorage
        driver.execute_script("localStorage.setItem('test_key', '42');")
        local_value = driver.execute_script("return localStorage.getItem('test_key');")
        assert local_value == "42"
        
        print("Test prošel.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_web_storage()
