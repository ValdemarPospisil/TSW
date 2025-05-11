from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.FirefoxOptions()
options.headless = False

driver = webdriver.Firefox(options=options)

try:
    driver.get("https://portal.ujep.cz")

    username_input = driver.find_element(By.NAME, "loginName")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys("st98265")
    password_input.send_keys("x0207112510")

    password_input.send_keys(Keys.RETURN)

    # login_button = driver.find_element(By.ID, "login_button_id")  # Uprav ID
    # login_button.click()

    time.sleep(5)

    try:
        user_panel = driver.find_element(By.XPATH, "//a[contains(text(), 'My study')]")
        print("✅ Test přihlášení prošel – uživatel je přihlášen.")
    except Exception as e:
        print("❌ Test selhal – uživatel není přihlášen.", str(e))


except Exception as e:
    print("❌ Test selhal:", str(e))

finally:
    driver.quit()
