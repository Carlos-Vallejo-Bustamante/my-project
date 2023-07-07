from behave import *
from selenium.webdriver.common.by import By


@given('el usuario esta registrado')
def step_impl(context):
   pass


@when('cuando introduce un nombre de usuario')
def step_impl(context):
   context.driver.find_element(By.ID, 'username').send_keys('tomsmith')


@when('cuando introduce un nombre falso de usuario')
def step_impl(context):
   context.driver.find_element(By.ID, 'username').send_keys('nombrefalso')


@when('cuando introduce su password')
def step_impl(context):
   context.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')


@when('el usuario pulsa login')
def step_impl(context):
   context.driver.find_element(By.CSS_SELECTOR, '#login > button').click()


@then('el usuario accede al portal')
def step_impl(context):
      assert context.driver.find_element(By.CSS_SELECTOR, '#content > div > a').is_displayed()


@then('el usuario no puede acceder al portal')
def step_impl(context):
      assert context.driver.find_element(By.CSS_SELECTOR, '#login > button').is_displayed()
