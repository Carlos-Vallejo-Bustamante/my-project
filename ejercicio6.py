from selenium import webdriver
from selenium.webdriver.common.by import By

"""
crear 10 elementos dándole a "add" en esta web 
https://the-internet.herokuapp.com/add_remove_elements/ 
y luego borrarlos dándole a "delete"
"""

driver = webdriver.Chrome()

URL = 'https://the-internet.herokuapp.com/add_remove_elements/'
driver.get(URL)


def push_button_add():
    click_button = driver.find_element(By.CSS_SELECTOR, '#content > div > button')
    click_button.click()


def push_button_remove():
    click_button = driver.find_element(By.CSS_SELECTOR, '#elements > button')
    click_button.click()


try:
    for i in range(11):
        push_button_add()
    for i in range(11):
        push_button_remove()
    assert AssertionError('Error')
finally:
    print('Final script')
