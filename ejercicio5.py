from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

URL = 'https://the-internet.herokuapp.com/tables'
driver.get(URL)

tabla = driver.find_element(By.ID, 'table1')

filas = tabla.find_elements(By.TAG_NAME, "tr")

lista_filas = []
lista_precio = []

for fila in filas:
    lista_filas.append(fila.text)

for fila in lista_filas:
    cut_fila = fila.split()
    lista_precio.append(cut_fila[3])
    print(fila)

print(lista_filas)
print(lista_precio)
driver.quit()
