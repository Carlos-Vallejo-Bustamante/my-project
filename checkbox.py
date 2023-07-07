import requests
import json
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

URL = 'https://mtp.alejmans.dev/maas/proxy/test/checkbox'
boo_response = json.loads(requests.get(URL).text)
check1 = boo_response['checkbox 1']
check2 = boo_response['checkbox 2']

try:
    def click_check(check1, check2):
        if check1:
            pass
        else:
            try:
                no_checked = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
                no_checked.click()
                time.sleep(3)
            except NoSuchElementException:
                pass

        if check2:
            pass
        else:
            try:
                no_checked = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')
                no_checked.click()
                time.sleep(3)
            except NoSuchElementException:
                pass

    click_check(check1, check2)
    time.sleep(3)
    click_check(check1, check2)
    time.sleep(3)
    click_check(check1, check2)
finally:
    print('Final')
    driver.quit()

