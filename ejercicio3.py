import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.eltiempo.es/madrid.html")

get_temp = driver.find_element(By.CSS_SELECTOR, "#headerCity > div.-block-3.c-wrapper-pois > section > div.c6.-a-top > section.-block-i-1.-b-center.temperature > span").text

temp = float(get_temp[0:2])

T_B = 20
T_M = 30

try:
    for i in range(3):
        if temp > T_M:
            print('Hace mucho calor')
            break
        elif temp < T_B:
            print('Hace frio')
            break
        elif temp < T_M:
            print('Hace buen tiempo')
            break
    assert AssertionError('Error')

finally:
    time.sleep(3)
    driver.close()

