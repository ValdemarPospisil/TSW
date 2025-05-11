from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


def test_file_upload():
    driver = webdriver.Firefox()
    try:
        driver.get("https://the-internet.herokuapp.com/upload")

        test_file_path = (
            "/home/valdemar/Documents/4.Semestr/SWI/CodeReviews/coderabbit_haskell.txt"
        )
        upload = driver.find_element(By.ID, "file-upload")
        upload.send_keys(test_file_path)

        driver.find_element(By.ID, "file-submit").click()
        time.sleep(2)

        message = driver.find_element(By.TAG_NAME, "h3").text
        assert "File Uploaded!" in message
        print("Test prošel.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_file_upload()
