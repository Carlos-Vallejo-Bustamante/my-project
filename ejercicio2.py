import requests
import json

# Ejercicio 2

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

A = 1
B = 2

params = {
    'a': A,
    'b': B
}

response_get = requests.get(URL, params=params)
print(response_get.text)

if float(response_get.text) != 3:
    raise AssertionError()

response_post = requests.post(URL, json=params)
print(response_post.json()['result'])


