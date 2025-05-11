from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Spuštění WebDriveru
driver = webdriver.Firefox()
driver.get("https://portal.ujep.cz/portal/studium/prohlizeni.html")

time.sleep(2)  # Počkej na načtení stránky

try:
    prohlizeni_link = driver.find_element(By.CLASS_NAME, "xg_stag_a_titulka")
    prohlizeni_link.click()

    time.sleep(2)

    # Výběr fakulty
    fakulta_select = Select(driver.find_element(By.ID, "browserFakulta"))
    fakulta_select.select_by_value("FSE")

    # Výběr formy studia
    forma_select = Select(driver.find_element(By.ID, "searchForma"))
    forma_select.select_by_value("P")

    # Kliknutí na tlačítko hledání
    driver.find_element(By.ID, "searchProgramySubmit").click()

    # Počkej na načtení výsledků
    time.sleep(3)

    prohlizeni_link_predmetu = driver.find_element(By.ID, "nalezenyProgramId_3")
    prohlizeni_link_predmetu.click()

    time.sleep(5)

    print("Test filtrů prošel úspěšně.")

except Exception as e:
    print("Chyba během testu:", str(e))

finally:
    driver.quit()
