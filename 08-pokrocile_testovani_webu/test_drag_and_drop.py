from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_drag_and_drop():
    driver = webdriver.Firefox()
    try:
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(0)
        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")
        ActionChains(driver).drag_and_drop(source, target).perform()
        assert "Dropped!" in target.text
        print("Test prošel.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_drag_and_drop()
