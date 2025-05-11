from selenium import webdriver
from selenium.webdriver.common import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def test_file_download():
    download_dir = os.path.abspath("./downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = webdriver.FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    options.set_preference("pdfjs.disabled", True)
    
    driver = webdriver.Firefox(options=options)
    try:
        driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
        
        try:
            consent_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-consent"))
            )
            consent_button.click()
            print("Cookie banner zavřen.")
        except:
            print("Cookie banner se nezobrazil.")

        download_link = driver.find_element(By.CLASS_NAME, "download-button")
        download_link.click()
        time.sleep(10)
        
        downloaded_files = [f for f in os.listdir(download_dir) if f.endswith(".pdf")]
        assert len(downloaded_files) > 0
        print(f"Test prošel. Stažené soubory: {downloaded_files}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_file_download()
