from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given("I open the file upload page")
def step_impl3(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://the-internet.herokuapp.com/upload")


@when('I select the file "{file_path}"')
def step_impl4(context, file_path):
    upload = context.driver.find_element(By.ID, "file-upload")
    upload.send_keys(file_path)


@when("I click the upload button")
def step_impl5(context):
    context.driver.find_element(By.ID, "file-submit").click()
    time.sleep(2)


@then('I should see the "{message}" message')
def step_impl6(context, message):
    actual_message = context.driver.find_element(By.TAG_NAME, "h3").text
    assert message in actual_message
    context.driver.quit()
