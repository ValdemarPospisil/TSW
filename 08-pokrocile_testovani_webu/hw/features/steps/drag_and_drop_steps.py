from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

@given('I open the drag and drop demo page')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://jqueryui.com/droppable/")

@when('I switch to the iframe')
def step_impl(context):
    context.driver.switch_to.frame(0)

@when('I drag the source element to the target')
def step_impl(context):
    source = context.driver.find_element(By.ID, "draggable")
    target = context.driver.find_element(By.ID, "droppable")
    ActionChains(context.driver).drag_and_drop(source, target).perform()

@then('the target should show "Dropped!"')
def step_impl(context):
    target = context.driver.find_element(By.ID, "droppable")
    assert "Dropped!" in target.text
    context.driver.quit()
